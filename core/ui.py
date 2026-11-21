"""Presentation helpers. All display-only tables escape user-supplied values."""
from html import escape
from typing import Iterable
import pandas as pd
import streamlit as st


def dark_table(frame: pd.DataFrame, *, highlight_columns: Iterable[str] = ()) -> None:
    """Display a readable dark table instead of Streamlit's light data-grid canvas.

    For fixed read-only examples only. Editing is always done via explicit form fields.
    """
    highlights = set(highlight_columns)
    headers = ''.join(f'<th scope="col">{escape(str(col))}</th>' for col in frame.columns)
    rows = []
    for _, row in frame.iterrows():
        cells = []
        for col in frame.columns:
            value = '' if pd.isna(row[col]) else str(row[col])
            style = ' class="cell-emphasis"' if col in highlights else ''
            cells.append(f'<td{style}>{escape(value)}</td>')
        rows.append('<tr>' + ''.join(cells) + '</tr>')
    if not rows:
        st.info('No records match your selection.')
        return
    html = (
        '<div class="kinetic-table-scroll" role="region" aria-label="Results table" tabindex="0">'
        '<table class="kinetic-table"><thead><tr>' + headers + '</tr></thead><tbody>'
        + ''.join(rows) + '</tbody></table></div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def section_step(number: int, title: str, explanation: str = '') -> None:
    description = f'<p>{escape(explanation)}</p>' if explanation else ''
    st.markdown(
        f'<div class="step-heading"><div class="step-index">{number:02d}</div>'
        f'<div class="step-copy"><h3>{escape(title)}</h3>{description}</div></div>',
        unsafe_allow_html=True,
    )


def note_card(label: str, copy: str, tone: str = 'moss', *, compact: bool = False) -> None:
    cls = (tone if tone in {'moss', 'sage', 'pine', 'gold'} else 'moss') + (' compact' if compact else '')
    st.markdown(
        f'<div class="brief-note {cls}"><div class="brief-note-label">{escape(label)}</div>'
        f'<p>{escape(copy)}</p></div>', unsafe_allow_html=True)


def hero_network() -> str:
    """Accessible responsive vector network, with subtle animated moving connection pulses.

    All coordinates are illustrative design locations, not geographical data.
    """
    edges = [
        ((260, 210), (122, 94)), ((260, 210), (385, 82)),
        ((260, 210), (454, 203)), ((260, 210), (380, 333)),
        ((260, 210), (114, 311)), ((122, 94), (385, 82)),
        ((385, 82), (454, 203)), ((454, 203), (380, 333)),
        ((380, 333), (114, 311)), ((114, 311), (122, 94)),
        ((122, 94), (82, 202)), ((82, 202), (114, 311)),
        ((454, 203), (480, 298)), ((380, 333), (480, 298)),
        ((385, 82), (478, 48)), ((122, 94), (64, 56)),
    ]
    lines = ''.join(
        f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" />'
        for a, b in edges
    )
    moving_edges = [edges[i] for i in (0, 1, 2, 3, 4, 9, 10, 12)]
    pulses = ''.join(
        '<circle r="3.2" class="mesh-particle" aria-hidden="true">'
        f'<animateMotion dur="{4.5 + i * .47:.2f}s" '
        f'begin="{-i * .78:.2f}s" repeatCount="indefinite" '
        f'path="M{a[0]} {a[1]} L{b[0]} {b[1]}" /></circle>'
        for i, (a, b) in enumerate(moving_edges)
    )
    nodes = [
        (260, 210, 12, 'core'), (122, 94, 7, 'outer'), (385, 82, 8, 'outer'),
        (454, 203, 7, 'outer'), (380, 333, 8, 'outer'), (114, 311, 7, 'outer'),
        (82, 202, 4, 'small'), (480, 298, 4, 'small'), (478, 48, 4, 'small'),
        (64, 56, 4, 'small'),
    ]
    circles = ''.join(
        f'<circle class="mesh-node {cls}" cx="{x}" cy="{y}" r="{r}" />'
        for x, y, r, cls in nodes
    )
    return f'''<div class="constellation" role="img" aria-label="Illustrative animated network connecting opportunities, people, capital and long-term value">
      <svg viewBox="0 0 520 410" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
        <defs>
          <radialGradient id="meshHalo"><stop offset="0" stop-color="#9dd9af" stop-opacity=".22"/><stop offset="1" stop-color="#9dd9af" stop-opacity="0"/></radialGradient>
          <filter id="meshGlow"><feGaussianBlur stdDeviation="4" /></filter>
        </defs>
        <circle cx="260" cy="210" r="152" fill="url(#meshHalo)" />
        <g class="mesh-orbit"><circle cx="260" cy="210" r="125"/><circle cx="260" cy="210" r="178" /></g>
        <g class="mesh-lines">{lines}</g>
        <g class="mesh-pulses">{pulses}</g>
        <circle cx="260" cy="210" r="28" fill="#75b993" opacity=".13" filter="url(#meshGlow)"/>
        <g class="mesh-nodes">{circles}</g>
        <text class="mesh-core-label" x="260" y="252" text-anchor="middle">KINETIC</text>
        <text class="mesh-label" x="120" y="78" text-anchor="middle">Opportunities</text>
        <text class="mesh-label" x="390" y="64" text-anchor="middle">Capital</text>
        <text class="mesh-label" x="443" y="184" text-anchor="middle">People</text>
        <text class="mesh-label" x="378" y="357" text-anchor="middle">Value</text>
        <text class="mesh-label" x="110" y="335" text-anchor="middle">Insight</text>
      </svg>
      <div class="visual-caption"><span class="live-dot"></span> CONNECTING IDEAS · PEOPLE · CAPITAL</div>
    </div>'''
