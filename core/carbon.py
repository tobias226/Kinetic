"""Editable scenario arithmetic. Inputs are hypothetical, not Copley Point asset data."""
from __future__ import annotations
from dataclasses import dataclass
from math import inf


@dataclass(frozen=True)
class CarbonScenario:
    floor_area_sqm: float = 15000
    embodied_refurb_kg_sqm: float = 210
    embodied_new_kg_sqm: float = 750
    operational_refurb_kg_sqm_yr: float = 19
    operational_new_kg_sqm_yr: float = 11
    capex_refurb_gbp_sqm: float = 450
    capex_new_gbp_sqm: float = 1250
    operating_cost_refurb_gbp_sqm_yr: float = 20
    operating_cost_new_gbp_sqm_yr: float = 14
    years: int = 20


def calculate(s: CarbonScenario) -> dict:
    if s.floor_area_sqm <= 0 or s.years <= 0:
        raise ValueError("Floor area and holding period must be positive")
    values = [s.embodied_refurb_kg_sqm, s.embodied_new_kg_sqm, s.operational_refurb_kg_sqm_yr,
              s.operational_new_kg_sqm_yr, s.capex_refurb_gbp_sqm, s.capex_new_gbp_sqm,
              s.operating_cost_refurb_gbp_sqm_yr, s.operating_cost_new_gbp_sqm_yr]
    if min(values) < 0:
        raise ValueError("Inputs cannot be negative")
    re = s.floor_area_sqm * s.embodied_refurb_kg_sqm / 1000
    ne = s.floor_area_sqm * s.embodied_new_kg_sqm / 1000
    ro = s.floor_area_sqm * s.operational_refurb_kg_sqm_yr / 1000
    no = s.floor_area_sqm * s.operational_new_kg_sqm_yr / 1000
    yearly_savings_new = ro - no
    upfront_excess_new = ne - re
    if yearly_savings_new > 0 and upfront_excess_new >= 0:
        payback = upfront_excess_new / yearly_savings_new
    elif upfront_excess_new <= 0 and yearly_savings_new >= 0:
        payback = 0.0
    else:
        payback = inf  # one pathway may never overtake without detailed analysis
    refurb_cost = s.floor_area_sqm * (s.capex_refurb_gbp_sqm + s.years * s.operating_cost_refurb_gbp_sqm_yr)
    new_cost = s.floor_area_sqm * (s.capex_new_gbp_sqm + s.years * s.operating_cost_new_gbp_sqm_yr)
    return {
        "embodied_refurb_t": re, "embodied_new_t": ne,
        "annual_refurb_t": ro, "annual_new_t": no,
        "lifetime_refurb_t": re + s.years * ro,
        "lifetime_new_t": ne + s.years * no,
        "carbon_payback_years": payback,
        "capex_refurb_gbp": s.floor_area_sqm * s.capex_refurb_gbp_sqm,
        "capex_new_gbp": s.floor_area_sqm * s.capex_new_gbp_sqm,
        "undiscounted_cost_refurb_gbp": refurb_cost,
        "undiscounted_cost_new_gbp": new_cost,
        "avoided_t_if_refurb": (ne + s.years * no) - (re + s.years * ro),
        "avoided_gbp_if_refurb": new_cost - refurb_cost,
    }
