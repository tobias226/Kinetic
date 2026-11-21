"""Regression checks for final KINETIC UI polish and accessibility."""
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
STYLE = (ROOT / "core/styles.py").read_text(encoding="utf-8")
UI = (ROOT / "core/ui.py").read_text(encoding="utf-8")


def test_visible_steps_are_human_readable_without_zero_padding():
    assert "label=f'{index}.  {page}'" in APP
    for label in ("1. SYSTEMS THINKING", "2. RELATIONSHIP NETWORKS", "3. SECOND-ORDER EFFECTS"):
        assert label in APP
    assert "{number}." in UI
    assert "{i}." in APP
    for old in ("01 / SYSTEMS THINKING", "02 / RELATIONSHIP NETWORKS", "03 / SECOND-ORDER EFFECTS"):
        assert old not in APP


def test_welcome_has_name_and_exactly_one_entry_button():
    tree = ast.parse(APP)
    fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "welcome")
    source = ast.get_source_segment(APP, fn)
    assert "Tobias Leung" in source
    assert 'class="creator-credit"' in source
    assert "Explore KINETIC" in source
    assert source.count("st.button(") == 1
    assert "st.image(" in source
    assert 'Not an official Copley Point product' in APP


def test_assess_value_expanders_and_all_selected_states_are_dark():
    assert "Adjust Building & Carbon Assumptions" in APP
    assert "Optional: Compare Annual Running Costs" in APP
    assert "[data-testid=\"stExpander\"] summary:hover" in STYLE
    assert "[data-testid=\"stExpander\"] summary:focus-visible" in STYLE
    assert "[data-testid=\"stExpander\"] summary[aria-expanded=\"true\"]" in STYLE
    assert "[data-baseweb=\"popover\"] [role=\"option\"][aria-selected=\"true\"]" in STYLE
    assert "background-color:var(--kin-field-active)!important" in STYLE
    assert "color:#FFFFFF!important" in STYLE or "color:#ffffff!important" in STYLE
    assert ".creator-credit" in STYLE


def test_preserve_theme_and_navigation_integrity():
    assert (ROOT / ".streamlit" / "config.toml").exists()
    assert (ROOT / "assets" / "kinetic-network.svg").exists()
    assert 'section_navigation()' in APP
    assert "st.html(CSS)" in APP
