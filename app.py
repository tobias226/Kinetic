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

st.set_page_config(page_title='KINETIC | Origination Intelligence', page_icon='🧭', layout='wide', initial_sidebar_state='collapsed')
st.markdown(CSS, unsafe_allow_html=True)

PAGES = ['Welcome', 'Command Centre', 'Market Signals', 'Origination Radar', 'Relationship Network', 'Partnership Bridge', 'Carbon Intelligence', 'Partner Briefing Room', 'Research & Method']
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
    # On the welcome screen this widget is not rendered, so it can be safely preselected.
    if page != 'Welcome':
        st.session_state.nav_page = page
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
        height=height, margin=dict(l=0,r=8,t=15,b=12),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='DM Sans, sans-serif', color='#d2e3d9', size=12),
        legend=dict(orientation='h',y=1.13,x=0),
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})


def status_table(frame: pd.DataFrame, columns: list[str]):
    st.dataframe(frame[columns], use_container_width=True, hide_index=True)


def sidebar():
    with st.sidebar:
        st.markdown('<div class="portal-wordmark">KINETIC</div><div class="concept-tag">ORIGINATION &amp; PARTNERSHIP INTELLIGENCE</div>', unsafe_allow_html=True)
        st.markdown('---')
        chosen = st.radio('NAVIGATE', options=PAGES[1:], key='nav_page')
        if chosen != st.session_state.page:
            st.session_state.page = chosen
            st.rerun()
        st.markdown('---')
        st.markdown('<span class="ribbon ribbon-demo">SYNTHETIC DATA / DEMO</span>', unsafe_allow_html=True)
        st.caption('Independent candidate concept. Not affiliated with, commissioned by or endorsed by Copley Point Capital.')
        if st.button('← Return to introduction', use_container_width=True):
            navigate('Welcome')
        with st.expander('Data portability', expanded=False):
            dataset = st.selectbox('Dataset', list(SCHEMAS), key='export_dataset')
            st.download_button('Export CSV', data=df(dataset).to_csv(index=False).encode('utf-8'), file_name=f'{dataset}_demo.csv', mime='text/csv', use_container_width=True)
            uploaded = st.file_uploader('Restore a CSV', type=['csv'], key='csv_restore')
            if uploaded is not None and st.button('Validate & restore', use_container_width=True):
                try:
                    imported = validate_df(dataset, pd.read_csv(uploaded, keep_default_na=False))
                    st.session_state[dataset] = imported
                    st.success(f'Restored {len(imported)} records')
                except (ValueError, KeyError, pd.errors.ParserError) as exc:
                    st.error(f'Could not restore: {exc}')
        if st.button('Reset all demo data', use_container_width=True):
            for kind in SCHEMAS:
                st.session_state[kind] = seed(kind)
            st.rerun()


def welcome():
    st.markdown('<div class="portal-wordmark" style="margin-top:1.1rem">KINETIC</div><div class="concept-tag">ORIGINATION &amp; PARTNERSHIP INTELLIGENCE</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="portal-hero">
      <div class="hero-grid">
        <div class="hero-copy">
          <div class="portal-eyebrow">AN INDEPENDENT CONCEPT FOR UK REAL ASSETS, PARTNERSHIPS &amp; ENERGY TRANSITION</div>
          <div class="hero-title">Turn relationship intelligence into <em>kinetic</em> opportunity.</div>
          <div class="subhead">Source the right platform. Understand its strategic fit. Identify the most credible institutional partner. Convert market intelligence into disciplined commercial momentum.</div>
          <div class="hero-footer">
            <span>FOCUS<strong>UK REAL ASSETS</strong></span>
            <span>MODEL<strong>HUMAN-LED ORIGINATION</strong></span>
            <span>DESIGN<strong>ONE PARTNER / PLATFORM</strong></span>
            <span>LENS<strong>CARBON &amp; CAPITAL</strong></span>
          </div>
        </div>
        <div class="hero-visual">
          <div class="grid-lines"></div>
          <div class="map-sheen"></div>
          <div class="orbit o1"><div class="orbit-dot"></div></div>
          <div class="orbit o2"><div class="orbit-dot"></div></div>
          <div class="flow f1"></div><div class="flow f2"></div><div class="flow f3"></div><div class="flow f4"></div><div class="flow f5"></div>
          <div class="node n1"></div><div class="node-label l1">Leeds</div>
          <div class="node n2"></div><div class="node-label l2">Midlands</div>
          <div class="node n3"></div><div class="node-label l3">Bristol</div>
          <div class="node n4"></div><div class="node-label l4">London</div>
          <div class="node n5"></div>
          <div class="energy-card c1"><strong>Origination Radar</strong><span>Asset-backed platforms, mapped and prioritised.</span></div>
          <div class="energy-card c2"><strong>Partnership Bridge</strong><span>Institutional fit matched with relationship access.</span></div>
          <div class="energy-card c3"><strong>Carbon Intelligence</strong><span>Operational efficiency with an embodied-carbon lens.</span></div>
          <div class="turbine">
            <div class="baseglow"></div>
            <div class="mast"></div>
            <div class="rotor">
              <div class="blade b1"></div>
              <div class="blade b2"></div>
              <div class="blade b3"></div>
            </div>
            <div class="hub"></div>
          </div>
          <div class="visual-tag">KINETIC ENERGY • NETWORKED OPPORTUNITY • RESPONSIBLE GROWTH</div>
        </div>
      </div>
    </div>
    ''', unsafe_allow_html=True)
    st.write('')
    c1, c2, c3 = st.columns([1.15, 1.05, 1])
    with c1:
        if st.button('Enter the intelligence workspace  →', type='primary', use_container_width=True):
            navigate('Command Centre')
    with c2:
        if st.button('Explore the standout feature  ↗', use_container_width=True):
            navigate('Partnership Bridge')
    with c3:
        if st.button('Understand the research  ↗', use_container_width=True):
            navigate('Research & Method')
    st.write('')
    ca, cb, cc = st.columns(3)
    with ca:
        st.markdown('<div class="topic-card"><div class="tag">01 / SOURCE</div><div class="title">Origination before transaction</div><p>Identify asset-backed platforms and founder-led teams that could scale with long-term capital.</p></div>', unsafe_allow_html=True)
    with cb:
        st.markdown('<div class="topic-card"><div class="tag">02 / CONNECT</div><div class="title">Partnership intelligence</div><p>Prioritise complementary mandates, introduction pathways and the next human action.</p></div>', unsafe_allow_html=True)
    with cc:
        st.markdown('<div class="topic-card"><div class="tag">03 / CREATE VALUE</div><div class="title">The second-order lens</div><p>Test asset-level carbon and capital trade-offs with transparent, editable assumptions.</p></div>', unsafe_allow_html=True)
    st.caption('Prototype by a prospective candidate • November 2026 • All pipeline records, parties and relationship histories are fictional.')

def command_centre():
    intro('01 / THE DESK', 'Command centre', 'A concise overview of the opportunity funnel, relationship priorities and thesis conviction. Every pipeline record below is fictional.')
    o = df('opportunities').copy()
    p = df('partners').copy()
    o['screen'] = o.apply(lambda r: thesis_score(r.to_dict())[0], axis=1)
    o['priority'] = o.apply(lambda r: priority_score(r.to_dict()), axis=1)
    a,b,c,d = st.columns(4)
    with a: st.metric('Illustrative opportunities', str(len(o)))
    with b: st.metric('Above 75 thesis fit', str((o.screen >= 75).sum()))
    with c: st.metric('Partner archetypes', str(len(p)))
    with d: st.metric('Next actions due in 7 days', str(((pd.to_datetime(o.next_action_date).dt.date >= date.today()) & (pd.to_datetime(o.next_action_date).dt.date <= date.today() + pd.Timedelta(days=7))).sum()))
    st.write('')
    left,right=st.columns([1.12,.88],gap='large')
    with left:
        st.subheader('Origination funnel')
        stages = o.stage.value_counts().reindex(STAGES, fill_value=0)
        fig=go.Figure(go.Bar(x=stages.values, y=stages.index, orientation='h', marker=dict(color=['#b5e0c5','#8ec9ab','#6eb596','#4f9d84','#3c806e','#657b74']),text=stages.values,textposition='outside',cliponaxis=False))
        fig.update_layout(yaxis=dict(autorange='reversed'),xaxis=dict(showgrid=False,dtick=1),showlegend=False)
        mk_chart(fig,280)
    with right:
        st.subheader('Theme distribution')
        counts=o.sector.value_counts().reset_index()
        counts.columns=['Sector','Records']
        fig=px.pie(counts, names='Sector', values='Records', hole=.71, color_discrete_sequence=['#b5e0c5','#6d9e88','#487a6b','#cfbd93','#9baea3'])
        fig.update_traces(textinfo='percent',textfont_size=11,marker_line_color='#142326',marker_line_width=3)
        mk_chart(fig,280)
    st.subheader('Priority actions')
    view=o.sort_values(['priority','screen'],ascending=False).head(5)[['name','sector','stage','priority','next_action','next_action_date']].rename(columns={'name':'Opportunity','sector':'Theme','stage':'Stage','priority':'Priority /100','next_action':'Next action','next_action_date':'Due'})
    st.dataframe(view,use_container_width=True,hide_index=True)
    with st.expander('How this score works'):
        st.write('Priority = 85% of thesis-screen score plus a stage-based workflow adjustment. It does **not** forecast returns, investment quality or probability of execution. Relationships and judgement determine the next action.')
    st.write('')
    st.markdown('<div class="section-line"><div class="eyebrow">PUBLIC PROOF POINTS / RESEARCH INTO THE FIRM</div></div>',unsafe_allow_html=True)
    ca,cb,cc=st.columns(3)
    with ca: panel('Investment model','ONE FITTED INSTITUTIONAL PARTNER','The firm commonly pursues one investor alongside each platform, with a significant Copley Point stake.')
    with cb: panel('Platform architecture','ASSETCO + OPCO','Real-asset downside protection paired with management and operational value creation.')
    with cc: panel('Known transaction','Rendesco / Pioneer · 2026','Copley Point sold half its Rendesco holding; Pioneer became the majority shareholder.')
    st.caption('Sources: Copley Point [investment approach](https://copleypoint.com/our-approach/), [platform model](https://copleypoint.com/platforms/) and [May 2026 Rendesco announcement](https://copleypoint.com/2026/05/13/copley-point-exits-part-of-its-shareholding-in-rendesco-to-pioneer-point-partners/).')


def market_signals():
    intro('02 / LANDSCAPE INTELLIGENCE','Market signals','Connect publicly sourced developments to specific origination questions. A dated research snapshot, not a live subscription or automated news feed.')
    signals=json.loads((Path(__file__).resolve().parent/'data'/'signals.json').read_text(encoding='utf-8'))
    themes=['All themes']+sorted(set(x['sector'] for x in signals))
    choice=st.selectbox('Filter signals by theme',themes)
    items=[x for x in signals if choice=='All themes' or x['sector']==choice]
    for item in items:
        st.markdown(f'<div class="topic-card"><div class="tag">{escape(item["date"])} · {escape(item["sector"].upper())} / VERIFIED SOURCE</div><div class="title">{escape(item["title"])}</div><p>{escape(item["fact"])}</p></div>',unsafe_allow_html=True)
        l,r=st.columns([1.1,.9],gap='medium')
        with l:
            st.markdown('**Origination interpretation**')
            st.write(item['implication'])
        with r:
            st.markdown('**Question worth asking**')
            st.write(item['question'])
            st.markdown(f'[Read primary source — {item["source"]}]({item["url"]})')
        with st.expander('Connect this intelligence to a demo opportunity',expanded=False):
            opts=df('opportunities')
            chosen=st.selectbox('Opportunity',opts['name'].tolist(),key='signal_'+item['id'])
            if st.button('Add to research log',key='attach_'+item['id']):
                oid=opts.loc[opts['name']==chosen,'id'].iloc[0]
                add_activity('Opportunity',oid,'Market signal',f'{item["title"]} | source: {item["url"]}',item['question'])
                st.success('Signal attached to demo activity history.')
        st.write('')
    st.caption('Source dates and statistics are frozen at November 2026. Interpretation is independently authored and requires subsequent verification. Browse source links for changes.')


def origination_radar():
    intro('03 / DISCOVER & QUALIFY','Origination radar','A transparent first-pass screen aligned with UK focus, post-technology risk, asset security, management quality and scalable platform formation.')
    x = df('opportunities').copy()
    a,b,c=st.columns([1.1,1.1,1])
    with a: sector_filter=st.multiselect('Sector', sorted(x.sector.unique()), default=sorted(x.sector.unique()))
    with b: stage_filter=st.multiselect('Stage', STAGES, default=STAGES)
    with c: min_score=st.slider('Minimum thesis fit',0,100,0,5)
    x['Thesis fit /100'] = x.apply(lambda r: thesis_score(r.to_dict())[0],axis=1)
    x=x[x.sector.isin(sector_filter)&x.stage.isin(stage_filter)&(x['Thesis fit /100']>=min_score)].sort_values('Thesis fit /100',ascending=False)
    if x.empty:
        st.info('No illustrative opportunities satisfy these filters.')
        return
    st.dataframe(x[['name','sector','region','capital_need_gbp_m','stage','Thesis fit /100']].rename(columns={'name':'Opportunity','sector':'Sector','region':'Region','capital_need_gbp_m':'Capital need (£m)','stage':'Stage'}), hide_index=True, use_container_width=True)
    lookup = dict(zip(x['name'],x['id']))
    selected=st.selectbox('Examine an opportunity',x['name'].tolist())
    op=record('opportunities',lookup[selected])
    score,parts=thesis_score(op)
    main,detail=st.columns([1.3,1],gap='large')
    with main:
        st.markdown(f'<div class="eyebrow">INVESTMENT THESIS / {escape(op["id"])}</div><div class="score">{score}<span style="font-size:1rem;color:#9cb0a5"> / 100</span></div>',unsafe_allow_html=True)
        st.write(op['description'])
        st.markdown('**Thesis fit decomposition**')
        fig=go.Figure(go.Bar(x=[r[1] for r in parts],y=[r[0] for r in parts],orientation='h',marker_color='#8abf9f',text=[f'{r[1]}/{r[2]}' for r in parts],textposition='outside',cliponaxis=False))
        fig.update_layout(yaxis=dict(autorange='reversed'),xaxis=dict(range=[0,23],showgrid=False),showlegend=False)
        mk_chart(fig,360)
    with detail:
        panel('Hypothetical capital requirement',f'£{float(op["capital_need_gbp_m"]):,.0f}m',f'Potential 3-year deployment £{float(op["capital_3y_gbp_m"]):,.0f}m')
        panel('Asset framework',op['platform_model'],f'{op["region"]} · {op["subsector"]}')
        st.markdown('**Critical challenge to thesis**')
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
    with st.expander('Add a new opportunity to the demo CRM'):
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
            description=st.text_area('Preliminary thesis')
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


def plot_network(partners: pd.DataFrame, contacts: pd.DataFrame):
    graph=nx.Graph()
    graph.add_node('Point / Origin',type='Hub')
    for _,p in partners.iterrows():
        graph.add_node(str(p['id']),type='Partner',label=str(p['name']).replace('Demo | ',''))
        graph.add_edge('Point / Origin',str(p['id']))
    for _,c in contacts.iterrows():
        graph.add_node(str(c['id']),type='Contact',label=str(c['name']))
        if str(c['partner_id']) in graph:
            graph.add_edge(str(c['partner_id']),str(c['id']))
    pos=nx.spring_layout(graph,seed=15,k=1.25,iterations=100)
    fig=go.Figure()
    for a,b in graph.edges():
        fig.add_trace(go.Scatter(x=[pos[a][0],pos[b][0]],y=[pos[a][1],pos[b][1]],mode='lines',line=dict(color='#44645d',width=1.5),hoverinfo='skip',showlegend=False))
    colors={'Hub':'#d5edce','Partner':'#78bd98','Contact':'#c9ac80'}
    for node_type in ['Hub','Partner','Contact']:
        nodes=[n for n,d in graph.nodes(data=True) if d['type']==node_type]
        fig.add_trace(go.Scatter(x=[pos[n][0] for n in nodes],y=[pos[n][1] for n in nodes],text=[graph.nodes[n].get('label',n) for n in nodes],mode='markers+text',textposition='top center',textfont=dict(size=10,color='#cbded1'),marker=dict(color=colors[node_type],size=23 if node_type=='Hub' else 14 if node_type=='Partner' else 9,line=dict(width=1,color='#0a1617')),hovertemplate='%{text}<extra></extra>',name=node_type))
    fig.update_layout(xaxis=dict(visible=False),yaxis=dict(visible=False),showlegend=True,hovermode='closest')
    mk_chart(fig,520)


def relationship_network():
    intro('04 / BUILD TRUST','Relationship network','An illustrative relationship map: who knows whom, which counterparties deserve attention and what the next thoughtful conversation should achieve.')
    p=df('partners'); c=df('contacts')
    left,right=st.columns([1.35,.95],gap='large')
    with left:
        st.subheader('Relationship pathways')
        plot_network(p,c)
        st.caption('All links represent fictional CRM examples, not actual relationships or introductions.')
    with right:
        st.subheader('Relationship intelligence')
        selected=st.selectbox('Partner archetype',p['name'].tolist())
        pt=p.loc[p['name']==selected].iloc[0].to_dict()
        ct=c.loc[c['partner_id']==pt['id']]
        panel('Capital range (indicative, invented)',f'£{pt["capital_min_m"]:,.0f}m–£{pt["capital_max_m"]:,.0f}m','Synthetic partner mandate')
        st.markdown('**Potential human connection**')
        if not ct.empty:
            contact=ct.iloc[0]
            st.write(f'**{contact["name"]}** · {contact["title"]}')
            st.caption(str(contact['mutual_connection']))
            st.write('Next step: '+str(contact['next_step']))
        else:
            st.info('No contact captured — research before outreach.')
        st.write('**Relationship access**')
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
    st.subheader('Latest recorded interactions')
    log=df('activities').sort_values('activity_date',ascending=False).head(10)
    st.dataframe(log[['activity_date','entity_type','entity_id','category','summary','next_step']].rename(columns={'activity_date':'Date','entity_type':'Entity','entity_id':'ID','category':'Activity','summary':'Learning','next_step':'Next action'}),hide_index=True,use_container_width=True)


def partnership_bridge():
    intro('05 / SIGNATURE FEATURE','The partnership bridge','One opportunity. One strategically aligned institutional partner. A credible introduction hypothesis. Explainable judgement, never automated deal-making.')
    opportunities=df('opportunities')
    options=opportunities['name'].tolist()
    select,access=st.columns([1.6,1])
    with select: selected=st.selectbox('Choose an illustrative platform opportunity', options, index=0)
    with access: weight=st.slider('Relationship-access weighting',0,50,20,5,help='How much should the practical ability to secure a meeting influence the shortlist? The rest is investment fit.')
    op=opportunities.loc[opportunities['name']==selected].iloc[0].to_dict()
    matches=[]
    for _,row in df('partners').iterrows():
        person=row.to_dict()
        fit=partner_fit(op,person,weight/100)
        matches.append({'id':person['id'],'Partner':person['name'],'Combined /100':fit['score'],'Investment /100':fit['investment'],'Access /100':fit['access'],'Sector fit':'✓' if fit['sector_ok'] else '—','Ticket fit':'✓' if fit['capacity_ok'] else '—'})
    ranks=pd.DataFrame(matches).sort_values(['Combined /100','Investment /100'],ascending=False)
    a,b,c=st.columns(3)
    with a: panel('Selected thesis',op['sector'],op['platform_model'])
    with b: panel('Illustrative required equity',f'£{float(op["capital_need_gbp_m"]):,.0f}m','Capital figure is invented for this demo')
    with c: panel('Top-ranked match',ranks.iloc[0]['Partner'].replace('Demo | ',''),f'{int(ranks.iloc[0]["Combined /100"])} / 100 heuristic score')
    st.subheader('Why this partner — and not simply the largest cheque?')
    st.dataframe(ranks.drop(columns=['id']),hide_index=True,use_container_width=True)
    partner_id=st.selectbox('Investigate a match',ranks['id'].tolist(),format_func=lambda pid: record('partners',pid)['name'])
    partner=record('partners',partner_id)
    f=partner_fit(op,partner,weight/100)
    left,right=st.columns([1.12,.88],gap='large')
    with left:
        st.markdown(f'<div class="eyebrow">PARTNER RATIONALE / SYNTHETIC</div><div class="score">{f["score"]} <span style="font-size:1rem;color:#a9bdb2">/ 100</span></div>',unsafe_allow_html=True)
        for label,key in [('Investment strategy alignment','investment'),('Relationship access','access')]:
            st.progress(f[key],text=f'{label} — {f[key]}/100')
        st.write('**Reasons to engage — or challenge**')
        for item in f['rationale']:
            st.markdown(f'<div class="evidence-line">{escape(item)}</div>',unsafe_allow_html=True)
        st.write('')
        st.warning('**Human checkpoint:** verify actual mandate, discretion, available capital, conflicts and the right introduction before any outreach. These scores are illustrative, not investment recommendations.', icon='⚖️')
    with right:
        st.markdown('**Introduction route**')
        st.markdown(f'<div class="topic-card"><div class="tag">THOUGHTFUL CONNECTION</div><div class="title">{escape(str(partner["introducer"]))}</div><p>Use the named relationship as a research prompt. The underlying contact and relationship are fictional.</p></div>',unsafe_allow_html=True)
        st.write('')
        st.markdown('**Partner mandate (fictional)**')
        st.write(partner['mandate_note'])
        with st.form('bridge_decision'):
            decision=st.selectbox('Your judgement',['Research further','Pursue introduction','Hold / not a fit'])
            reason=st.text_area('Commercial rationale',placeholder='What has to be true before a conversation adds value?')
            if st.form_submit_button('Capture decision',type='primary'):
                if not reason.strip():
                    st.error('Record the human rationale.')
                else:
                    add_activity('Opportunity',op['id'],'Partner review',f'{decision} — {partner["name"]}: {reason}','Validate with the investment team')
                    st.success('Decision captured in session activity log.')
    st.subheader('Convert intelligence into a usable conversation')
    st.download_button('Download internal relationship brief  ↓',data=partner_brief(op,partner,f,external=False),file_name=f'{op["id"]}_internal_brief.txt',mime='text/plain',use_container_width=True)
    st.caption('The engine ranks ONE proposed partner at a time. It does not assume a syndicate or claim knowledge of any real institution’s investment mandate.')


def carbon_intelligence():
    intro('06 / SECOND-ORDER THINKING','The carbon + capital lens','A sensitivity tool inspired by Copley Point’s published research on refurbishment versus rebuilding industrial property. The decision requires both climate and economic underwriting.')
    st.info('**Assumptions are illustrative, not from Copley Point’s asset data or research model.** Adjust the inputs to test hypotheses; no live emissions, pricing or energy data is connected.')
    with st.expander('Set assumptions — building and carbon',expanded=True):
        a,b,c=st.columns(3)
        with a:
            area=st.number_input('Industrial floor area (m²)',min_value=1000.0,max_value=1_000_000.0,value=15000.0,step=1000.0)
            years=st.slider('Evaluation horizon (years)',5,40,20)
            em_r=st.number_input('Refurbishment embodied carbon (kgCO₂e/m²)',0.0,2000.0,210.0,10.0)
        with b:
            em_n=st.number_input('New-build embodied carbon (kgCO₂e/m²)',0.0,3000.0,750.0,10.0)
            op_r=st.number_input('Refurbished annual operational carbon (kgCO₂e/m²/yr)',0.0,200.0,19.0,1.0)
            op_n=st.number_input('New-build annual operational carbon (kgCO₂e/m²/yr)',0.0,200.0,11.0,1.0)
        with c:
            cap_r=st.number_input('Refurbishment upfront capex (£/m²)',0.0,10000.0,450.0,25.0)
            cap_n=st.number_input('New-build upfront capex (£/m²)',0.0,20000.0,1250.0,25.0)
            st.caption('Capex excludes land, finance, tax, exit and other transaction costs.')
    with st.expander('Additional cash running-cost assumptions'):
        a,b=st.columns(2)
        with a: run_r=st.number_input('Refurbished annual operating costs (£/m²/yr)',0.0,1000.0,20.0,1.0)
        with b: run_n=st.number_input('New-build annual operating costs (£/m²/yr)',0.0,1000.0,14.0,1.0)
    scenario=CarbonScenario(area,em_r,em_n,op_r,op_n,cap_r,cap_n,run_r,run_n,years)
    results=calculate(scenario)
    a,b,c=st.columns(3)
    with a: st.metric('Refurbishment lifecycle emissions',f'{results["lifetime_refurb_t"]:,.0f} tCO₂e',help='Embodied plus operational emissions over chosen horizon')
    with b: st.metric('New-build lifecycle emissions',f'{results["lifetime_new_t"]:,.0f} tCO₂e')
    with c:
        p=results['carbon_payback_years']
        st.metric('New-build carbon payback',f'{p:.1f} yrs' if p!=float('inf') else 'Not reached',help='Years for lower annual new-build emissions to offset its higher upfront embodied carbon, where applicable')
    st.subheader('The long view: cumulative carbon')
    time=pd.DataFrame({'Year':list(range(years+1))})
    time['Refurbish (tCO₂e)']=results['embodied_refurb_t']+time['Year']*results['annual_refurb_t']
    time['Rebuild (tCO₂e)']=results['embodied_new_t']+time['Year']*results['annual_new_t']
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=time.Year,y=time['Refurbish (tCO₂e)'],mode='lines',name='Refurbish',line=dict(color='#b5e0c5',width=3)))
    fig.add_trace(go.Scatter(x=time.Year,y=time['Rebuild (tCO₂e)'],mode='lines',name='Rebuild',line=dict(color='#d7b889',width=3)))
    fig.update_layout(xaxis_title='Years',yaxis_title='Cumulative tCO₂e',hovermode='x unified')
    mk_chart(fig,380)
    left,right=st.columns(2)
    with left:
        delta=results['avoided_t_if_refurb']
        panel('Net carbon impact at horizon',f'{abs(delta):,.0f} tCO₂e '+('avoided by refurbishment' if delta>=0 else 'avoided by new build'),'Illustrative undiscounted carbon accounting; excludes end-of-life, lease dynamics and offsets.')
    with right:
        delta_gbp=results['avoided_gbp_if_refurb']
        panel('Cash-cost comparison (no discounting)',f'£{abs(delta_gbp)/1e6:,.2f}m '+('less for refurbishment' if delta_gbp>=0 else 'less for new build'),'Upfront capex + constant annual operating cost only. Not an asset valuation or NPV.')
    csv=time.to_csv(index=False).encode('utf-8')
    st.download_button('Download scenario time series (CSV)',data=csv,file_name='carbon_scenario_illustrative.csv',mime='text/csv')
    st.markdown('**Why this belongs in an origination app:** An industrial asset can look less attractive if you focus only on energy efficiency, but more resilient when embodied carbon, capex, tenant needs and an active-management plan are considered together. The tool is a screening conversation starter, not a verdict.')
    st.caption(f'Copley Point source: [The carbon case for upgrading existing industrial real estate]({PUBLIC_LINKS["Carbon research"]}). See the app methodology for exclusions.')


def partner_room():
    intro('07 / COMMUNICATE WITH DISCIPLINE','Partner briefing room','A partner-ready communication workflow: begin with one precise investment story, then disclose only what is appropriate for the intended audience.')
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
    st.text_area('Preview — actual downloadable content',content,height=410)
    st.download_button('Download this briefing  ↓',content,file_name=f'point_origin_{op["id"]}_{"external" if external else "internal"}.txt',mime='text/plain',type='primary')
    st.subheader('JV coordination — simulated milestone board')
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
            st.dataframe(public[['workstream','owner','status','due','deliverable']].rename(columns={'workstream':'Workstream','owner':'Owner','status':'Status','due':'Target','deliverable':'Shareable deliverable'}),hide_index=True,use_container_width=True)
        st.caption('External preview excludes all internal-only milestone rows and confidential notes. This is a local illustration, not a live investor workspace.')
    else:
        editor=st.data_editor(sub,hide_index=True,use_container_width=True,num_rows='fixed',disabled=['id','opportunity_id','workstream','owner','audience','deliverable','notes'],key='milestone_editor_'+op['id'])
        if st.button('Save milestone updates to session',type='primary'):
            if not set(editor['status']).issubset({'Not started','In progress','Complete'}):
                st.error('Use the defined statuses: Not started, In progress, Complete.')
            else:
                for _,r in editor.iterrows():
                    key=st.session_state.milestones['id']==r['id']
                    for col in ['status','due']:
                        st.session_state.milestones.loc[key,col]=r[col]
                st.success('Milestone board updated within this session. Export milestones CSV from the sidebar to preserve.')
    st.markdown('<div class="eyebrow">NO AUTOMATIC SHARING / NO INVESTOR LOG-IN</div>',unsafe_allow_html=True)
    st.write('A genuine partner portal would require permissioned identity, separately scoped workspaces, secure document storage, audit logs, explicit approvals and an agreed data-room policy. This prototype deliberately does **not** expose any public upload link, email partner or imply access to firm systems.')
    st.caption('In external mode the brief intentionally excludes internal risk notes, contact names, relationship history, scores and strategic judgement.')


def methodology():
    intro('08 / ACCOUNTABLE RESEARCH','Research & methodology','The difference between an impressive demonstration and a credible investment tool is provenance, transparency and knowing what is not yet known.')
    c1,c2=st.columns(2,gap='large')
    with c1:
        st.subheader('What the public record supports')
        st.markdown(f'''**Copley Point’s role:** an independent, management-owned sponsor focusing on UK real assets and platform businesses. [Official overview]({PUBLIC_LINKS['About Copley Point']}).

**Investment focus:** asset-backed downside protection; platform-building upside; post-technology risk; scalable capital deployment and selective relationships. [Approach]({PUBLIC_LINKS['Approach']}).

**Capital structure:** typically an institutional JV partner alongside the firm per platform, often with AssetCo/OpCo capital tranching. [Approach]({PUBLIC_LINKS['Approach']}) · [Platforms]({PUBLIC_LINKS['Platforms']}).

**Evidence of partnership execution:** the announced Block Industrial–Sixth Street joint venture in 2024, and Copley Point’s partial exit of Rendesco to Pioneer Point in May 2026. [Sixth Street]({PUBLIC_LINKS['Sixth Street JV']}) · [Rendesco]({PUBLIC_LINKS['Rendesco & Pioneer']}).

**Carbon as an underwriting question:** Copley Point published research comparing the carbon effects of existing industrial real-estate upgrades and new construction. [Research paper]({PUBLIC_LINKS['Carbon research']}).''')
    with c2:
        st.subheader('What is deliberately not asserted')
        st.markdown('''- No real investment mandate, active capital commitment or current appetite is ascribed to a third-party investor.
- No named fictional target is presented as a real deal, team, company or Copley Point pipeline item.
- The screens and partner rankings are **heuristics**, not proprietary due diligence or forecasts of probability, returns or credit quality.
- Capital, headcount, asset values, introductions, relationship histories and scores inside the demo are invented.
- There is no real-time market-data API, LinkedIn scraping, shared CRM or authenticated co-partner portal.''')
        st.subheader('Human governance rules')
        st.markdown('''1. **Source before scoring:** capture a verifiable basis for each commercial assertion.
2. **One capital partner per platform:** evaluate fit and flexibility, not number of prospective co-investors.
3. **Human decision owner:** a ranked score never initiates contact, sends information or makes an investment decision.
4. **Permission before sharing:** external briefs are redacted by default; never insert confidential data in a public demo.
5. **Retest assumptions:** a relevant introduction is an invitation to understand a counterparty, not evidence of an investable opportunity.''')
    st.write('')
    st.subheader('Values translated into design decisions')
    st.caption('Copley Point publicly identifies Candour, Creativity, Empathy, Humility and Tenacity as firm values. This concept makes each value operational rather than using it as decorative branding.')
    columns=st.columns(5)
    behaviours=[('CANDOUR','Cited sources and clear uncertainty'),('CREATIVITY','Asset and capital scenario thinking'),('EMPATHY','Understand the other side’s mandate'),('HUMILITY','Human review and explicit limitations'),('TENACITY','Visible ownership of next actions')]
    for col,(value,behaviour) in zip(columns,behaviours):
        with col:
            st.markdown(f'<div class="topic-card"><div class="tag">{escape(value)}</div><p>{escape(behaviour)}</p></div>',unsafe_allow_html=True)
    st.caption(f'Firm values source: [Copley Point — About Us]({PUBLIC_LINKS["About Copley Point"]}).')
    st.write('')
    st.subheader('From prototype to a secure internal product')
    st.markdown('**Phase 1:** controlled internal CSV/CRM ingest, verified source links, owner and next-action workflow. **Phase 2:** relational database, SSO and role-based permissions, auditable edits, secure document repository and counterparty consent tracking. **Phase 3:** licensed company/property data feeds, calibrated scoring with analyst review and a permissioned partner workspace.')
    st.caption('Developed independently for interview discussion. Copley Point and named historical business partners have not contributed data to, approved or sponsored this demo.')


init()
if st.session_state.page == 'Welcome':
    welcome()
else:
    sidebar()
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
