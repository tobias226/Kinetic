# KINETIC

### An independent concept for Copley Point Capital–relevant origination and partnership intelligence

> **Independent candidate prototype**. Not affiliated with, prepared for, commissioned by or endorsed by Copley Point Capital. **All opportunities, counterparties, contacts, introductions, capital figures and activity records are fictional.** Named existing Copley Point platforms and historical transactions are discussed only with publicly available citations.

A polished, human-led **Streamlit** app that connects the three elements of real-assets origination: **platform opportunity → right institutional investor → trusted human introduction**. Includes a separate scenario calculator that compares carbon and cash costs of industrial refurbishment and redevelopment.


## KINETIC v7 — the welcome experience

The landing message is **“Connecting Ideas. Connecting People. Creating Value.”** Beneath the KINETIC wordmark, the product is identified as **human-centric, technology-assisted real-assets intelligence**. The screen has one action, **Explore KINETIC**, with a high-contrast mint button and dark lettering. The animated graphic retains the connected network and three stylised wind turbines, while the editorial copy is intentionally concise.

The initial screen intentionally contains no hiring/interview disclaimer; the app continues to disclose its fictional sample data and independent status in the **workspace sidebar** and **Research & Method** page.

## Deployment-ready design: animation and dark form controls

KINETIC uses **Streamlit native columns and `st.image`** to show a local SVG
at `assets/kinetic-network.svg`. The landing page does **not** embed animated SVG
inside a Markdown HTML block. If a browser has reduced motion enabled, or does
not animate SVG files, the full network graphic still displays without motion.

The dark green dropdowns, text inputs and menus now primarily use official
Streamlit theme keys in `.streamlit/config.toml`, with CSS as a fallback. CSS is
inserted using `st.html()` rather than as a Markdown fragment. The actual
live app may differ subtly from the static preview due to Streamlit/browser
versions, but it should no longer default to white native inputs.

**When deploying:** Upload the *contents* of `kinetic-v7/` to the GitHub
repository root, including the **hidden `.streamlit/` directory** and the
`assets/` directory. If `.streamlit/config.toml` is missing from the remote
repository, widget colours can revert to white. Streamlit Community Cloud
will redeploy when GitHub is updated. If you still see the previous UI, reload
the app and check its Manage App / logs to confirm the new commit is deployed.
You can also open **Sidebar → Check Display Settings** inside KINETIC to see
whether the dark-green theme was loaded by Streamlit.

## Launch the app locally

Requires Python 3.10 or newer (3.11 recommended).

```bash
# Download or clone this repository and open a terminal here.
python -m venv .venv
source .venv/bin/activate                # macOS/Linux
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Your browser should open `http://localhost:8501`. If it does not, visit that URL directly.

## Deploy using GitHub + Streamlit Community Cloud

1. Create a **new GitHub repository** (e.g. `kinetic`) and upload the contents of this project folder so that `app.py`, `requirements.txt` and `.streamlit/config.toml` are in the repository root. Do not upload the outer ZIP.
2. Commit all files, including `core/`, `data/`, `docs/` and `tests/`.
3. Visit **[share.streamlit.io](https://share.streamlit.io/)**, sign in with GitHub and choose **Create app / Deploy an app**.
4. Select your repository, branch (`main`), and the main file path **`app.py`**.
5. Deploy and open the resulting app URL. No API keys, credentials or paid services are needed.

**Data behaviour:** The app runs from bundled **synthetic CSV** samples. Edits, new leads, activity logging and CSV restores are stored in **the current browser session only**. Use **sidebar → Export or restore demo data → Export CSV** to save your work; import the file to restore it. Streamlit Community Cloud containers may restart at any time, and this demo has no durable database.

**Privacy:** This is a public demonstration, not an authenticated CRM or production partner portal. Do not put genuine confidential data, contacts, credentials, client notes or proprietary underwriting into it.

## Navigate KINETIC (v7)

The introduction has **one action**, **Explore KINETIC**, with the headline **“Connecting Ideas. Connecting People. Creating Value.”**, the human-centric / technology-assisted descriptor, and a responsive animated connection network. Its moving points and integrated turbine silhouettes represent interconnected opportunities, people, capital and the long-term implications of real-asset decisions; they are **not live data**. There is a reduced-motion setting for visitors who prefer less animation.

The next page presents **three conceptual lenses**, each with a practical area title:

| Concept | Area | Pages | What it helps you demonstrate |
|---|---|---|---|
| **1. Systems Thinking** | **Find Opportunities** | Command Centre · Market Signals · Origination Radar | Understand the relationship between sectors, property or infrastructure assets, operating businesses and the next research action. |
| **2. Relationship Networks** | **Build Partnerships** | Partnership Bridge · Relationship Network · Partner Briefing Room | Consider a single suitable investor for each platform, understand human introductions, and coordinate a sensitive discussion. |
| **3. Second-Order Effects** | **Assess Value** | Carbon Intelligence · Research & Method | Compare the immediate and future effects of a refurbishment or rebuild, making assumptions and exclusions explicit. |

The **Explore** page also includes a preview of the fictional relationship network. Each detailed page has **one clear ← Three Areas** button and numbered navigation tabs for the pages within its area. The sidebar contains only sample-data export, import and reset controls; it does not duplicate page navigation.

### Visual design

The images in `docs/previews/` are **illustrative static previews** (some show earlier design iterations). The current hero layout reference is `docs/STATIC_DESIGN_PREVIEW.html`. These are not screenshots of a deployed Streamlit server.

KINETIC uses a dark pine/moss/sage palette throughout. Sample read-only tables are deliberately rendered as accessible, dark HTML tables rather than light default data grids. Editable items use explicit form controls, including a simple milestone-update form, rather than a spreadsheet-style editor. A responsive layout keeps the animated network separate from headline text. The Market Signals page presents each research observation in three distinct panels: **What Happened**, **Why It Matters**, and **Question To Explore**.

### Meaning and limitations

**Systems thinking** means considering how parts of an investment ecosystem interact, rather than studying each part in isolation. **Relationship networks** means the human connections that enable appropriate conversations. **Second-order effects** means consequences that arise after the first obvious result of a decision.

The **opportunity checklist** and **investor match** are invented illustrations, not verified judgments. The investor match uses sample sector/capital/structure preferences and a sample introduction score; all real investor appetite, available capital, returns, risk tolerance and conflicts remain **unknown**. These are prompts for genuine research and human conversation, not predictions or automated allocations.

See the [plain-language guide](docs/PLAIN_LANGUAGE_GUIDE.md), [interview demonstration](docs/INTERVIEW_DEMO.md), [v4 deployment fixes](docs/CHANGELOG_V4.md) and [detailed model assumptions](docs/METHOD_AND_DATA.md).

## Research alignment

Copley Point's publicly stated approach prioritises underlying UK real assets as downside protection; platform growth; selectively chosen institutional partners in joint-venture arrangements; scalability; and operating teams. The publicly described structures include **AssetCo/OpCo and GP/LP**. This concept therefore **does not** assume a multi-LP syndication model: the Partnership Bridge ranks candidate matches to support the selection of **one well-suited institutional co-investor per platform**.

Relevant public reference points: [Copley Point approach](https://copleypoint.com/our-approach/), [platform model](https://copleypoint.com/platforms/), [Block Industrial / Sixth Street joint venture](https://copleypoint.com/2024/11/13/sixth-street-and-copley-point-announce-joint-venture-for-uk-industrial-real-estate/), [Rendesco / Pioneer announcement, May 2026](https://copleypoint.com/2026/05/13/copley-point-exits-part-of-its-shareholding-in-rendesco-to-pioneer-point-partners/) and [The carbon case for upgrading existing industrial real estate](https://copleypoint.com/wp-content/uploads/2025/05/CPC-Research-The-carbon-case-for-upgrading-existing-industrial-real-estate.pdf).

The dated **Market Signals** dataset uses published sources and was prepared in November 2026. It is not a live data feed.

## Where the code lives

```text
kinetic/
├── app.py                       # Streamlit page and interactive workflows
├── core/
│   ├── scoring.py               # Independent, transparent heuristics
│   ├── carbon.py                # Carbon/cost model and payback
│   ├── briefs.py                # Redacted vs internal briefing export
│   ├── data.py                  # Data loading and validation
│   ├── styles.py                # Visual design system
│   └── ui.py                    # Escaped dark tables, content cards & animated vector network
├── data/
│   ├── opportunities.csv        # Entirely fictional deals
│   ├── partners.csv             # Entirely fictional capital partners
│   ├── contacts.csv             # Entirely fictional contact network
│   ├── milestones.csv           # Fictional JV collaboration preview
│   ├── activities.csv           # Entirely fictional log
│   └── signals.json             # Real, linked, dated PUBLIC research signals
├── docs/
│   ├── INTERVIEW_DEMO.md        # 2-minute demonstration script
│   ├── PLAIN_LANGUAGE_GUIDE.md  # Simple definitions and conversation examples
│   ├── METHOD_AND_DATA.md      # Scoring, sample schema and boundaries
│   ├── SOURCES.md              # Primary-source bibliography
│   └── SECURITY_AND_ROADMAP.md # How to evolve responsibly
├── tests/                       # Unit tests
├── .streamlit/config.toml       # Dark theme
├── requirements.txt
├── requirements-dev.txt
└── .github/workflows/tests.yml  # Automated test run on push
```

## Run tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

The app is designed to work without paid data feeds or external APIs. The 32 automated checks cover calculations, data contracts, redaction and simulated page execution. The scoring and carbon-calculation functions are independently testable. A static layout reference is provided in `docs/STATIC_DESIGN_PREVIEW.html`; a deployed Streamlit browser run remains the final UI verification step. See `docs/METHOD_AND_DATA.md` for the model specification and its limitations.

## Usage and attribution

Concept UI/implementation: original independent demonstration. Source companies retain their respective names and marks; this project does not use their logos, imply an official appointment, or claim access to their systems. Any business or investment decision requires independent due diligence and expert review.


## Final UI pass (v7)

- Visible navigation and methodology steps use **1., 2., 3.**, not leading-zero labels.
- The introduction credits **Tobias Leung**, with one prominent entry button.
- Expandable panels, selected options, focused fields and hover states use deliberately styled dark green backgrounds and high-contrast text. This addresses the white panel highlight in **Assess Value**.
- Added consistent focus states, clearer section-navigation buttons, card/table contrast and spacing across the three work areas.
- All sample deals, capital partners and investment scores remain fictional and illustrative.
