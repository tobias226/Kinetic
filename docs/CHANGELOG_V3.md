# KINETIC v3 — Design & Usability Refinement

## Why this version exists

The aim was to make the prototype easier to navigate, more visually consistent and more credible when presented to an investment professional. This iteration changes the interface, not the fundamental investment model or example scoring weights.

## What's new

- **Stronger welcome:** A larger KINETIC title, one short message and a responsive, vector connection network with moving lights and lines; graphics and copy occupy separate columns. Reduced-motion settings are respected.
- **Three conceptual lenses:** **1. Systems Thinking → Find Opportunities**, **2. Relationship Networks → Build Partnerships**, and **3. Second-Order Effects → Assess Value**. Distinct pine, moss and sage greens clarify the choices.
- **Relationship preview:** The Explore page shows the fictional contact network, with a direct route to the full network screen.
- **Simplified navigation:** Every detailed page uses **← Three Areas** plus numbered page tabs. The sidebar now contains only demo-data controls.
- **Market Signals:** Each item has **What Happened**, **Why It Matters** and **Question To Explore** panels, followed by its attributed source.
- **Dark tables & input fields:** Read-only data grids are HTML tables with dark backgrounds and escaped cell values. Edit flows use forms instead of a spreadsheet editor, including JV milestones.
- **Partnership Bridge:** A linear five-step narrative, with six separately presented real-world due-diligence questions that are **not** scored based on imaginary information.
- **Carbon scenarios:** Numbered scenario → result → second-order effects flow, with editable illustrative inputs and prominent caveats.
- **Methodology:** Plain-language explanation of systems thinking, second-order effects, invented scoring rules and known gaps.

## What has *not* changed

All pipeline opportunities, counterparties, financial figures, contacts and introductions remain fictional. No private CRM, live funding availability, investor portal or real-time market data is connected. The carbon model still compares simple cumulative emissions and undiscounted cost; it is **not** a complete valuation.

## Verification

- 25 automated checks: model calculations, data contracts, redaction, navigation structure and deterministic smoke paths through every page.
- Chromium desktop and mobile static HTML previews of the revised landing page; text-graphic intersection measured at zero in both viewport sizes.
- Static preview of the three-area menu and Market Signals cards for visual review.

A **deployed Streamlit browser test** is still recommended: the local design previews are deliberately not substitutes for a live Streamlit run. In particular, review the interaction of the custom SVG with the Streamlit frontend and check widgets against the actual version installed by Streamlit Community Cloud.
