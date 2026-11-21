"""Exercise every page with a deterministic Streamlit API stub.

This is not a browser test; it catches uncaught Python exceptions in the default
page paths when Streamlit is unavailable in the CI build environment.
"""
import importlib.util
import sys
import types
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['Welcome', 'Explore', 'Command Centre', 'Market Signals', 'Origination Radar',
         'Relationship Network', 'Partnership Bridge', 'Carbon Intelligence',
         'Partner Briefing Room', 'Research & Method']


class Session(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class Context:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class FakeStreamlit(types.ModuleType):
    def __init__(self, page):
        super().__init__('streamlit')
        self.session_state = Session(page=page)
        self.sidebar = Context()
        self.markdown_output = []

    def markdown(self, body, **kwargs):
        self.markdown_output.append(body)

    def columns(self, spec, **kwargs):
        return [Context() for _ in (spec if isinstance(spec, (list, tuple)) else range(spec))]

    def expander(self, *args, **kwargs):
        return Context()

    form = expander

    def button(self, *args, **kwargs):
        return False

    form_submit_button = button
    download_button = button
    checkbox = button

    def selectbox(self, label, choices, **kwargs):
        return list(choices)[kwargs.get('index', 0)]

    radio = selectbox

    def multiselect(self, label, choices, **kwargs):
        return kwargs.get('default', list(choices))

    def slider(self, label, *args, **kwargs):
        return args[2] if len(args) >= 3 else kwargs.get('value', args[0] if args else 0)

    def number_input(self, label, *args, **kwargs):
        return kwargs.get('value', args[2] if len(args) >= 3 else 0)

    def text_input(self, label, **kwargs):
        return kwargs.get('value','')

    text_area = text_input

    def date_input(self, label, **kwargs):
        return kwargs.get('value')

    def file_uploader(self, *args, **kwargs):
        return None

    def __getattr__(self, name):
        if name == 'rerun':
            return lambda: None
        if name in {'plotly_chart','metric','progress','caption','write','subheader',
                    'info','warning','error','success','set_page_config'}:
            return lambda *args, **kwargs: None
        raise AttributeError(name)


@pytest.mark.parametrize('page', PAGES)
def test_initial_page_paths_do_not_raise(page, monkeypatch):
    st = FakeStreamlit(page)
    monkeypatch.setitem(sys.modules, 'streamlit', st)
    name = 'kinetic_smoke_' + page.replace(' ','_')
    spec = importlib.util.spec_from_file_location(name, ROOT / 'app.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
        assert st.markdown_output, f'{page} emitted no content'
    finally:
        sys.modules.pop(name, None)
