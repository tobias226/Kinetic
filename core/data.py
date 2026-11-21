"""Demo data loading and strict lightweight CSV import validation."""
from __future__ import annotations
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'
SCHEMAS = {
    'opportunities': ['id','name','sector','subsector','region','platform_model','asset_backed',
                      'post_technology_risk','management_quality','scalability','capital_need_gbp_m',
                      'capital_3y_gbp_m','estimated_asset_value_gbp_m','downside_strength','stage',
                      'owner','next_action','next_action_date','last_updated','description',
                      'thesis_tags','risks','notes'],
    'partners': ['id','name','kind','sectors','geography','capital_min_m','capital_max_m',
                 'hold_years','structural_flexibility','relationship_strength','warm_intro',
                 'introducer','mandate_note'],
    'contacts': ['id','partner_id','name','title','relationship_owner','relationship_strength',
                 'last_contact','mutual_connection','next_step'],
    'activities': ['id','entity_type','entity_id','activity_date','category','summary','next_step'],
    'milestones': ['id','opportunity_id','workstream','owner','audience','status','due','deliverable','notes'],
}
NUMERIC = {
    'opportunities': ['asset_backed','post_technology_risk','management_quality','scalability',
                      'capital_need_gbp_m','capital_3y_gbp_m','estimated_asset_value_gbp_m','downside_strength'],
    'partners': ['capital_min_m','capital_max_m','hold_years','structural_flexibility',
                 'relationship_strength','warm_intro'],
    'contacts': ['relationship_strength'], 'activities': [], 'milestones': []
}

def validate_df(kind: str, frame: pd.DataFrame) -> pd.DataFrame:
    if kind not in SCHEMAS:
        raise ValueError('Unknown dataset')
    cols = SCHEMAS[kind]
    missing = set(cols) - set(frame.columns)
    if missing:
        raise ValueError('Missing columns: ' + ', '.join(sorted(missing)))
    result = frame[cols].copy().fillna('')
    for col in NUMERIC[kind]:
        result[col] = pd.to_numeric(result[col], errors='raise')
        if not result[col].between(0, 10**9).all():
            raise ValueError(f'{col} must be non-negative')
    result['id'] = result['id'].astype(str)
    if result['id'].duplicated().any() or result['id'].eq('').any():
        raise ValueError('IDs must be non-empty and unique')
    return result


def seed(kind: str) -> pd.DataFrame:
    return validate_df(kind, pd.read_csv(DATA_DIR / (kind + '.csv'), keep_default_na=False))
