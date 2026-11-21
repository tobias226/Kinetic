"""Plain-text exports: deliberately keep private CRM metadata out of partner-facing briefs."""
from datetime import date
from html import escape


def partner_brief(op: dict, partner: dict, fit: dict, external: bool = True) -> str:
    lines = [
        'KINETIC   •   CONCEPT BRIEF',
        'Illustrative only — not prepared or endorsed by Copley Point Capital',
        f'Generated {date.today().isoformat()}', '',
        f'OPPORTUNITY  |  {op["name"]}',
        f'Theme: {op["sector"]} / {op["subsector"]}',
        f'Geography: {op["region"]}',
        f'Indicative capital need: £{float(op["capital_need_gbp_m"]):.0f}m (synthetic)',
        f'Proposed structure: {op["platform_model"]}', '',
        'INVESTMENT HYPOTHESIS', str(op['description']), '',
        'DISCUSSION POINTS',
        '- What asset backing and cash-flow security can be independently verified?',
        '- How strong is the founder/operator team and capacity to scale?',
        '- What is the optimal AssetCo/OpCo or equivalent funding structure?',
        '- Which downside protections and asset-level value-creation levers are credible?',
    ]
    if not external:
        lines.extend(['', 'INTERNAL ONLY — DO NOT FORWARD',
                      f'Demo partner: {partner["name"]}',
                      f'Heuristic fit: {fit["score"]}/100 (not a credit/investment opinion)',
                      f'Demo relationship entry: {partner["introducer"]}',
                      f'Risks to investigate: {op["risks"]}',
                      f'Internal notes: {op["notes"]}'])
    else:
        lines.extend(['', 'This is a redacted fictional discussion example. No investment proposal,',
                      'partner mandate, investment return or confidential information is asserted.'])
    return '\n'.join(lines)


def html_card(title: str, value: str, foot: str = '') -> str:
    return (f'<div class="glass-card"><div class="eyebrow">{escape(title)}</div>'
            f'<div class="card-value">{escape(value)}</div>'
            f'<div class="muted">{escape(foot)}</div></div>')
