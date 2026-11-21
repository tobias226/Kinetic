"""Transparent heuristic rubrics: decision support, not investment advice."""
from __future__ import annotations

THEME_SECTORS = {
    "Industrial & Logistics", "Clean Heat", "Energy Infrastructure", "Essential Infrastructure"
}


def clamp(value: float, lo: float = 0, hi: float = 100) -> float:
    return max(lo, min(hi, value))


def thesis_score(op: dict) -> tuple[int, list[tuple[str, int, int]]]:
    """Return a visible, fixed-weight screen grounded in published investment themes."""
    sector = op.get("sector", "")
    structure = op.get("platform_model", "")
    rows = [
        ("UK focus", 10 if op.get("region", "") in {"Midlands", "North West", "North East", "London & South East", "South West", "Scotland", "Wales", "Yorkshire", "East of England", "UK-wide"} else 0, 10),
        ("Sector alignment", 18 if sector in THEME_SECTORS else 4, 18),
        ("Asset-backed downside", 18 if int(op.get("asset_backed", 0)) else 0, 18),
        ("Beyond technology risk", 12 if int(op.get("post_technology_risk", 0)) else 0, 12),
        ("Scalability", round((int(op.get("scalability", 1))-1) / 4 * 12), 12),
        ("Management capability", round((int(op.get("management_quality", 1))-1) / 4 * 12), 12),
        ("Downside strength", round((int(op.get("downside_strength", 1))-1) / 4 * 12), 12),
        ("Platform capital model", 6 if structure in {"AssetCo / OpCo", "GP / LP", "Asset aggregation"} else 0, 6),
    ]
    return sum(item[1] for item in rows), rows


def partner_fit(op: dict, partner: dict, access_weight: float = .2) -> dict:
    """Score a SINGLE prospective platform partner, with investment fit and access separated."""
    sectors = [x.strip() for x in str(partner.get("sectors", "")).split("|")]
    sector_ok = op.get("sector") in sectors
    ticket = float(op.get("capital_need_gbp_m", 0))
    low, high = float(partner.get("capital_min_m", 0)), float(partner.get("capital_max_m", 0))
    capacity_ok = low <= ticket <= high
    if capacity_ok:
        ticket_pts = 30
    elif ticket > high and high > 0:
        ticket_pts = round(30 * max(0, 1 - ((ticket - high) / high)))
    elif ticket < low and low > 0:
        ticket_pts = round(30 * max(0, ticket / low))
    else:
        ticket_pts = 0
    geography_ok = str(partner.get("geography", "")).lower() in {"uk", "uk & europe", "pan-europe"}
    horizon_pts = 10 if float(partner.get("hold_years", 0)) >= 7 else 5
    flexibility_pts = round((float(partner.get("structural_flexibility", 1)) - 1) / 4 * 15)
    investment = int(clamp((35 if sector_ok else 0) + ticket_pts + (10 if geography_ok else 0) + horizon_pts + flexibility_pts))
    strength = int(partner.get("relationship_strength", 1))
    access = int(clamp(15 * strength + (25 if bool(partner.get("warm_intro", False)) else 0)))
    weight = clamp(float(access_weight), 0, 1) if access_weight <= 1 else clamp(float(access_weight)) / 100
    combined = round((1 - weight) * investment + weight * access)
    rationale = []
    rationale.append("Thematic mandate overlaps" if sector_ok else "Sector mandate is not an obvious fit")
    rationale.append("Illustrative ticket within indicated range" if capacity_ok else "Capital requirement outside the indicated ticket range")
    rationale.append("Relationship pathway identified in demo records" if bool(partner.get("warm_intro", False)) else "No warm introduction captured")
    rationale.append("Flexible structures" if float(partner.get("structural_flexibility", 1)) >= 4 else "Structuring flexibility needs discussion")
    return {
        "score": combined,
        "investment": investment,
        "access": access,
        "sector_ok": sector_ok,
        "capacity_ok": capacity_ok,
        "rationale": rationale,
    }


def priority_score(op: dict) -> int:
    screen, _ = thesis_score(op)
    stage = op.get("stage", "")
    stage_bump = {"New lead": 0, "Research": 3, "Warm introduction": 8, "Engaged": 12, "Under review": 15, "Paused": -25}.get(stage, 0)
    return int(clamp(screen * .85 + stage_bump))
