# KINETIC

### An independent concept for Copley Point Capital–relevant origination and partnership intelligence

> **Independent candidate prototype**. Not affiliated with, prepared for, commissioned by or endorsed by Copley Point Capital. **All opportunities, counterparties, contacts, introductions, capital figures and activity records are fictional.** Named existing Copley Point platforms and historical transactions are discussed only with publicly available citations.

A polished, human-led **Streamlit** app that connects the three elements of real-assets origination: **platform opportunity → right institutional investor → trusted human introduction**. Includes a separate scenario calculator that compares carbon and cash costs of industrial refurbishment and redevelopment.

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

**Data behaviour:** The app runs from bundled **synthetic CSV** samples. Edits, new leads, activity logging and CSV restores are stored in **the current browser session only**. Use **sidebar → Data portability → Export CSV** to save your work; import the file to restore it. Streamlit Community Cloud containers may restart at any time, and this demo has no durable database.

**Privacy:** This is a public demonstration, not an authenticated CRM or production partner portal. Do not put genuine confidential data, contacts, credentials, client notes or proprietary underwriting into it.

## Navigation

| Area | What you can actually do | Why it matters |
|---|---|---|
| Welcome | Enter the workspace or jump straight to the signature feature | Clear professional narrative and memorable first impression |
| Command Centre | Review stage funnel, ranked priorities, next actions and public Copley Point proof points | Workflow discipline and commercial prioritisation |
| Market Signals | Read dated primary-source industry developments and attach intelligence to a demo opportunity's activity log | Signals are converted into origination questions and action |
| Origination Radar | Filter nine demo platform opportunities; inspect explainable thesis scores; update status, action and notes; add a new lead | Investment judgement plus record management |
| Relationship Network | Explore fictional relationships/introductions; select capital archetypes and log calls, meetings or research | Genuine relationship-first approach |
| Partnership Bridge | Rank single-partner matches, vary relationship access weighting, inspect suitability and blockers, save a decision and export an internal brief | Shows how human access and institutional fit meet |
| Carbon Intelligence | Change floor area, upfront embodied carbon, annual operational carbon, capex, running costs and time horizon; compare cumulative emissions and simple costs | Original analytical lens linked to the firm's industrial real-estate research |
| Partner Briefing Room | Preview and download redacted/internal briefings; simulate selective milestone-sharing and update JV workflow status | Discretion and audience-appropriate communication |
| Research & Method | Review cited strategy facts and the limitations of the prototype | Evidence-aware, not performative, research |

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
│   └── styles.py                # Visual design system
├── data/
│   ├── opportunities.csv        # Entirely fictional deals
│   ├── partners.csv             # Entirely fictional capital partners
│   ├── contacts.csv             # Entirely fictional contact network
│   ├── milestones.csv           # Fictional JV collaboration preview
│   ├── activities.csv           # Entirely fictional log
│   └── signals.json             # Real, linked, dated PUBLIC research signals
├── docs/
│   ├── INTERVIEW_DEMO.md        # 2-minute demonstration script
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

The app is designed to work without paid data feeds or external APIs. The scoring and carbon-calculation functions are fully testable without the UI. See `docs/METHOD_AND_DATA.md` for the model specification and its limitations.

## Usage and attribution

Concept UI/implementation: original independent demonstration. Source companies retain their respective names and marks; this project does not use their logos, imply an official appointment, or claim access to their systems. Any business or investment decision requires independent due diligence and expert review.
