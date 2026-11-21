# Methodology, data design and model limitations

## 1. Thesis-screen score (0–100)

The screening rubric is a **transparent and user-independent heuristic** based on Copley Point's *publicly stated themes*, not confidential firm underwriting criteria or a predicted investment return.

| Dimension | Max points | Logic |
|---|---:|---|
| UK geography | 10 | Listed UK region; otherwise zero |
| Sector alignment | 18 | Industrial/logistics, clean heat, energy infrastructure or essential infrastructure get full score |
| Asset-backed protection | 18 | Binary yes/no demonstration field |
| Post technology-risk | 12 | Binary yes/no demonstration field |
| Scalability | 12 | Linear transformation of a 1–5 analyst input |
| Management quality | 12 | Linear transformation of a 1–5 analyst input |
| Downside strength | 12 | Linear transformation of a 1–5 analyst input |
| Platform funding model | 6 | AssetCo/OpCo, GP/LP or aggregation structure |
| **Total** | **100** | Observable in Origination Radar |

**Important:** Each score is only as good as its underlying evidence. Assessment inputs are invented, subjective and uncalibrated. A high score is a prompt for further diligence, not a decision or recommendation. Direct asset acquisitions may be relevant to Copley Point, so a non-platform structure's lower structural score is a *choice of this demo model*, not a claim that the firm would reject it.

## 2. Partnership Bridge score

The app compares **a single partner to a single platform opportunity**. The investment fit (0–100) combines:

- Overlap of investment sector: 35 points.
- Indicative cheque size within fictional ticket range: up to 30 points; lower for mismatch.
- UK geographic mandate: 10 points.
- Horizon/long-term capital: 10 or 5 points.
- Structuring flexibility: up to 15 points.

A separate relationship-access score uses an illustrative relationship-strength assessment and whether the demo record contains a warm introduction. The combined priority is:

`Combined = (1 − access_weight) × investment_fit + access_weight × relationship_access`

Default `access_weight = 0.20`, adjustable from 0 to 0.50 on-screen. The score does not capture hard conflicts, mandates, covenants, fund restrictions, negotiation leverage, certainty of capital, valuation, financing or allocation. Any one can be decisive.

Unlike a syndicate-matching tool, this reflects the firm's public description of commonly working with **one third-party institutional investor per platform**. The table presents **alternatives**; it does not allocate one opportunity across all of them.

## 3. Priority score

`Priority = clamp(0.85 × thesis_screen + pipeline_stage_adjustment, 0, 100)`

Pipeline-stage adjustments: new lead 0, research +3, warm introduction +8, engaged +12, under review +15, paused −25. This is a *task triage* view, not a probability-of-closing estimate. Due-date prioritisation remains with the user.

## 4. Carbon scenario arithmetic

Definitions: `A` = gross floor area in m², `E` = upfront embodied kgCO₂e/m², `O` = annual operational kgCO₂e/m², `T` = years, `C0` = capex £/m², `Cy` = annual operating cash £/m².

`Cumulative carbon (tonnes) = A × (E + T × O) / 1,000`

`Undiscounted cash cost (£) = A × (C0 + T × Cy)`

Where new-build embodied emissions exceed refurbishment but its yearly operational emissions are lower:

`Carbon payback years = (E_new − E_refurb) / (O_refurb − O_new)`

The general calculator returns an infinite/“not reached” payback when a straightforward improvement is not established. **Payback is for carbon only** and is not a financial payback, investment hurdle or NPV.

All example intensities and costs are editable **illustrative assumptions**, not claimed reference values from the Copley Point paper. The simplified model excludes discount rates, rent, operating income, asset value, residual value, financing, taxes, land, construction disruption, embodied lifecycle beyond one upfront event, end-of-life impacts, replacement cycles, electricity-grid decarbonisation, consumption patterns, demand changes, capital-market conditions, carbon pricing, uncertainties and rebound effects. It cannot justify a real refurbishment or demolition decision.

Reference inspiration: Copley Point's published research *The carbon case for upgrading existing industrial real estate* (September 2024); see SOURCES.md.

## 5. Data contracts

All CSVs are loaded from `data/`. The `id` column identifies records uniquely. The app validates required columns and rejects duplicate/blank IDs and invalid numeric types. Other text fields use illustrative, editable data. CRM changes are maintained only within the active Streamlit session.

### Opportunities

- Identity/thesis: `id`, `name`, `sector`, `subsector`, `region`, `platform_model`, `description`, `thesis_tags`, `risks`.
- Screen: `asset_backed` and `post_technology_risk` as 0/1; `management_quality`, `scalability`, `downside_strength` as ratings 1–5.
- Capital: `capital_need_gbp_m`, `capital_3y_gbp_m`, `estimated_asset_value_gbp_m`: illustrative £m.
- Workflow: `stage`, `owner`, `next_action`, `next_action_date`, `last_updated`, `notes`.

### Partners

- Identity: `id`, `name`, `kind`, `sectors` (pipe-separated), `geography`, `mandate_note`.
- Capital fit: `capital_min_m`, `capital_max_m`, `hold_years`, `structural_flexibility`.
- Relationship hypothesis: `relationship_strength`, `warm_intro`, `introducer`.

### Contacts, activities and JV milestones

- Contacts: fictional name, title, partner ID, relationship owner, strength, last contact and introducer context.
- Activities: type, relevant ID, activity date, category, what was learned and next human action.
- Milestones: illustrative deal ID, workstream, owner, audience, status, due date, deliverable and private notes. Only items tagged `Partner-shareable` are visible in the external preview.
- One `signals.json` file contains dated and source-linked public research facts plus the concept author's interpretation.

## 6. Evidence taxonomy

**Tier A — documented public fact:** source URL, identifiable speaker/publisher, date, correctly scoped unit/claim.

**Tier B — interpretative hypothesis:** plausible but explicitly presented as a question or hypothesis.

**Tier C — synthetic demo record:** not an actual company, mandate, relationship, investment, target or transaction.

A real version should record source evidence, last verified timestamp, analyst ownership, confidence, updates and conflicts and should distinguish clearly between verifiable observations and subjective judgements.
