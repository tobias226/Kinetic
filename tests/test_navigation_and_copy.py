"""Structural UX checks that do not require a running Streamlit server."""
import ast
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
APP=ROOT.joinpath('app.py').read_text(encoding='utf-8')
STYLES=ROOT.joinpath('core/styles.py').read_text(encoding='utf-8')
TREE=ast.parse(APP)


def test_welcome_has_exactly_one_action():
    welcome=next(node for node in TREE.body if isinstance(node,ast.FunctionDef) and node.name=='welcome')
    buttons=[n for n in ast.walk(welcome) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='button']
    assert len(buttons)==1
    assert 'Explore KINETIC' in APP


def test_hub_three_areas_and_back_paths():
    assert "'Find opportunities'" in APP
    assert "'Build partnerships'" in APP
    assert "'Assess value'" in APP
    assert "navigate('Explore')" in APP
    assert "navigate('Welcome')" in APP
    assert "st.session_state.page == 'Explore'" in APP


def test_visual_accessibility_and_readable_explanations():
    assert 'prefers-reduced-motion:reduce' in STYLES
    assert '.kinetic-hero{display:grid' in STYLES
    assert 'Looking beyond the immediate decision' in APP
    assert 'What factors shape the initial score?' in APP
    assert 'six essential checks' in APP
    assert 'Relationship-access weighting' not in APP
    assert 'Point / Origin' not in APP


def test_methods_docs_exist():
    assert ROOT.joinpath('docs/PLAIN_LANGUAGE_GUIDE.md').is_file()
    assert ROOT.joinpath('docs/METHOD_AND_DATA.md').is_file()
    assert ROOT.joinpath('docs/STATIC_DESIGN_PREVIEW.html').is_file()
