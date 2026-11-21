from math import inf
from pathlib import Path
import json
import pandas as pd
import pytest
from core.carbon import CarbonScenario, calculate
from core.data import seed, validate_df, SCHEMAS
from core.scoring import thesis_score, partner_fit, priority_score
from core.briefs import partner_brief


def test_seed_files_have_valid_schema_and_unique_ids():
    for kind, columns in SCHEMAS.items():
        frame = seed(kind)
        assert len(frame) > 0
        assert list(frame.columns) == columns
        assert frame['id'].is_unique


def test_scores_are_bounded_and_thesis_dimensions_sum_to_100():
    for _, op in seed('opportunities').iterrows():
        score, rows = thesis_score(op.to_dict())
        assert 0 <= score <= 100
        assert score == sum(r[1] for r in rows)
        assert sum(r[2] for r in rows) == 100
        assert 0 <= priority_score(op.to_dict()) <= 100


def test_bad_technology_risk_record_scores_lower():
    items = seed('opportunities').set_index('id')
    assert thesis_score(items.loc['O-107'].to_dict())[0] < thesis_score(items.loc['O-101'].to_dict())[0]


def test_partner_fit_rewards_sector_and_capacity():
    opportunities = seed('opportunities').set_index('id')
    partners = seed('partners').set_index('id')
    op = opportunities.loc['O-101'].to_dict()
    suitable = partner_fit(op, partners.loc['P-02'].to_dict())
    wrong = partner_fit(op, partners.loc['P-05'].to_dict())
    assert suitable['score'] > wrong['score']
    assert suitable['sector_ok'] is True and suitable['capacity_ok'] is True
    assert wrong['sector_ok'] is False


def test_partner_fit_weight_changes_score_and_stays_in_range():
    op=seed('opportunities').iloc[0].to_dict()
    partner=seed('partners').iloc[3].to_dict()
    no_access=partner_fit(op,partner,0)
    with_access=partner_fit(op,partner,.5)
    assert no_access['score']==no_access['investment']
    assert with_access['score']!=no_access['score']
    assert 0<=with_access['score']<=100


def test_carbon_default_and_payback():
    x=calculate(CarbonScenario())
    assert x['carbon_payback_years']==pytest.approx(67.5)
    assert x['lifetime_refurb_t']==8850
    assert x['lifetime_new_t']==14550
    assert x['avoided_t_if_refurb']>0


def test_carbon_scenario_equal_or_domination_cases():
    equal=calculate(CarbonScenario(embodied_new_kg_sqm=210,operational_new_kg_sqm_yr=19))
    assert equal['carbon_payback_years']==0
    not_reached=calculate(CarbonScenario(embodied_new_kg_sqm=750,operational_new_kg_sqm_yr=25))
    assert not_reached['carbon_payback_years']==inf
    with pytest.raises(ValueError):
        calculate(CarbonScenario(floor_area_sqm=-2))


def test_external_brief_redacts_internal_notes_and_person():
    op=seed('opportunities').iloc[0].to_dict()
    pt=seed('partners').iloc[0].to_dict()
    fit=partner_fit(op,pt)
    external=partner_brief(op,pt,fit,True)
    internal=partner_brief(op,pt,fit,False)
    assert op['notes'] not in external
    assert pt['introducer'] not in external
    assert 'INTERNAL ONLY' not in external
    assert pt['introducer'] in internal
    assert op['notes'] in internal


def test_csv_import_rejects_missing_columns_and_duplicate_ids():
    frame=seed('opportunities')
    with pytest.raises(ValueError,match='Missing columns'):
        validate_df('opportunities',frame.drop(columns=['sector']))
    duplicate=pd.concat([frame.iloc[[0]],frame.iloc[[0]]],ignore_index=True)
    with pytest.raises(ValueError,match='unique'):
        validate_df('opportunities',duplicate)


def test_signal_source_urls_and_facts_present():
    path=Path(__file__).resolve().parents[1]/'data'/'signals.json'
    signals=json.loads(path.read_text(encoding='utf-8'))
    assert len(signals)>=4
    for s in signals:
        assert s['url'].startswith('https://')
        assert s['fact'] and s['implication'] and s['question']
