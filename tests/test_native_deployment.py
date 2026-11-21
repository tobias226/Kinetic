"""Guard the hosted deployment fixes against UI regressions."""
from pathlib import Path
import ast
import tomllib
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / 'app.py').read_text(encoding='utf-8')
STYLES = (ROOT / 'core/styles.py').read_text(encoding='utf-8')
TREE = ast.parse(APP)


def test_landing_uses_native_streamlit_image_and_one_entry_button():
    page = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == 'welcome')
    funcs = [n.func.attr for n in ast.walk(page) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)]
    assert funcs.count('image') == 1
    assert funcs.count('button') == 1
    assert 'hero_network()' not in ast.get_source_segment(APP, page)
    assert 'kinetic-network.svg' in ast.get_source_segment(APP, page)
    assert 'st.html(CSS)' in APP
    assert 'st.markdown(CSS' not in APP


def test_svg_is_valid_and_contains_motion_with_static_fallback():
    svg_file = ROOT / 'assets' / 'kinetic-network.svg'
    assert svg_file.is_file()
    svg = svg_file.read_text(encoding='utf-8')
    ET.parse(svg_file)
    assert '<animateMotion' in svg
    assert 'prefers-reduced-motion:reduce' in svg
    assert svg.count('<line ') >= 20
    assert 'IDEAS · PEOPLE · CAPITAL · VALUE' in svg


def test_native_theme_is_deep_green_even_if_light_theme_selected():
    config = tomllib.loads((ROOT / '.streamlit/config.toml').read_text())
    theme = config['theme']
    assert theme['base'] == 'dark'
    for variant in [theme, theme['dark'], theme['light']]:
        for key in ['backgroundColor','secondaryBackgroundColor','textColor','borderColor']:
            assert variant[key].startswith('#')
        assert variant['backgroundColor'].lower() not in ['#ffffff','#fff']
    assert 'data-baseweb="popover"' in STYLES
    assert '[data-testid="stTextArea"] textarea' in STYLES


def test_theme_file_and_artwork_in_project_root():
    assert (ROOT/'.streamlit'/'config.toml').is_file()
    assert (ROOT/'assets'/'kinetic-network.svg').is_file()
