"""Deployment regression checks for the KINETIC v8 navy/ice-blue theme.

These are deterministic code and accessibility checks, not a claim that Streamlit
Community Cloud was opened in a browser during this test run.
"""
from pathlib import Path
import re
import tomllib
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / 'core/styles.py').read_text(encoding='utf-8')
APP = (ROOT / 'app.py').read_text(encoding='utf-8')
SVG = (ROOT / 'assets/kinetic-network.svg').read_text(encoding='utf-8')


def _luminance(colour: str) -> float:
    h = colour.lstrip('#')
    rgb = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    linear = [(v / 12.92) if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
    return .2126 * linear[0] + .7152 * linear[1] + .0722 * linear[2]


def _contrast(foreground: str, background: str) -> float:
    a, b = sorted([_luminance(foreground), _luminance(background)], reverse=True)
    return (a + .05) / (b + .05)


def test_blue_native_streamlit_theme_in_all_modes():
    conf = tomllib.loads((ROOT / '.streamlit/config.toml').read_text())
    for item in [conf['theme'], conf['theme']['light'], conf['theme']['dark']]:
        assert item['backgroundColor'] == '#071321'
        assert item['secondaryBackgroundColor'] == '#142E4C'
        assert item['textColor'] == '#F0F7FF'
    assert "active_bg.lower() == '#142e4c'" in APP
    assert 'KINETIC navy-blue theme is loaded' in APP


def test_blue_cta_and_field_text_are_accessible():
    assert _contrast('#08213B', '#A6D6FF') > 9.5
    assert _contrast('#F0F7FF', '#142E4C') > 12
    assert _contrast('#FFFFFF', '#254E78') > 7.0
    assert '.st-key-enter_kinetic button' in CSS
    assert 'background:linear-gradient(108deg,#A6D6FF,#C8E9FF)' in CSS
    assert '-webkit-text-fill-color:#08213B!important' in CSS


def test_all_widgets_and_popovers_have_dark_blue_states():
    for selector in (
        '[data-testid="stExpander"] summary:focus-visible',
        '[data-testid="stExpander"] summary[aria-expanded="true"]',
        '[data-baseweb="popover"] [role="option"][aria-selected="true"]',
        '[data-testid="stSelectbox"]:focus-within',
        '[data-testid="stTextArea"]',
        '[data-testid="stNumberInput"]',
    ):
        assert selector in CSS
    assert 'background:#254E78!important;color:#FFFFFF!important' in CSS


def test_svg_is_blue_animated_and_keeps_turbines():
    ET.fromstring(SVG)
    assert SVG.count('class="rotor"') >= 3
    assert '<animateMotion' in SVG
    assert 'prefers-reduced-motion:reduce' in SVG
    assert '#A6D6FF' in CSS
    assert 'KINETIC' in SVG
    assert 'Tobias Leung' in APP


def test_v8_previews_and_documentation_present():
    for rel in ('docs/previews/kinetic-v8-landing.png',
                'docs/previews/kinetic-v8-landing-mobile.png',
                'docs/previews/kinetic-v8-workspace.png',
                'docs/CHANGELOG_V8.md'):
        assert (ROOT / rel).exists()
