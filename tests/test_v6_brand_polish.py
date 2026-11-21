"""Regression checks for the revised welcome and brand voice."""
import ast
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / 'app.py').read_text(encoding='utf-8')
CSS = (ROOT / 'core/styles.py').read_text(encoding='utf-8')


def test_editorial_intro_is_one_action_and_no_disclaimer():
    node = next(n for n in ast.parse(APP).body if isinstance(n, ast.FunctionDef) and n.name == 'welcome')
    src = ast.get_source_segment(APP, node)
    assert src.count('st.button(') == 1
    assert 'Connecting Ideas.' in src and 'Connecting People.' in src and 'Creating Value.' in src
    assert 'HUMAN-CENTRIC · TECHNOLOGY-ASSISTED · REAL ASSETS INTELLIGENCE' in src
    assert 'Independent interview concept' not in src
    assert 'st.caption(' not in src
    assert 'st.image(' in src


def test_entry_button_is_scoped_and_contrasting():
    scoped = CSS.split('/* KINETIC v6 — restrained editorial finish. Scoped to the welcome and entry CTA. */',1)[1]
    assert 'st-key-enter_kinetic' in scoped
    assert 'linear-gradient(108deg,#A6D6FF,#C8E9FF)' in scoped
    assert 'color:#08213B!important' in scoped
    assert '-webkit-text-fill-color:#08213B!important' in scoped
    assert '.kinetic-brand:not(.compact)' in scoped


def test_disclosures_retained_elsewhere_and_svg_loadable():
    assert 'Not an official Copley Point product' in APP
    assert 'Not commissioned or endorsed by Copley Point' in APP
    svg_file = ROOT / 'assets' / 'kinetic-network.svg'
    ET.parse(svg_file)
    graphic = svg_file.read_text(encoding='utf-8')
    assert graphic.count('class="rotor"') >= 3
    assert '<animateMotion' in graphic
