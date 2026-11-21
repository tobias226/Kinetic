"""KINETIC — human-led UK real-assets origination intelligence demo.

Streamlit Community Cloud entrypoint: app.py
Entire dataset is synthetic; selected public company facts are separately sourced.
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import date, datetime
from html import escape
from uuid import uuid4

import networkx as nx
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from core.briefs import partner_brief, html_card
from core.carbon import CarbonScenario, calculate
from core.data import seed, validate_df, SCHEMAS
from core.scoring import thesis_score, partner_fit, priority_score, THEME_SECTORS
from core.styles import CSS
from core.ui import dark_table, section_step, note_card

st.set_page_config(page_title='KINETIC | Origination Intelligence', page_icon='🧭', layout='wide', initial_sidebar_state='collapsed')
st.html(CSS)  # Inject CSS into the app DOM (not a Markdown body)

AREAS = {
    'Find Opportunities': ['Command Centre', 'Market Signals', 'Origination Radar'],
    'Build Partnerships': ['Partnership Bridge', 'Relationship Network', 'Partner Briefing Room'],
    'Assess Value': ['Carbon Intelligence', 'Research & Method'],
}
AREA_LANDING = {'Find Opportunities': 'Command Centre', 'Build Partnerships': 'Partnership Bridge', 'Assess Value': 'Carbon Intelligence'}
PAGES = ['Welcome', 'Explore'] + [page for pages in AREAS.values() for page in pages]
STAGES = ['New lead', 'Research', 'Warm introduction', 'Engaged', 'Under review', 'Paused']
PUBLIC_LINKS = {
    'Approach': 'https://copleypoint.com/our-approach/',
    'Platforms': 'https://copleypoint.com/platforms/',
    'About Copley Point': 'https://copleypoint.com/about-us/',
    'Sixth Street JV': 'https://copleypoint.com/2024/11/13/sixth-street-and-copley-point-announce-joint-venture-for-uk-industrial-real-estate/',
    'Rendesco & Pioneer': 'https://copleypoint.com/2026/05/13/copley-point-exits-part-of-its-shareholding-in-rendesco-to-pioneer-point-partners/',
    'Carbon research': 'https://copleypoint.com/wp-content/uploads/2025/05/CPC-Research-The-carbon-case-for-upgrading-existing-industrial-real-estate.pdf',
    'UK Industrial Strategy': 'https://www.gov.uk/government/collections/the-uks-modern-industrial-strategy-2025',
}


def init():
    for kind in SCHEMAS:
        if kind not in st.session_state:
            st.session_state[kind] = seed(kind)
    if 'page' not in st.session_state:
        st.session_state.page = 'Welcome'


def navigate(page: str):
    st.session_state.page = page
    st.rerun()


def df(kind: str) -> pd.DataFrame:
    return st.session_state[kind]


def record(kind: str, entity_id: str) -> dict:
    rows = df(kind).loc[df(kind)['id'] == entity_id]
    if rows.empty:
        raise ValueError(f'{entity_id} not found')
    return rows.iloc[0].to_dict()


def add_activity(entity_type: str, entity_id: str, category: str, summary: str, next_step: str):
    row = {
        'id': 'A-' + uuid4().hex[:8].upper(), 'entity_type': entity_type,
        'entity_id': entity_id, 'activity_date': date.today().isoformat(),
        'category': category, 'summary': summary, 'next_step': next_step,
    }
    st.session_state.activities = pd.concat([df('activities'), pd.DataFrame([row])], ignore_index=True)


def intro(kicker: str, title: str, description: str):
    st.markdown(f'<div class="main-intro"><div class="portal-eyebrow">{escape(kicker)}</div><div class="page-title">{escape(title)}</div><div class="page-desc">{escape(description)}</div></div>', unsafe_allow_html=True)


def panel(title: str, value: str, foot: str = ''):
    st.markdown(html_card(title, value, foot), unsafe_allow_html=True)


def mk_chart(fig, height: int = 320):
    fig.update_layout(
        height=height, margin=dict(l=12,r=18,t=48,b=28),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='DM Sans, sans-serif', color='#c9d9ec', size=12),
        legend=dict(orientation='h', y=1.10, x=0, xanchor='left', font=dict(size=11)),
        hoverlabel=dict(bgcolor='#16293a', bordercolor='#4175b4', font=dict(color='#e9eef5')),
        showlegend=fig.layout.showlegend if fig.layout.showlegend is not None else True,
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})



def current_area(page: str) -> str:
    for area, pages in AREAS.items():
        if page in pages:
            return area
    return 'Find Opportunities'



def section_navigation():
    """Simple top-level wayfinding; only one back action in work areas."""
    area = current_area(st.session_state.page)
    pages = AREAS[area]
    back, subtitle = st.columns([1.2, 4.8], gap='large', vertical_alignment='center')
    with back:
        if st.button('← Three Areas', key='back_areas', use_container_width=True):
            navigate('Explore')
    with subtitle:
        st.markdown(f'<div class="nav-area-name">{escape(area.upper())} <span>/ SELECT A PAGE BELOW</span></div>', unsafe_allow_html=True)
    steps=st.columns(len(pages), gap='small')
    for index,(col,page) in enumerate(zip(steps,pages),start=1):
        with col:
            active=page==st.session_state.page
            label=f'{index}.  {page}'
            if st.button(label, key='top_nav_'+page, use_container_width=True, disabled=active):
                navigate(page)
    st.markdown('<div class="navigation-divider"></div>',unsafe_allow_html=True)


def sidebar():
    """Optional data controls; primary navigation remains at the top of each page."""
    with st.sidebar:
        st.markdown('<div class="portal-wordmark">KINETIC<span>.</span></div><div class="concept-tag">DEMO SETTINGS &amp; DATA</div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<span class="ribbon ribbon-demo">FICTIONAL DEMO DATA</span>', unsafe_allow_html=True)
        st.caption('Independent candidate prototype. Not an official Copley Point product.')
        st.caption('For page navigation, use the numbered tabs at the top of the workspace.')
        with st.expander('Check Display Settings', expanded=False):
            active_bg = str(st.get_option('theme.secondaryBackgroundColor') or '')
            if active_bg.lower() == '#142e4c':
                st.success('KINETIC navy-blue theme is loaded.')
            else:
                st.warning('The deployment may be missing .streamlit/config.toml. ' 
                           'Confirm that the hidden .streamlit folder was uploaded to GitHub.')
            st.caption('Expected widget background: #142E4C. Active setting: ' + (active_bg or 'not set'))
        with st.expander('Export or restore demo data', expanded=False):
            dataset = st.selectbox('Dataset', list(SCHEMAS), key='export_dataset')
            st.download_button('Export CSV', data=df(dataset).to_csv(index=False).encode('utf-8'), file_name=f'{dataset}_demo.csv', mime='text/csv', use_container_width=True)
            uploaded = st.file_uploader('Restore a CSV', type=['csv'], key='csv_restore')
            if uploaded is not None and st.button('Validate & restore', use_container_width=True):
                try:
                    imported = validate_df(dataset, pd.read_csv(uploaded, keep_default_na=False))
                    st.session_state[dataset] = imported
                    st.success(f'Restored {len(imported)} fictional records')
                except (ValueError, KeyError, pd.errors.ParserError) as exc:
                    st.error(f'Could not restore: {exc}')
        with st.expander('Reset all sample data'):
            if st.button('Reset sample data', use_container_width=True):
                for kind in SCHEMAS:
                    st.session_state[kind] = seed(kind)
                st.rerun()


def welcome():
    """A deliberately concise, human-first welcome page.

    The animated artwork remains in a local SVG rendered by Streamlit's
    native image component, which has proved more reliable when deployed.
    """
    st.markdown('<div class="kinetic-brand">KINETIC<span>.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="kinetic-brand-subtitle">HUMAN-CENTRIC · TECHNOLOGY-ASSISTED · REAL ASSETS INTELLIGENCE</div>', unsafe_allow_html=True)
    st.write('')
    copy, graphic = st.columns([0.94, 1.06], gap='large', vertical_alignment='center')
    with copy:
        st.markdown('<div class="portal-eyebrow">SYSTEMS THINKING. HUMAN CONNECTION.</div>', unsafe_allow_html=True)
        st.markdown('<h1 class="welcome-headline">Connecting Ideas.<br>Connecting People.<br><em>Creating Value.</em></h1>', unsafe_allow_html=True)
        st.markdown('<p class="welcome-introduction">A clearer view of UK real assets — bringing opportunities, people and capital together. Technology supports the analysis; human judgement leads the decisions.</p>', unsafe_allow_html=True)
    with graphic:
        st.image(Path(__file__).resolve().parent / 'assets' / 'kinetic-network.svg', use_container_width=True)
    st.write('')
    st.markdown('<div class="cta-kicker">DISCOVER THE THREE PERSPECTIVES</div>', unsafe_allow_html=True)
    _, middle, _ = st.columns([1.05, 1.10, 1.05])
    with middle:
        if st.button('Explore KINETIC  →', key='enter_kinetic', type='primary', use_container_width=True):
            navigate('Explore')
    st.markdown('<div class="creator-credit"><span>CREATED BY</span><strong>Tobias Leung</strong></div>', unsafe_allow_html=True)


def explore():
    st.markdown('<div class="kinetic-brand compact">KINETIC<span>.</span></div>', unsafe_allow_html=True)
    if st.button('← Introduction', key='explore_back'):
        navigate('Welcome')
    intro('THREE CONNECTED PERSPECTIVES', 'See the Whole Picture', 'Follow an opportunity from first insight to the right partnership and the value it can create.')
    cards = [
        ('1. SYSTEMS THINKING', 'Find Opportunities',
         'Spot patterns across markets, assets and operators, then identify the next conversation worth having.',
         'Discover Opportunities  →','pine'),
        ('2. RELATIONSHIP NETWORKS', 'Build Partnerships',
         'Connect investment needs with suitable capital and trusted relationships — without losing human judgement.',
         'Explore Partnerships  →','moss'),
        ('3. SECOND-ORDER EFFECTS', 'Assess Value',
         'Understand how decisions today can change costs, carbon and outcomes tomorrow.',
         'Explore Long-Term Value  →','sage'),
    ]
    cols=st.columns(3,gap='large')
    for col,(idea,area,description,cta,tone) in zip(cols,cards):
        with col:
            st.markdown(f'<div class="area-card {tone}"><div class="area-number">{escape(idea)}</div>'
                        f'<h3>{escape(area)}</h3><p>{escape(description)}</p>'
                        '<div class="area-bottom-mark">↗</div></div>',unsafe_allow_html=True)
            if st.button(cta,key='area_'+area,use_container_width=True):
                navigate(AREA_LANDING[area])
    st.markdown('<div class="section-divider-large"></div>',unsafe_allow_html=True)
    st.markdown('<div class="feature-heading"><div><span class="portal-eyebrow">A CONNECTED APPROACH</span>'
                '<h3>The right connections change what’s possible.</h3>'
                '<p>Explore how ideas, investors and people might connect. All relationships below are fictional examples.</p>'
                '</div><span class="feature-pill">INTERACTIVE DEMO</span></div>',unsafe_allow_html=True)
    plot_network(df('partners'),df('contacts'),height=390,compact=True)
    left,mid,right=st.columns([1,1.2,1])
    with mid:
        if st.button('Explore Relationship Pathways  →',key='open_network_preview',use_container_width=True):
            navigate('Relationship Network')
    st.caption('Illustrative network only. No real contacts, investor mandates or proprietary systems are connected.')


def command_centre():
    intro('1. FIND OPPORTUNITIES', 'Opportunity Overview', 'A simple overview of the fictional opportunities we are tracking, and what we might do next.')
    o=df('opportunities').copy()
    p=df('partners')
    o['screen']=o.apply(lambda r: thesis_score(r.to_dict())[0], axis=1)
    o['priority']=o.apply(lambda r: priority_score(r.to_dict()), axis=1)
    a,b,c,d=st.columns(4,gap='medium')
    with a: st.metric('Sample opportunities',len(o),help='Fictional investment opportunities used to demonstrate the workflow.')
    with b: st.metric('Meet our initial criteria',int((o.screen>=75).sum()),help='Sample opportunities scoring at least 75/100 against an illustrative screening checklist. Not real Copley Point criteria.')
    with c: st.metric('Sample investor profiles',len(p),help='Fictional investor profiles, with different investment sectors and cheque sizes. These are not real mandates.')
    with d:
        today=date.today()
        soon=today+pd.Timedelta(days=7)
        due=pd.to_datetime(o.next_action_date).dt.date
        st.metric('Follow-ups in next 7 days',int(((due>=today)&(due<=soon)).sum()),help='Upcoming follow-up tasks from the fictional records.')
    with st.expander('What do these numbers mean?'):
        st.write('**Initial criteria score:** our example checklist of location, asset backing, sector, management and growth potential. **Investor profile:** a fictional example of what an institution might look for. Neither is verified live information or an investment prediction.')
    st.write('')
    left,right=st.columns([1,1],gap='large')
    with left:
        st.subheader('Where Are Opportunities In The Process?')
        st.caption('Each stage represents a step from first research to a more serious review.')
        stages=o.stage.value_counts().reindex(STAGES,fill_value=0)
        fig=go.Figure(go.Bar(x=stages.values,y=stages.index,orientation='h',marker_color='#84a8d3',text=stages.values,textposition='outside',cliponaxis=False))
        fig.update_layout(yaxis=dict(autorange='reversed',automargin=True),xaxis=dict(showgrid=False,dtick=1,range=[0,max(2,int(stages.max())+1)]),showlegend=False)
        mk_chart(fig,315)
    with right:
        st.subheader('Which Investment Sectors Feature?')
        st.caption('Number of fictional opportunities in each sector; no chart key is needed.')
        counts=o.sector.value_counts().sort_values()
        fig=go.Figure(go.Bar(x=counts.values,y=counts.index,orientation='h',marker_color=['#33648f','#3d77a9','#5687c2','#84a8d3','#b1c8e4'][:len(counts)],text=counts.values,textposition='outside',cliponaxis=False))
        fig.update_layout(yaxis=dict(automargin=True),xaxis=dict(showgrid=False,dtick=1,range=[0,max(2,int(counts.max())+1)]),showlegend=False)
        mk_chart(fig,315)
    st.write('')
    st.subheader('Suggested Next Actions')
    st.caption('A demonstration of how to organise follow-up work. The ordering is a simple sample rule, not a deal-quality or return forecast.')
    view=o.sort_values(['priority','screen'],ascending=False).head(5)[['name','stage','next_action','next_action_date']]
    headers=['Opportunity','Current stage','Next step','Target date']
    rows=[]
    for _,r in view.iterrows():
        cells=''.join(f'<td>{escape(str(value))}</td>' for value in [r['name'].replace('Demo | ',''),r['stage'],r['next_action'],r['next_action_date']])
        rows.append('<tr>'+cells+'</tr>')
    table='<div class="kinetic-table-scroll"><table class="kinetic-table"><thead><tr>'+''.join('<th>'+v+'</th>' for v in headers)+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'
    st.markdown(table,unsafe_allow_html=True)
    with st.expander('How are suggested actions ordered?'):
        st.write('The prototype combines an **illustrative screening score** with a small adjustment for how far a conversation has progressed. The weights are chosen for demonstration, not drawn from any internal Copley Point process. A person should decide which opportunity deserves attention, using evidence and urgency.')
    st.write('')
    section_step(3, 'Why This Reflects Copley Point', 'Three public aspects of the firm’s investment approach informed the prototype.')
    ca,cb,cc=st.columns(3,gap='large')
    with ca: note_card('FOCUSED PARTNERSHIPS','The firm describes a selective approach to identifying suitable institutional capital for each platform.','pine')
    with cb: note_card('ASSETS + OPERATIONS','Underlying property or infrastructure assets may provide protection while operators work to grow the platform.','moss')
    with cc: note_card('RENDESCO / PIONEER','The May 2026 transaction provides a public example of how a platform partnership can develop.','sage')
    st.caption('Public sources: Copley Point [approach](https://copleypoint.com/our-approach/), [platforms](https://copleypoint.com/platforms/) and [Rendesco announcement](https://copleypoint.com/2026/05/13/copley-point-exits-part-of-its-shareholding-in-rendesco-to-pioneer-point-partners/).')



def market_signals():
    intro('1. FIND OPPORTUNITIES','Market Signals',
          'A simple research workflow: what changed, why might it matter, and what should we ask next?')
    note_card('HOW TO USE THIS PAGE', 'Choose a sector, read a verified public development, then turn it into a useful question before deciding whether to log it against a sample opportunity.', 'pine', compact=True)
    signals=json.loads((Path(__file__).resolve().parent/'data'/'signals.json').read_text(encoding='utf-8'))
    themes=['All Sectors'] + sorted(set(x['sector'] for x in signals))
    choice=st.selectbox('Show Market Signals For',themes)
    items=[x for x in signals if choice=='All Sectors' or x['sector']==choice]
    st.markdown(f'<p class="content-label">{len(items)} RESEARCH NOTES · PUBLIC SOURCES · DATED SNAPSHOT</p>',unsafe_allow_html=True)
    for i,item in enumerate(items,start=1):
        url=escape(str(item['url']),quote=True)
        html=(
            f'<article class="signal-card"><div class="signal-top">'
            f'<span class="signal-number">{i}.</span>'
            f'<span class="signal-sector">{escape(item["sector"])}</span>'
            f'<span class="signal-date">{escape(item["date"])}</span></div>'
            f'<h3>{escape(item["title"])}</h3>'
            '<div class="signal-grid">'
            f'<div class="signal-pane fact"><h4>What Happened</h4><p>{escape(item["fact"])}</p></div>'
            f'<div class="signal-pane meaning"><h4>Why It Matters</h4><p>{escape(item["implication"])}</p></div>'
            f'<div class="signal-pane question"><h4>Question To Explore</h4><p>{escape(item["question"])}</p></div>'
            '</div><div class="signal-source">PUBLICATION / '
            f'<a href="{url}" target="_blank" rel="noopener noreferrer">{escape(item["source"])} ↗</a></div></article>'
        )
        st.markdown(html,unsafe_allow_html=True)
        with st.expander('Add This Signal To A Sample Opportunity',expanded=False):
            opts=df('opportunities')
            chosen=st.selectbox('Sample Opportunity',opts['name'].tolist(),key='signal_'+item['id'])
            if st.button('Save Research Question',key='attach_'+item['id']):
                oid=opts.loc[opts['name']==chosen,'id'].iloc[0]
                add_activity('Opportunity',oid,'Market signal',f'{item["title"]} | source: {item["url"]}',item['question'])
                st.success('Saved to the fictional activity history for this session.')
    st.caption('This is a November 2026 research snapshot, not live market intelligence. Always recheck the linked source before relying on the information.')


def origination_radar():
    intro('1. FIND OPPORTUNITIES','Explore opportunities','Compare fictional opportunities using a starting checklist: location, sector, assets, leadership and potential to grow.')
    note_card('WHAT THE SCORE MEANS','A higher number only means that the fictional record meets more of our example screening criteria. It does not predict returns or replace due diligence.','pine')
    section_step(1, 'Browse The Opportunity Shortlist', 'Filter the fictional opportunities by sector, stage and our illustrative checklist.')
    x = df('opportunities').copy()
    a,b,c=st.columns([1.1,1.1,1])
    with a: sector_filter=st.multiselect('Sector', sorted(x.sector.unique()), default=sorted(x.sector.unique()))
    with b: stage_filter=st.multiselect('Stage', STAGES, default=STAGES)
    with c: min_score=st.slider('Minimum initial checklist score',0,100,0,5)
    x['Checklist score /100'] = x.apply(lambda r: thesis_score(r.to_dict())[0],axis=1)
    x=x[x.sector.isin(sector_filter)&x.stage.isin(stage_filter)&(x['Checklist score /100']>=min_score)].sort_values('Checklist score /100',ascending=False)
    if x.empty:
        st.info('No sample opportunities match those filters.')
        return
    dark_table(x[['name','sector','region','capital_need_gbp_m','stage','Checklist score /100']].rename(columns={'name':'Opportunity','sector':'Sector','region':'Region','capital_need_gbp_m':'Capital Need (£m)','stage':'Stage','Checklist score /100':'Initial Checklist /100'}),highlight_columns=['Initial Checklist /100'])
    lookup = dict(zip(x['name'],x['id']))
    section_step(2, 'Look More Closely At An Opportunity', 'Explore why a sample opportunity scores as it does, then record an appropriate next step.')
    selected=st.selectbox('Choose An Opportunity',x['name'].tolist())
    op=record('opportunities',lookup[selected])
    score,parts=thesis_score(op)
    main,detail=st.columns([1.3,1],gap='large')
    with main:
        st.markdown(f'<div class="eyebrow">INVESTMENT IDEA / {escape(op["id"])}</div><div class="score">{score}<span style="font-size:1rem;color:#7ca2d0"> / 100</span></div>',unsafe_allow_html=True)
        st.write(op['description'])
        st.markdown('**What contributes to the score?**')
        st.caption('Each bar shows points awarded for a checklist item. The weights are illustrative and not taken from an internal investment policy.')
        fig=go.Figure(go.Bar(x=[r[1] for r in parts],y=[r[0] for r in parts],orientation='h',marker_color='#7aa0cf',text=[f'{r[1]}/{r[2]}' for r in parts],textposition='outside',cliponaxis=False))
        fig.update_layout(yaxis=dict(autorange='reversed'),xaxis=dict(range=[0,23],showgrid=False),showlegend=False)
        mk_chart(fig,360)
    with detail:
        panel('Hypothetical capital requirement',f'£{float(op["capital_need_gbp_m"]):,.0f}m',f'Potential 3-year deployment £{float(op["capital_3y_gbp_m"]):,.0f}m')
        panel('Example investment structure',op['platform_model'],f'{op["region"]} · {op["subsector"]}')
        with st.expander('What do these investment structures mean?'):
            st.write('**AssetCo / OpCo:** the property or infrastructure assets are held separately from the company running the business. **GP / LP:** a manager oversees a partnership with investors. **Asset aggregation:** several assets are brought together into one platform. They are different possible structures, not claims about a particular deal.')
        st.markdown('**Key Risk To Investigate**')
        st.warning(op['risks'],icon='⚠️')
        with st.form('op_change'):
            stage=st.selectbox('Pipeline stage',STAGES,index=STAGES.index(op['stage']))
            action=st.text_input('Next human action',value=str(op['next_action']))
            note=st.text_area('Internal note (demo only)',value=str(op['notes']),height=90)
            if st.form_submit_button('Save changes',type='primary'):
                for k,v in {'stage':stage,'next_action':action,'notes':note,'last_updated':date.today().isoformat()}.items():
                    st.session_state.opportunities.loc[st.session_state.opportunities['id']==op['id'],k] = v
                add_activity('Opportunity',op['id'],'Update',f'Stage updated to {stage}',action)
                st.success('Updated in this session. Use sidebar CSV export to preserve changes.')
    with st.expander('Add A New Fictional Opportunity'):
        with st.form('new_opportunity',clear_on_submit=True):
            name=st.text_input('Opportunity name',placeholder='Demo | New Platform')
            c1,c2,c3=st.columns(3)
            with c1:
                sector=st.selectbox('Theme',sorted(THEME_SECTORS)+['Digital Infrastructure'])
                region=st.selectbox('UK geography',['Midlands','North West','North East','London & South East','South West','Scotland','Wales','Yorkshire','East of England','UK-wide'])
            with c2:
                structure=st.selectbox('Platform model',['AssetCo / OpCo','GP / LP','Asset aggregation','Direct asset acquisition'])
                ticket=st.number_input('Capital needed (£m)',min_value=1.0,value=50.0,step=5.0)
            with c3:
                asset=st.checkbox('Underlying asset backing',value=True)
                post=st.checkbox('Post technology risk',value=True)
            description=st.text_area('Why might this be interesting?')
            risk=st.text_input('Principal challenge / diligence item')
            submitted=st.form_submit_button('Add opportunity')
            if submitted:
                if not name.strip() or not description.strip():
                    st.error('Provide a name and investment hypothesis.')
                else:
                    new={'id':'O-'+uuid4().hex[:8].upper(),'name':name.strip(),'sector':sector,'subsector':'To be classified','region':region,'platform_model':structure,'asset_backed':int(asset),'post_technology_risk':int(post),'management_quality':3,'scalability':3,'capital_need_gbp_m':ticket,'capital_3y_gbp_m':ticket,'estimated_asset_value_gbp_m':ticket,'downside_strength':3,'stage':'New lead','owner':'Origination team','next_action':'Validate management and asset thesis','next_action_date':date.today().isoformat(),'last_updated':date.today().isoformat(),'description':description,'thesis_tags':'','risks':risk,'notes':'Entered in demo session'}
                    st.session_state.opportunities=pd.concat([df('opportunities'),pd.DataFrame([new])],ignore_index=True)
                    add_activity('Opportunity',new['id'],'New lead','Created illustrative record','Validate investment thesis')
                    st.success('Illustrative opportunity added to this session.')


def plot_network(partners: pd.DataFrame, contacts: pd.DataFrame, *, height: int = 540, compact: bool = False):
    graph=nx.Graph()
    graph.add_node('KINETIC',type='Hub')
    for _,p in partners.iterrows():
        graph.add_node(str(p['id']),type='Partner',label=str(p['name']).replace('Demo | ',''))
        graph.add_edge('KINETIC',str(p['id']))
    for _,c in contacts.iterrows():
        graph.add_node(str(c['id']),type='Contact',label=str(c['name']))
        if str(c['partner_id']) in graph:
            graph.add_edge(str(c['partner_id']),str(c['id']))
    pos=nx.spring_layout(graph,seed=15,k=1.25,iterations=100)
    fig=go.Figure()
    for a,b in graph.edges():
        fig.add_trace(go.Scatter(x=[pos[a][0],pos[b][0]],y=[pos[a][1],pos[b][1]],mode='lines',line=dict(color='#365672',width=1.5),hoverinfo='skip',showlegend=False))
    colors={'Hub':'#ccdcef','Partner':'#6b96ca','Contact':'#799cd0'}
    for node_type in ['Hub','Partner','Contact']:
        nodes=[n for n,d in graph.nodes(data=True) if d['type']==node_type]
        fig.add_trace(go.Scatter(x=[pos[n][0] for n in nodes],y=[pos[n][1] for n in nodes],text=[graph.nodes[n].get('label',n) for n in nodes],mode='markers' if node_type=='Contact' else 'markers+text',textposition='top center',textfont=dict(size=10,color='#c1d3e8'),marker=dict(color=colors[node_type],size=23 if node_type=='Hub' else 14 if node_type=='Partner' else 9,line=dict(width=1,color='#091118')),hovertemplate='%{text}<extra></extra>',name={'Hub':'KINETIC','Partner':'Investor','Contact':'Person'}[node_type]))
    fig.update_layout(xaxis=dict(visible=False),yaxis=dict(visible=False),showlegend=not compact,hovermode='closest',
                      margin=dict(l=5,r=5,t=22,b=15))
    mk_chart(fig,height)


def relationship_network():
    intro('2. BUILD PARTNERSHIPS','Relationship Pathways','See how fictional investors, people and introduction routes could connect. Each connection would need real-world verification.')
    p=df('partners'); c=df('contacts')
    left,right=st.columns([1.35,.95],gap='large')
    with left:
        section_step(1,'Explore The Relationship Map','Green circles are fictional investor organisations; gold circles are individual contacts. Hover to explore.')
        plot_network(p,c)
        st.caption('Green nodes represent sample investors; smaller gold nodes are fictional individual contacts. Hover over a node for the name. Nothing here represents a real introduction.')
    with right:
        section_step(2,'Understand One Investor','Review a sample capital range and a possible first conversation.')
        selected=st.selectbox('Sample investor profile',p['name'].tolist())
        pt=p.loc[p['name']==selected].iloc[0].to_dict()
        ct=c.loc[c['partner_id']==pt['id']]
        panel('Capital range (indicative, invented)',f'£{pt["capital_min_m"]:,.0f}m–£{pt["capital_max_m"]:,.0f}m','Synthetic partner mandate')
        st.markdown('**Potential Human Connection**')
        if not ct.empty:
            contact=ct.iloc[0]
            st.write(f'**{contact["name"]}** · {contact["title"]}')
            st.caption(str(contact['mutual_connection']))
            st.write('Next step: '+str(contact['next_step']))
        else:
            st.info('No contact captured — research before outreach.')
        st.write('**Relationship Strength (Illustrative)**')
        st.progress(int(float(pt['relationship_strength']))*20, text=f'{int(pt["relationship_strength"])}/5 demo relationship strength')
        with st.form('log_touch'):
            kind=st.selectbox('Activity',['Call','Meeting','Introduction','Email','Research','Note'])
            summary=st.text_area('Conversation note / intelligence captured',placeholder='What did we learn about their investment priorities?')
            next_step=st.text_input('Thoughtful follow-up',value='Request a meeting to clarify capital appetite')
            if st.form_submit_button('Log interaction',type='primary'):
                if not summary.strip():
                    st.error('Add a short note before logging.')
                else:
                    add_activity('Partner',pt['id'],kind,summary,next_step)
                    st.success('Interaction saved in the current session.')
    section_step(3,'Recent Conversations & Follow-Ups','A chronological log of demo meetings and next steps.')
    log=df('activities').sort_values('activity_date',ascending=False).head(10)
    dark_table(log[['activity_date','entity_type','entity_id','category','summary','next_step']].rename(columns={'activity_date':'Date','entity_type':'Type','entity_id':'ID','category':'Activity','summary':'What We Learnt','next_step':'Next Step'}))


def partnership_bridge():
    intro('2. BUILD PARTNERSHIPS', 'Partnership Bridge', 'Explore one opportunity, compare potential investors, verify the important questions and decide on a next conversation.')
    st.caption('All example investors, mandates, connections and scores are invented. Matching means a promising question, not an approved investment.')
    opportunities=df('opportunities')
    section_step(1, 'Choose An Opportunity', 'Start with one fictional platform and the kind of capital it might need.')
    selected=st.selectbox('Sample Opportunity', opportunities['name'].tolist())
    weight=20
    with st.expander('Optional: how much should an existing introduction matter?', expanded=False):
        st.write('A match has two parts: **business fit** (does the investor appear interested in this kind of opportunity?) and **ease of introduction** (do we have a trusted route to speak with them?). The default gives business fit 80% of the illustrative score and ease of introduction 20%. A warm contact is useful but should never outweigh a poor investment fit.')
        weight=st.slider('Importance of an existing contact (%)',0,50,20,5,help='At 20%, the overall example score uses 80% business fit and 20% ease of introduction. This is only a demonstration setting.')
    op=opportunities.loc[opportunities['name']==selected].iloc[0].to_dict()
    matches=[]
    for _,row in df('partners').iterrows():
        person=row.to_dict()
        fit=partner_fit(op,person,weight/100)
        matches.append({
            'id':person['id'],
            'Sample investor':person['name'].replace('Demo | ',''),
            'Overall example /100':fit['score'],
            'Business fit /100':fit['investment'],
            'Introduction /100':fit['access'],
            'Sector match':'Yes' if fit['sector_ok'] else 'Check',
            'Capital size match':'Yes' if fit['capacity_ok'] else 'Check',
        })
    ranks=pd.DataFrame(matches).sort_values(['Overall example /100','Business fit /100'],ascending=False)
    a,b,c=st.columns(3,gap='large')
    with a: panel('Sector being considered',op['sector'],op['platform_model'])
    with b: panel('Capital needed (example)',f'£{float(op["capital_need_gbp_m"]):,.0f}m','Fictional capital requirement')
    with c: panel('Highest initial match',ranks.iloc[0]['Sample investor'],f'{int(ranks.iloc[0]["Overall example /100"])} / 100 · unverified')
    st.write('')
    section_step(2, 'Compare Potential Partners', 'This illustrative shortlist is a starting point for conversation, not a recommendation or a confirmed investor mandate.')
    st.caption('The scores reflect example inputs only. A high number does not mean an investor has available capital, a suitable risk appetite or an interest in this specific opportunity.')
    dark_table(ranks.drop(columns=['id']).rename(columns={'Sample investor':'Potential Investor','Overall example /100':'Initial Match /100','Business fit /100':'Business Fit /100','Introduction /100':'Ease Of Contact /100','Sector match':'Sector Fits?','Capital size match':'Funding Size Fits?'}),highlight_columns=['Initial Match /100'])
    with st.expander('What factors shape the initial score?'):
        st.markdown('**Business fit (80% by default):** sector 35 points, approximate funding amount 30, UK geography 10, time horizon 10 and willingness to consider different investment structures 15. **Introduction (20% by default):** fictional relationship strength and whether a warm introduction is recorded. These point allocations are design choices for this demonstration, **not** Copley Point criteria or real investor preferences.')
    section_step(3, 'Understand One Potential Partner', 'See the assumptions behind the comparison and where further investigation is needed.')
    partner_id=st.selectbox('Potential Investor',ranks['id'].tolist(),format_func=lambda pid: record('partners',pid)['name'].replace('Demo | ',''))
    partner=record('partners',partner_id)
    f=partner_fit(op,partner,weight/100)
    left,right=st.columns([1.05, .95],gap='large')
    with left:
        st.markdown(f'<div class="eyebrow">ILLUSTRATIVE MATCH · NOT VERIFIED</div><div class="score">{f["score"]} <span style="font-size:1rem;color:#8fafd7">/ 100</span></div>',unsafe_allow_html=True)
        st.progress(f['investment'],text=f'Business fit · {f["investment"]}/100')
        st.progress(f['access'],text=f'Ease of introduction · {f["access"]}/100')
        st.write('**What This Example Suggests**')
        for item in f['rationale']:
            st.markdown(f'<div class="evidence-line">{escape(item)}</div>',unsafe_allow_html=True)
    with right:
        st.markdown('**Potential Introduction — Fictional**')
        st.markdown(f'<div class="topic-card"><div class="tag">EXAMPLE CONTACT ROUTE</div><div class="title">{escape(str(partner["introducer"]))}</div><p>Would require research and confirmation before use.</p></div>',unsafe_allow_html=True)
        st.write('**Illustrative preferences**')
        st.write(partner['mandate_note'])
    st.write('')
    section_step(4, 'Verify The Important Questions', 'A good numerical match can still be commercially unsuitable; these are deliberately not assigned invented scores.')
    st.caption('These factors are deliberately **not** given invented points. An apparently strong match could fail any one of these checks.')
    questions=[
        ('Current appetite & available capital','Is this investor actively allocating to this type of opportunity, and is there money available now?'),
        ('Investment returns & downside risk','Do expected returns, cash-flow risks and safeguards suit their requirements?'),
        ('Track record & operating team','Does the platform leadership have the expertise and credibility to deliver the business plan?'),
        ('Governance & decision-making','Who approves investments, how quickly can they decide, and what control rights would they want?'),
        ('Sustainability & asset quality','Would environmental performance, upgrading costs and asset risks fit the investor’s expectations?'),
        ('Conflicts, reputation & exclusivity','Are there other commitments, conflicts or relationship sensitivities that could make a partnership unsuitable?'),
    ]
    checks=''.join(
        f'<div class="check-card"><h4>{escape(name)}</h4><p>{escape(question)}</p></div>'
        for name, question in questions
    )
    st.markdown('<div class="check-grid">'+checks+'</div>',unsafe_allow_html=True)
    with st.expander('Why Aren’t These Factors In The Score?'):
        st.write('They require verified, often confidential information. KINETIC deliberately does not invent investor demand, risk appetite, governance preferences or available capital. The checks are there to prompt a careful conversation.')
    section_step(5, 'Decide The Next Human Action', 'Use the comparison to prepare a more informed conversation, not automate a decision.')
    with st.form('bridge_decision'):
        decision=st.selectbox('Your proposed next step',['Research further','Ask for a warm introduction','Hold / not a fit'])
        reason=st.text_area('Why? What needs checking?',placeholder='Example: Confirm whether the investor has UK industrial capacity and who would make the decision.')
        if st.form_submit_button('Save your reasoning',type='primary'):
            if not reason.strip():
                st.error('Add one short reason so the next action is clear.')
            else:
                add_activity('Opportunity',op['id'],'Investor review',f'{decision} — {partner["name"]}: {reason}','Confirm facts with appropriate people')
                st.success('Reasoning saved in this demo session.')
    st.write('')
    st.download_button('Download a private discussion note  ↓',data=partner_brief(op,partner,f,external=False),file_name=f'{op["id"]}_internal_brief.txt',mime='text/plain',use_container_width=True)
    st.caption('This feature compares alternative individual partners. It does not syndicate an opportunity to several investors or imply access to real investor information.')


def carbon_intelligence():
    intro('3. ASSESS VALUE','Carbon & Cost Comparison','Explore a longer-term question: is refurbishing an industrial building better than rebuilding it once you consider upfront costs, running costs and carbon emissions?')
    st.caption('Looking beyond the immediate decision means examining what happens later: lower upfront cost today can lead to higher running costs or emissions over time. This is a simplified demonstration, not an investment decision.')
    st.info('All numbers are editable examples, not actual asset figures or results from Copley Point research. No live market or energy data is connected.')
    section_step(1,'Set The Scenario','Compare refurbishment and a new building using fictional, editable assumptions.')
    with st.expander('Adjust Building & Carbon Assumptions',expanded=True):
        a,b,c=st.columns(3)
        with a:
            area=st.number_input('Industrial floor area (m²)',min_value=1000.0,max_value=1_000_000.0,value=15000.0,step=1000.0)
            years=st.slider('Evaluation horizon (years)',5,40,20)
            em_r=st.number_input('Carbon from refurbishment work (kgCO₂e/m²)',0.0,2000.0,210.0,10.0)
        with b:
            em_n=st.number_input('Carbon from new construction (kgCO₂e/m²)',0.0,3000.0,750.0,10.0)
            op_r=st.number_input('Annual emissions after refurbishment (kgCO₂e/m²)',0.0,200.0,19.0,1.0)
            op_n=st.number_input('Annual emissions after rebuilding (kgCO₂e/m²)',0.0,200.0,11.0,1.0)
        with c:
            cap_r=st.number_input('Refurbishment cost upfront (£/m²)',0.0,10000.0,450.0,25.0)
            cap_n=st.number_input('Rebuilding cost upfront (£/m²)',0.0,20000.0,1250.0,25.0)
            st.caption('These example upfront costs exclude land, borrowing, taxes and selling costs.')
    with st.expander('Optional: Compare Annual Running Costs'):
        a,b=st.columns(2)
        with a: run_r=st.number_input('Refurbished annual operating costs (£/m²/yr)',0.0,1000.0,20.0,1.0)
        with b: run_n=st.number_input('New-build annual operating costs (£/m²/yr)',0.0,1000.0,14.0,1.0)
    with st.expander('How To Read The Carbon Figures'):
        st.write('**kgCO₂e/m²** means kilograms of greenhouse-gas emissions (expressed as carbon-dioxide equivalent) per square metre. **Upfront emissions** arise from construction work; **annual emissions** happen as the building is used. **tCO₂e** means tonnes, or 1,000 kilograms. The model combines upfront emissions with an assumed constant amount each year.')
    scenario=CarbonScenario(area,em_r,em_n,op_r,op_n,cap_r,cap_n,run_r,run_n,years)
    results=calculate(scenario)
    a,b,c=st.columns(3)
    with a: st.metric('Refurbishment: total emissions',f'{results["lifetime_refurb_t"]:,.0f} tCO₂e',help='Embodied plus operational emissions over chosen horizon')
    with b: st.metric('Rebuild: total emissions',f'{results["lifetime_new_t"]:,.0f} tCO₂e')
    with c:
        p=results['carbon_payback_years']
        st.metric('Years to offset extra build carbon',f'{p:.1f} yrs' if p!=float('inf') else 'Not reached',help='Years for lower annual new-build emissions to offset its higher upfront embodied carbon, where applicable')
    section_step(2,'Compare Emissions Over Time','This chart includes the emissions from construction and the assumed emissions from using the building.')
    time=pd.DataFrame({'Year':list(range(years+1))})
    time['Refurbish (tCO₂e)']=results['embodied_refurb_t']+time['Year']*results['annual_refurb_t']
    time['Rebuild (tCO₂e)']=results['embodied_new_t']+time['Year']*results['annual_new_t']
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=time.Year,y=time['Refurbish (tCO₂e)'],mode='lines',name='Refurbish',line=dict(color='#b1c8e4',width=3)))
    fig.add_trace(go.Scatter(x=time.Year,y=time['Rebuild (tCO₂e)'],mode='lines',name='Rebuild',line=dict(color='#83a7dd',width=3)))
    fig.update_layout(xaxis_title='Years',yaxis_title='Cumulative tCO₂e',hovermode='x unified')
    mk_chart(fig,380)
    section_step(3,'Consider The Longer-Term Trade-Off','The simplest answer is not always the best one: consider both initial investment and the consequences over time.')
    left,right=st.columns(2)
    with left:
        delta=results['avoided_t_if_refurb']
        panel('Carbon difference over the period',f'{abs(delta):,.0f} tCO₂e '+('avoided by refurbishment' if delta>=0 else 'avoided by new build'),'Illustrative undiscounted carbon accounting; excludes end-of-life, lease dynamics and offsets.')
    with right:
        delta_gbp=results['avoided_gbp_if_refurb']
        panel('Simple cost comparison',f'£{abs(delta_gbp)/1e6:,.2f}m '+('less for refurbishment' if delta_gbp>=0 else 'less for new build'),'Upfront capex + constant annual operating cost only. Not an asset valuation or NPV.')
    csv=time.to_csv(index=False).encode('utf-8')
    st.download_button('Download scenario time series (CSV)',data=csv,file_name='carbon_scenario_illustrative.csv',mime='text/csv')
    note_card('SECOND-ORDER EFFECTS','A rebuild may use less energy each year but require substantial upfront capital and construction emissions. Refurbishment can be less disruptive, yet may have higher running costs. The tool helps us ask better questions; it cannot determine the best investment.','sage')
    st.caption(f'Copley Point source: [The carbon case for upgrading existing industrial real estate]({PUBLIC_LINKS["Carbon research"]}). See the app methodology for exclusions.')


def partner_room():
    intro('2. BUILD PARTNERSHIPS','Partner Briefing Room','Draft a discussion note, control what can be shared and organise fictional partnership milestones.')
    section_step(1,'Choose The Opportunity & Audience','Pick a sample deal and investor, then select an internal or external view.')
    options=df('opportunities')['name'].tolist()
    chosen=st.selectbox('Hypothetical opportunity', options)
    op=df('opportunities').loc[df('opportunities')['name']==chosen].iloc[0].to_dict()
    partner_choices=df('partners')['name'].tolist()
    chosen_partner=st.selectbox('Illustrative target counterparty',partner_choices)
    pt=df('partners').loc[df('partners')['name']==chosen_partner].iloc[0].to_dict()
    fit=partner_fit(op,pt,.2)
    audience=st.radio('Briefing audience',['External / redacted','Internal / working draft'],horizontal=True)
    external=audience.startswith('External')
    content=partner_brief(op,pt,fit,external=external)
    section_step(2, 'Preview The Briefing', 'External view omits internal notes and relationship information. Nothing is actually shared.')
    st.markdown('<div class="brief-preview"><pre>'+escape(content)+'</pre></div>',unsafe_allow_html=True)
    st.download_button('Download this briefing  ↓',content,file_name=f'kinetic_{op["id"]}_{"external" if external else "internal"}.txt',mime='text/plain',type='primary')
    section_step(3,'Coordinate The Partnership','Review fictional action owners, deadlines and approval status. This is a local demonstration, not an investor portal.')
    st.caption('An idea for future co-management: joint milestones, ownership and selective visibility. No third party can access or modify this board.')
    milestone_frame=df('milestones')
    sub=milestone_frame.loc[milestone_frame['opportunity_id']==op['id']].copy()
    if sub.empty:
        st.info('No illustrative milestones created for this opportunity.')
    elif external:
        public=sub.loc[sub['audience']=='Partner-shareable']
        if public.empty:
            st.info('No partner-shareable milestones have been approved for this concept example.')
        else:
            dark_table(public[['workstream','owner','status','due','deliverable']].rename(columns={'workstream':'Workstream','owner':'Owner','status':'Status','due':'Target Date','deliverable':'Shareable Deliverable'}))
        st.caption('External preview excludes all internal-only milestone rows and confidential notes. This is a local illustration, not a live investor workspace.')

    else:
        dark_table(sub[['workstream','owner','status','due','audience']].rename(
            columns={'workstream':'Workstream','owner':'Owner','status':'Status','due':'Target Date','audience':'Visibility'}))
        with st.expander('Update A Fictional Milestone'):
            choices=dict(zip(sub['workstream']+' — '+sub['id'],sub['id']))
            selection=st.selectbox('Milestone To Update',list(choices))
            mid=choices[selection]
            existing=sub.loc[sub['id']==mid].iloc[0]
            with st.form('milestone_form'):
                new_status=st.selectbox('New Status',['Not started','In progress','Complete'],
                   index=['Not started','In progress','Complete'].index(existing['status']))
                new_due=st.date_input('Target Date',value=pd.to_datetime(existing['due']).date())
                if st.form_submit_button('Save Milestone Change',type='primary'):
                    key=st.session_state.milestones['id']==mid
                    st.session_state.milestones.loc[key,'status']=new_status
                    st.session_state.milestones.loc[key,'due']=new_due.isoformat()
                    st.success('Milestone updated in this session. Use the sidebar to export sample data.')
    st.markdown('<div class="eyebrow">NO AUTOMATIC SHARING / NO INVESTOR LOG-IN</div>',unsafe_allow_html=True)
    st.write('A genuine partner portal would require permissioned identity, separately scoped workspaces, secure document storage, audit logs, explicit approvals and an agreed data-room policy. This prototype deliberately does **not** expose any public upload link, email partner or imply access to firm systems.')
    st.caption('In external mode the brief intentionally excludes internal risk notes, contact names, relationship history, scores and strategic judgement.')


def methodology():
    intro('3. ASSESS VALUE','Research & How It Works','A plain-language guide to the evidence, the sample scores and the limits of the app.')
    st.subheader('What Is KINETIC Designed To Do?')
    st.write('KINETIC is a demonstration of three everyday questions: **Which opportunities are worth learning about? Which investors could be appropriate partners? What happens to costs and emissions over time?** It helps organise information and conversations. It does not replace commercial judgement or due diligence.')
    st.write('')
    with st.expander('1. What is grounded in public Copley Point information?', expanded=True):
        st.write('Copley Point describes an investment approach centred on UK real assets, scalable platforms, underlying asset security and selective capital partnerships. Published examples include the Block Industrial–Sixth Street joint venture and the Rendesco/Pioneer transaction. The firm has also published a paper examining the carbon implications of upgrading industrial buildings.')
        st.markdown(f'**Primary sources:** [Investment approach]({PUBLIC_LINKS["Approach"]}) · [Platform model]({PUBLIC_LINKS["Platforms"]}) · [Sixth Street transaction]({PUBLIC_LINKS["Sixth Street JV"]}) · [Rendesco announcement]({PUBLIC_LINKS["Rendesco & Pioneer"]}) · [Carbon research]({PUBLIC_LINKS["Carbon research"]}).')
        st.caption('These sources explain the themes informing the prototype; they do not provide the fictional investor preferences or scoring weights.')
    with st.expander('2. What has been invented for this demonstration?'):
        st.write('Every sample investment opportunity, investor profile, contact, conversation, capital requirement and follow-up task has been created for demonstration. The market-research section contains dated public links, but it is **not a live data feed**. The app does not connect to any Copley Point system or third-party CRM.')
    with st.expander('3. How does the opportunity checklist work?'):
        st.write('An opportunity receives points for eight example characteristics: UK location, sector, underlying assets, maturity of the technology, potential to grow, strength of management, protection against losses and broad funding structure. The total is out of 100. Point weights are deliberately simple, subjective choices made for this prototype; **Copley Point has not confirmed or supplied them**.')
        st.write('A high score does not mean the asset is worth buying or that the team is capable. Any claim needs evidence, including site-level information, finances and interviews.')
    with st.expander('4. How does the investor comparison work?'):
        st.write('The first part considers whether the example investment sector, funding amount, geography, expected investment period and structure match the fictional investor. The second part considers whether there might be an existing relationship or introduction. By default, business fit contributes 80% and access 20%; this can be adjusted in the investor screen to explore sensitivity.')
        st.write('Crucially, **available capital, investor appetite, returns, risk tolerance, investment committee process, conflicts, track record, governance and sustainability requirements are not verified**. They appear as questions a person should ask, not facts assumed by the score.')
        st.write('This is a comparison of **alternative individual partners**, not an instruction to assemble a syndicate.')
    with st.expander('5. What Are Second-Order Effects?'):
        st.write('**Second-order effects** are the indirect consequences of a decision. **Systems thinking** considers how people, assets, capital and the wider market influence each other. Both encourage a broader perspective rather than focusing only on the immediately visible cost. For example, rebuilding a warehouse might lower energy use, but constructing it releases carbon and requires substantial money up front. Refurbishment may save both today while leaving higher annual energy needs. The carbon page lets you change assumptions and compare the two over a chosen period.')
        st.write('Its simple total-cost calculation does not include future rents, asset values, taxes, funding, discount rates, disruption or all lifecycle emissions. **It is not a financial model or a reason to approve a project**.')
    with st.expander('6. How would a real version differ?'):
        st.write('It would need verified information, staff ownership, permissions, an approved CRM connection, clear records of evidence and decisions, confidential storage and compliance checks. It should also be checked by investment professionals before any screening scores influence real choices.')
    st.write('')
    st.caption('Built independently for interview discussion. Not commissioned or endorsed by Copley Point. Public sources are linked above; the fictional examples and scoring rules are supplied for demonstration only.')


init()
if st.session_state.page == 'Welcome':
    welcome()
elif st.session_state.page == 'Explore':
    explore()
else:
    sidebar()
    section_navigation()
    page_map={
        'Command Centre':command_centre,
        'Market Signals':market_signals,
        'Origination Radar':origination_radar,
        'Relationship Network':relationship_network,
        'Partnership Bridge':partnership_bridge,
        'Carbon Intelligence':carbon_intelligence,
        'Partner Briefing Room':partner_room,
        'Research & Method':methodology,
    }
    page_map.get(st.session_state.page,command_centre)()
