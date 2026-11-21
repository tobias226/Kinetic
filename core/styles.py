CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --mint:#b5e0c5; --bright:#d5f8dd; --bg:#091315; --panel:#132326; --ink:#eff5ef; --muted:#a2b4ad; --gold:#b7a17c; --line:#2a4540; }
html, body, [class*="css"], [data-testid="stApp"] {font-family:'DM Sans',sans-serif!important;}
.stApp {background: radial-gradient(ellipse 80% 45% at 83% -10%,#193d3a 0%,transparent 74%),#0b1618;color:var(--ink);}
.main .block-container {padding-top:1.55rem;padding-bottom:4rem;max-width:1300px;}
header[data-testid="stHeader"] {background: transparent!important;}
[data-testid="stSidebar"] {background:#0b1b1e;border-right:1px solid #23393b;}
[data-testid="stSidebar"] .block-container {padding-top:2rem;}
[data-testid="stSidebar"] hr {border-color:#30413f;}
[data-testid="stSidebar"] [role="radiogroup"] label {padding:.36rem .5rem;border-radius:8px;}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {background:#1a3433;}
[data-testid="stMetric"] {background:#142528;border:1px solid #28423e;padding:18px 20px;border-radius:14px;min-height:122px;}
[data-testid="stMetricLabel"] {color:#a9bbb2;font-size:.80rem;}
[data-testid="stMetricValue"] {color:#e8faed;font-size:2rem;font-weight:700;}
[data-testid="stMetricDelta"] {font-size:.72rem;}
[data-testid="stVerticalBlock"] {gap:.75rem;}
.stButton>button[kind="primary"], .stDownloadButton>button[kind="primary"] {background:#b5e0c5;color:#102321;border:1px solid #b5e0c5;font-weight:700;border-radius:9px;padding:.64rem 1.15rem;}
.stButton>button[kind="primary"]:hover {background:#d5f8dd;color:#0b1618;border-color:#d5f8dd;}
.stButton>button[kind="secondary"],.stDownloadButton>button {border:1px solid #46635b;background:#18302f;color:#e3f4e6;border-radius:9px;}
.stButton>button:hover,.stDownloadButton>button:hover {border-color:#b5e0c5;color:#b5e0c5;}
[data-testid="stTabs"] button {color:#b1c1bc;}
[data-testid="stMarkdownContainer"] a {color:#bee9cc;text-decoration-color:#6e9b88;}
[data-testid="stDataFrame"] {border:1px solid #26443f;border-radius:11px;overflow:hidden;}
[data-testid="stExpander"] {border:1px solid #29453f;border-radius:10px;}
[data-testid="stAlert"] {border-radius:10px;}
h1,h2,h3{font-family:'Manrope','DM Sans',sans-serif!important;letter-spacing:-.035em;}
h1{font-weight:800!important;} h2{font-weight:700!important;}
.portal-eyebrow,.eyebrow{color:#a8c9ba;font-size:.73rem;font-weight:700;letter-spacing:.17em;text-transform:uppercase;}
.portal-wordmark{font-family:Manrope,sans-serif;font-size:1.42rem;letter-spacing:.10em;font-weight:800;line-height:1.5;}
.portal-wordmark span {color:#b5e0c5;}
.concept-tag {color:#9bb4ab;font-size:.74rem;letter-spacing:.09em;}
.portal-hero{margin-top:1.4rem;border:1px solid #35564d;border-radius:25px;position:relative;overflow:hidden;padding:clamp(1.45rem,3.8vw,3.6rem);min-height:540px;background:radial-gradient(circle at 78% 28%,rgba(92,165,131,.18),transparent 33%),radial-gradient(circle at 25% 95%,rgba(39,74,70,.45),transparent 32%),linear-gradient(122deg,#142826,#091417 78%);}
.portal-hero:before{content:"";position:absolute;inset:0;background:linear-gradient(120deg,rgba(255,255,255,.02),transparent 23%,transparent 78%,rgba(255,255,255,.02));pointer-events:none;}
.portal-hero:after{content:"";pointer-events:none;position:absolute;right:-7%;top:6%;width:44%;height:92%;border:1px solid rgba(181,224,197,.12);transform:skew(-23deg) rotate(-9deg);box-shadow:-30px 20px 0 -2px rgba(174,229,201,.05),-65px 55px 0 -2px rgba(174,229,201,.04),-110px 90px 0 -2px rgba(174,229,201,.03);}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(360px,.85fr);gap:1.7rem;align-items:center;position:relative;z-index:2;min-height:460px;}
.portal-hero .hero-title{font-family:Manrope,sans-serif;font-weight:800;font-size:clamp(2.7rem,5.6vw,5.1rem);line-height:1.04;letter-spacing:-.068em;color:#eff5ee;max-width:740px;margin:22px 0 20px;}
.portal-hero em{font-style:normal;color:#b5e0c5;}
.portal-hero .subhead{font-size:1.11rem;line-height:1.8;max-width:585px;color:#aabeb5;}
.hero-footer{display:flex;gap:20px;flex-wrap:wrap;margin-top:36px;padding-top:22px;border-top:1px solid var(--line);max-width:740px;}
.hero-footer span{font-size:.73rem;color:#b7c7bd;letter-spacing:.08em;}
.hero-footer strong{display:block;font-size:.92rem;color:#f0f5ec;letter-spacing:0;margin-top:6px;}
.main-intro{margin:0 0 20px 0;}
.main-intro .page-title{font-family:Manrope,sans-serif;font-weight:800;font-size:2.28rem;letter-spacing:-.05em;color:#f3f6f0;margin:8px 0 8px;}
.main-intro .page-desc{color:#a9bdb1;font-size:.99rem;line-height:1.7;max-width:780px;}
.glass-card{min-height:140px;border:1px solid #28443d;background:linear-gradient(135deg,#172c2b,#102021);border-radius:14px;padding:23px 23px;margin-bottom:9px;}
.glass-card .card-value{font-family:Manrope,sans-serif;font-size:1.24rem;font-weight:700;letter-spacing:-.04em;margin:12px 0;color:#e8f7e9;}
.muted{color:#a0b3aa;font-size:.83rem;line-height:1.65;}
.section-line{border-top:1px solid #294039;margin-top:22px;padding-top:13px;}
.topic-card{min-height:155px;padding:22px 23px;border-radius:15px;background:#142729;border:1px solid #2b4540;}
.topic-card .tag{color:#b6d9c4;font-size:.72rem;letter-spacing:.11em;font-weight:700;}
.topic-card .title{font-size:1.08rem;font-weight:700;color:#eef5ef;margin:11px 0 6px;}
.topic-card p{font-size:.87rem;color:#aec0b8;line-height:1.63;}
.ribbon{display:inline-block;font-size:.72rem;letter-spacing:.08em;padding:6px 10px;border-radius:22px;background:#1c4137;border:1px solid #376f51;color:#cdeed4;font-weight:700;}
.ribbon-demo{background:#342b21;border-color:#796749;color:#e7d4aa;}
.score{font-family:Manrope,sans-serif;font-size:2.65rem;line-height:1.15;font-weight:800;color:#d7fae1;}
.evidence-line{color:#abbcb3;font-size:.82rem;padding:.56rem 0;border-bottom:1px solid #233c37;}
.highlight-text{color:#bbe8ce;}
.hero-smallnote{font-size:.8rem;color:#8fa89d;margin-top:15px;}

.hero-visual{position:relative;height:440px;border:1px solid rgba(181,224,197,.12);border-radius:22px;background:radial-gradient(circle at 70% 20%,rgba(106,198,147,.14),transparent 24%),linear-gradient(180deg,rgba(16,30,31,.92),rgba(11,20,23,.84));box-shadow:inset 0 1px 0 rgba(255,255,255,.03);overflow:hidden;}
.hero-visual .grid-lines{position:absolute;inset:0;background-image:linear-gradient(rgba(181,224,197,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(181,224,197,.06) 1px,transparent 1px);background-size:46px 46px;mask-image:linear-gradient(180deg,rgba(255,255,255,.85),rgba(255,255,255,.25));}
.hero-visual .map-sheen{position:absolute;inset:-10% -5% auto auto;width:88%;height:88%;background:radial-gradient(circle at 50% 45%,rgba(79,157,132,.15),transparent 34%);filter:blur(6px);animation:drift 10s ease-in-out infinite;}
.flow{position:absolute;height:2px;border-radius:999px;background:linear-gradient(90deg,transparent,rgba(213,248,221,.95),transparent);opacity:.9;transform-origin:left center;animation:flow 3.8s linear infinite;}
.flow.f1{width:170px;left:36px;top:102px;transform:rotate(8deg);animation-delay:0s;}
.flow.f2{width:200px;left:112px;top:176px;transform:rotate(-10deg);animation-delay:1.1s;}
.flow.f3{width:185px;left:48px;top:278px;transform:rotate(11deg);animation-delay:2s;}
.flow.f4{width:155px;left:174px;top:86px;transform:rotate(31deg);animation-delay:.65s;}
.flow.f5{width:175px;left:198px;top:228px;transform:rotate(-24deg);animation-delay:1.8s;}
.node{position:absolute;width:14px;height:14px;border-radius:50%;background:#d5f8dd;box-shadow:0 0 0 0 rgba(181,224,197,.85);animation:pulse 2.8s infinite;}
.node.n1{left:52px;top:96px;animation-delay:.2s;}
.node.n2{left:212px;top:150px;animation-delay:.7s;}
.node.n3{left:115px;top:262px;animation-delay:1.2s;}
.node.n4{left:303px;top:206px;animation-delay:1.7s;}
.node.n5{left:248px;top:321px;animation-delay:2.2s;}
.node-label{position:absolute;font-size:.70rem;letter-spacing:.06em;color:#bad0c5;text-transform:uppercase;}
.node-label.l1{left:72px;top:84px;} .node-label.l2{left:230px;top:138px;} .node-label.l3{left:135px;top:250px;} .node-label.l4{left:324px;top:194px;}
.energy-card{position:absolute;padding:.7rem .85rem;border:1px solid rgba(181,224,197,.16);border-radius:12px;background:rgba(11,24,26,.88);backdrop-filter:blur(7px);box-shadow:0 10px 32px rgba(0,0,0,.22);animation:floaty 6.2s ease-in-out infinite;}
.energy-card strong{display:block;font-size:.83rem;color:#eef5ef;letter-spacing:.01em;}
.energy-card span{display:block;font-size:.72rem;color:#9fb5ad;margin-top:4px;line-height:1.45;}
.energy-card.c1{right:18px;top:24px;animation-delay:0s;} .energy-card.c2{right:28px;top:145px;animation-delay:1.4s;} .energy-card.c3{right:38px;bottom:32px;animation-delay:2.5s;}
.turbine{position:absolute;left:52%;bottom:38px;width:155px;height:310px;transform:translateX(-50%);}
.turbine .mast{position:absolute;left:50%;bottom:0;width:10px;height:196px;border-radius:10px;background:linear-gradient(180deg,#d8e8dd,#9db5ad);transform:translateX(-50%);box-shadow:0 0 28px rgba(213,248,221,.09);}
.turbine .hub{position:absolute;left:50%;bottom:182px;width:18px;height:18px;border-radius:50%;background:#e9f6ec;transform:translateX(-50%);z-index:3;box-shadow:0 0 18px rgba(213,248,221,.55);}
.turbine .rotor{position:absolute;left:50%;bottom:191px;width:0;height:0;transform:translateX(-50%);animation:spin 7s linear infinite;transform-origin:center center;z-index:2;}
.turbine .blade{position:absolute;left:-4px;top:-84px;width:8px;height:92px;border-radius:999px;background:linear-gradient(180deg,#eef8f0,#93ab9d);transform-origin:50% 84px;box-shadow:0 0 12px rgba(213,248,221,.22);}
.turbine .blade.b2{transform:rotate(120deg);}
.turbine .blade.b3{transform:rotate(240deg);}
.turbine .baseglow{position:absolute;left:50%;bottom:10px;width:178px;height:28px;transform:translateX(-50%);background:radial-gradient(circle,rgba(181,224,197,.24),transparent 65%);filter:blur(4px);}
.orbit{position:absolute;border:1px solid rgba(181,224,197,.12);border-radius:50%;}
.orbit.o1{width:270px;height:270px;left:104px;top:88px;animation:rotateSlow 18s linear infinite;}
.orbit.o2{width:336px;height:336px;left:72px;top:55px;animation:rotateSlow 25s linear infinite reverse;}
.orbit-dot{position:absolute;width:8px;height:8px;border-radius:50%;background:#b5e0c5;top:18px;left:48%;box-shadow:0 0 14px rgba(213,248,221,.55);}
.visual-tag{position:absolute;left:22px;bottom:18px;font-size:.72rem;letter-spacing:.14em;color:#a6c8b7;text-transform:uppercase;}

@keyframes spin {from{transform:translateX(-50%) rotate(0deg)} to{transform:translateX(-50%) rotate(360deg)}}
@keyframes pulse {0%{box-shadow:0 0 0 0 rgba(181,224,197,.55)} 70%{box-shadow:0 0 0 15px rgba(181,224,197,0)} 100%{box-shadow:0 0 0 0 rgba(181,224,197,0)}}
@keyframes flow {0%{opacity:0;transform:translateX(-18px) scaleX(.7)} 25%{opacity:.92;} 75%{opacity:.92;} 100%{opacity:0;transform:translateX(26px) scaleX(1.02)}}
@keyframes floaty {0%,100%{transform:translateY(0px)} 50%{transform:translateY(-8px)}}
@keyframes drift {0%,100%{transform:translateY(0) translateX(0)} 50%{transform:translateY(10px) translateX(-10px)}}
@keyframes rotateSlow {from{transform:rotate(0deg)} to{transform:rotate(360deg)}}

@media (max-width: 1080px){
  .hero-grid{grid-template-columns:1fr;}
  .hero-visual{height:360px;}
  .portal-hero{min-height:unset;}
}
@media (max-width: 720px){
  .portal-hero .hero-title{font-size:clamp(2.4rem,8vw,4.2rem)}
  .hero-visual{height:320px;}
  .energy-card{display:none;}
  .turbine{left:58%;transform:translateX(-58%) scale(.87);transform-origin:bottom center;}
}
/* KINETIC v2: restrained introduction and spacious three-area workspace */
.intro-mark{font-size:1.65rem;margin:1rem 0 .05rem;}
.kinetic-hero{display:grid;grid-template-columns:minmax(0,1.16fr) minmax(290px,.84fr);align-items:center;gap:3rem;margin-top:1.6rem;min-height:430px;padding:clamp(2.1rem,4.8vw,4.6rem);background:linear-gradient(120deg,#102321,#091518);border:1px solid #325149;border-radius:22px;overflow:hidden;position:relative;isolation:isolate;}
.kinetic-copy{position:relative;z-index:2;min-width:0;}
.kinetic-copy .portal-eyebrow{font-size:.70rem;letter-spacing:.13em;}
.kinetic-headline{font:800 clamp(2.65rem,4.55vw,4.85rem)/1.10 Manrope,sans-serif;letter-spacing:-.06em;margin:1.4rem 0 1.25rem;max-width:750px;color:#f2f7f1;overflow-wrap:normal;}
.kinetic-headline em{font-style:normal;color:#b5e0c5;}
.kinetic-copy p{font-size:1.06rem;line-height:1.8;color:#b5c9bd;max-width:510px;}
.kinetic-visual{height:320px;width:100%;max-width:400px;min-width:0;position:relative;justify-self:center;overflow:hidden;isolation:isolate;background:radial-gradient(circle at 50% 49%,rgba(100,173,137,.12),transparent 62%);}
.kinetic-glow{position:absolute;inset:14%;border-radius:50%;background:radial-gradient(circle,rgba(102,188,139,.13),transparent 70%);filter:blur(14px);}
.kinetic-ring{position:absolute;border:1px solid rgba(176,218,184,.22);border-radius:50%;left:50%;top:49%;transform:translate(-50%,-50%);}
.kinetic-ring.ring-one{width:202px;height:202px;}.kinetic-ring.ring-two{width:280px;height:280px;border-color:rgba(176,218,184,.09);}
.kinetic-tower{position:absolute;left:50%;top:46%;width:8px;height:171px;background:linear-gradient(#dbece0,#809b90);transform:translateX(-50%);border-radius:6px 6px 2px 2px;z-index:2;}
.kinetic-rotor{position:absolute;left:50%;top:46%;height:0;width:0;animation:kinetic-spin 10s linear infinite;z-index:3;}
.kinetic-rotor i{position:absolute;display:block;left:-4px;bottom:-4px;height:99px;width:8px;background:linear-gradient(#fbfffa,#a2c7b2);border-radius:100% 100% 45% 45%;transform-origin:4px calc(100% - 4px);box-shadow:0 0 14px rgba(194,244,206,.10);}
.kinetic-rotor i:nth-child(2){transform:rotate(120deg);}.kinetic-rotor i:nth-child(3){transform:rotate(240deg);}
.kinetic-hub{position:absolute;left:50%;top:46%;width:17px;height:17px;transform:translate(-50%,-50%);border-radius:50%;background:#edfaef;box-shadow:0 0 16px #a9dcbf;z-index:4;}
.kinetic-trace{position:absolute;left:9%;height:1px;width:80%;background:linear-gradient(90deg,transparent,rgba(181,224,197,.42),transparent);z-index:1;}
.trace-one{top:36%;transform:rotate(-18deg)}.trace-two{top:69%;transform:rotate(22deg)}
.kinetic-dot{position:absolute;width:8px;height:8px;border-radius:50%;background:#a8dec0;box-shadow:0 0 0 0 rgba(181,224,197,.43);animation:kinetic-pulse 4s ease-out infinite;}
.dot-one{left:13%;top:30%}.dot-two{right:16%;top:23%;animation-delay:1.4s}.dot-three{right:12%;bottom:18%;animation-delay:2.5s}
@keyframes kinetic-spin{to{transform:rotate(360deg)}}
@keyframes kinetic-pulse{0%{box-shadow:0 0 0 0 rgba(181,224,197,.35)}70%{box-shadow:0 0 0 12px rgba(181,224,197,0)}100%{box-shadow:0 0 0 0 rgba(181,224,197,0)}}
.area-card{padding:1.85rem 1.55rem;min-height:255px;background:linear-gradient(145deg,#172b2b,#112122);border:1px solid #2d4942;border-radius:17px;display:flex;flex-direction:column;gap:.95rem;margin-top:1.1rem;}
.area-card h3{font:700 clamp(1.2rem,1.7vw,1.55rem)/1.35 Manrope,sans-serif;margin:0;color:#f1f8f1;letter-spacing:-.03em;}
.area-card p{color:#afc5b9;line-height:1.7;font-size:.95rem;margin:0;}
.kinetic-table-scroll{overflow-x:auto;border:1px solid #2f4b42;border-radius:14px;background:#112224;margin:.65rem 0 1.1rem;}
.kinetic-table{border-collapse:collapse;width:100%;min-width:650px;font-size:.88rem;color:#e9f6ed;}
.kinetic-table th{text-align:left;color:#b2c9bb;background:#1b3331;letter-spacing:.045em;font-size:.73rem;padding:15px 17px;font-weight:700;white-space:nowrap;}
.kinetic-table td{border-top:1px solid #2a423b;padding:16px 17px;line-height:1.55;vertical-align:top;}
.kinetic-table tbody tr:nth-child(even){background:#15282a;}
.kinetic-table tbody tr:hover{background:#203a36;}
[data-testid="stDataFrame"]{background:#142628!important;}
[data-testid="stDataFrame"] canvas{border-radius:9px;}
[data-testid="stMarkdownContainer"] p{line-height:1.65;}
[data-testid="stPlotlyChart"]{padding:.25rem 0 .6rem;}
[data-testid="stMetric"]{min-height:134px;}
[data-testid="stMetricLabel"] p{font-size:.81rem!important;line-height:1.45!important;}
.stButton>button{min-height:2.7rem;}
@media(max-width:1040px){.kinetic-hero{grid-template-columns:minmax(0,1fr) minmax(250px,.72fr);gap:1.25rem;padding:2.3rem}.kinetic-headline{font-size:clamp(2.2rem,4vw,3.65rem)}}
@media(max-width:780px){.kinetic-hero{grid-template-columns:1fr;gap:1rem;padding:2rem 1.5rem}.kinetic-visual{height:265px;max-width:315px}.kinetic-headline{font-size:clamp(2.3rem,7vw,3.5rem)}.area-card{min-height:170px}}
@media(prefers-reduced-motion:reduce){.kinetic-rotor,.kinetic-dot{animation:none!important}}
/* KINETIC v3 — editorial layout, dark form controls, spacious navigation */
:root {--kin-bg:#071513;--kin-pine:#102923;--kin-moss:#19352c;--kin-fern:#2f5a43;--kin-sage:#a8d8b8;--kin-text:#f1f8f2;--kin-muted:#bbd0c2;}
.stApp{background:radial-gradient(circle at 80% -5%,rgba(53,108,78,.22),transparent 35%),linear-gradient(180deg,#0b1917,#0a1819 68%,#0b1818)!important;color:#eff7f0!important;}
.main .block-container{max-width:1380px!important;padding-top:2rem!important;padding-bottom:5rem!important;}
[data-testid="stVerticalBlock"]{gap:1.0rem!important;}
[data-testid="stMarkdownContainer"] h2,[data-testid="stMarkdownContainer"] h3,[data-testid="stMarkdownContainer"] h4{color:#eef8ef!important;}
[data-testid="stMarkdownContainer"] p,[data-testid="stMarkdownContainer"] li{color:#d1e0d6;line-height:1.7;}
[data-testid="stCaptionContainer"] p{color:#b8ccbf!important;}
[data-testid="stMarkdownContainer"] strong{color:#ecf7ed;}
[data-testid="stMetric"]{background:linear-gradient(145deg,#17332b,#102421)!important;border-color:#345747!important;border-radius:17px!important;}
[data-testid="stMetricLabel"] p{color:#c4d8c8!important;}
[data-testid="stMetricValue"]{color:#e8faec!important;font-size:1.85rem!important;}
[data-testid="stExpander"]{background:#112721!important;border-color:#315044!important;border-radius:13px!important;}
[data-testid="stExpander"] summary{color:#edf7ef!important;font-weight:600!important;}
[data-testid="stForm"]{background:#112721!important;border:1px solid #315344!important;border-radius:15px!important;padding:1.1rem!important;}
/* Inputs, dropdown lists, text boxes and date controls have consistent dark surfaces. */
[data-testid="stTextInput"] input,[data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input,[data-testid="stDateInput"] input,
[data-testid="stFileUploader"] section,[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea{
  color:#f3fbf4!important;background:#182f28!important;caret-color:#c5eacd!important;
  border-color:#355c49!important;
}
[data-baseweb="input"],[data-baseweb="textarea"],[data-baseweb="select"] > div,
[data-testid="stDateInput"] [data-baseweb="input"]{
  background:#182f28!important;color:#eef7ee!important;border-color:#355b49!important;
  border-radius:9px!important;
}
[data-baseweb="select"] *{color:#edf7ed!important;}
[data-baseweb="popover"] [role="listbox"],[data-baseweb="menu"],[data-baseweb="popover"] ul,
[role="listbox"]{background:#162e27!important;color:#eef7ee!important;}
[role="option"]{background:#162e27!important;color:#eef7ee!important;}
[role="option"]:hover,[role="option"][aria-selected="true"]{background:#2d5840!important;}
[data-testid="stSelectbox"] label p,[data-testid="stTextInput"] label p,
[data-testid="stNumberInput"] label p,[data-testid="stTextArea"] label p,
[data-testid="stDateInput"] label p,[data-testid="stSlider"] label p{
 color:#e0efe3!important;font-weight:600!important;
}
[data-testid="stRadio"] label p,[data-testid="stCheckbox"] label p{color:#ecf7ed!important;}
[data-testid="stAlert"]{background:#1d332b!important;color:#f0f7f0!important;border:1px solid #3c644b!important;}
[data-testid="stAlert"] p{color:#e6f4e9!important;}
.stButton>button[kind="secondary"],.stDownloadButton>button{
 background:linear-gradient(135deg,#1c3b30,#142b26)!important;
 border:1px solid #47745a!important;color:#f0f8f0!important;
 border-radius:10px!important;min-height:3rem!important;
}
.stButton>button[kind="secondary"]:hover,.stDownloadButton>button:hover{
 background:#284d3a!important;color:#f5fff4!important;border-color:#8cc7a1!important;
}
.stButton>button[kind="primary"]{background:linear-gradient(135deg,#2f7e54,#78d8a2)!important;color:#f6fff8!important;border-color:#7bd8a2!important;border-radius:14px!important;min-height:3.35rem!important;font-weight:800!important;font-size:1.01rem!important;letter-spacing:.01em;box-shadow:0 10px 28px rgba(71,167,111,.22)!important;} 
.stButton>button[kind="primary"]:hover{background:linear-gradient(135deg,#3d9663,#96e2b7)!important;color:#ffffff!important;border-color:#9fe6bf!important;transform:translateY(-1px);} 
.stButton>button:disabled{background:#2b5540!important;color:#ecf9ef!important;opacity:1!important;border-color:#83c29d!important;cursor:default!important;}
.stButton>button:focus-visible,a:focus-visible{outline:2px solid #ccefd1!important;outline-offset:3px;}

/* Hero stays legible even at laptop widths: animation is confined to its own column. */
.kinetic-brand{font-family:Manrope,sans-serif;font-weight:800;font-size:clamp(4rem,8.5vw,7.8rem);line-height:1.01;letter-spacing:.13em;color:#f3fbf4;margin:.55rem 0 .35rem;text-shadow:0 0 18px rgba(170,236,190,.08);} 
.kinetic-brand span{color:#bff6cc;} 
.kinetic-brand.compact{font-size:clamp(2.2rem,4vw,3.5rem);margin-top:.3rem;}
.kinetic-brand-subtitle{font-size:.78rem;font-weight:800;color:#cdebd5;letter-spacing:.22em;margin:.55rem 0 1.15rem;} 
.welcome-stage{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(340px,.98fr);gap:clamp(1.2rem,4vw,4.3rem);align-items:center;background:radial-gradient(circle at 75% 35%,rgba(51,110,72,.17),transparent 45%),linear-gradient(121deg,#142b25 0%,#071714 100%);border:1px solid #355f47;border-radius:25px;padding:clamp(1.7rem,4.5vw,4.5rem);min-height:470px;margin:1.3rem 0 1.8rem;overflow:hidden;isolation:isolate;}
.welcome-copy{min-width:0;position:relative;z-index:2;}
.welcome-copy .portal-eyebrow{color:#c6ebcf;letter-spacing:.16em;font-size:.76rem;} 
.welcome-headline{font:800 clamp(3.2rem,5.9vw,5.8rem)/1.03 Manrope,sans-serif;letter-spacing:-.07em;color:#f4faf4;margin:1.35rem 0 1.1rem;text-wrap:balance;} 
.welcome-headline em{font-style:normal;color:#bff3c8;} 
.welcome-copy p{max-width:520px;font-size:1.14rem;line-height:1.82;color:#d7e7d8;} 
.constellation{height:410px;width:100%;max-width:620px;margin:0 auto;min-width:0;position:relative;isolation:isolate;overflow:hidden;} 
.constellation:before{content:"";position:absolute;inset:3%;border-radius:32px;background:radial-gradient(circle at 28% 28%,rgba(126,228,165,.22),transparent 26%),radial-gradient(circle at 74% 34%,rgba(53,154,103,.18),transparent 26%),radial-gradient(circle at 50% 68%,rgba(178,246,204,.14),transparent 30%);filter:blur(8px);z-index:-1;} 
.constellation svg{display:block;width:100%;height:100%;overflow:visible;}
.mesh-orbit circle{fill:none;stroke:rgba(129,194,146,.13);stroke-width:1;stroke-dasharray:3 8;}
.mesh-lines line{stroke:rgba(139,196,152,.43);stroke-width:1.4;stroke-dasharray:4 7;animation:kinetic-dash 10s linear infinite;}
.mesh-nodes .mesh-node{fill:#b2e6bf;stroke:#16382b;stroke-width:3;filter:drop-shadow(0 0 5px rgba(153,228,169,.7));animation:kinetic-node 4s ease-in-out infinite;transform-origin:center;transform-box:fill-box;}
.mesh-nodes .mesh-node.core{fill:#e3ffea;stroke:#2b6948;stroke-width:4;}
.mesh-nodes .mesh-node.small{fill:#6fa783;}
.mesh-particle{fill:#defbe3;filter:drop-shadow(0 0 5px #a9edb9);}
.mesh-label{font-family:Manrope,sans-serif;fill:#c2dbc9;font-weight:600;font-size:12px;}
.mesh-core-label{font-family:Manrope,sans-serif;fill:#ecfbf0;font-weight:800;font-size:13px;letter-spacing:3px;}
.visual-caption{position:absolute;bottom:2px;left:0;right:0;text-align:center;color:#b9e4c4;letter-spacing:.12em;font-size:.66rem;font-weight:800;} 
.live-dot{display:inline-block;vertical-align:middle;background:#a4dcb3;width:6px;height:6px;border-radius:50%;margin-right:7px;box-shadow:0 0 10px #94d6a4;}
@keyframes kinetic-dash{to{stroke-dashoffset:-100;}}
@keyframes kinetic-node{0%,100%{opacity:.8;transform:scale(.95);}50%{opacity:1;transform:scale(1.1);}}

/* Explore cards: three harmonious shades of green, explicit concept then title */
.area-card{position:relative;min-height:290px;padding:2.0rem 1.7rem;border-radius:20px;border:1px solid #42664e;overflow:hidden;margin-top:1rem;gap:1rem;}
.area-card.pine{background:linear-gradient(145deg,#17382f,#0e2521)!important;}
.area-card.moss{background:linear-gradient(145deg,#24483b,#132c27)!important;}
.area-card.sage{background:linear-gradient(145deg,#345747,#1b342d)!important;}
.area-card:before{content:"";position:absolute;right:-42px;top:-42px;width:180px;height:180px;border:1px solid rgba(191,241,198,.13);border-radius:50%;box-shadow:0 0 0 35px rgba(156,209,165,.035),0 0 0 80px rgba(156,209,165,.025);}
.area-card .area-number{color:#bdddc5;font-size:.70rem;font-weight:700;letter-spacing:.12em;line-height:1.6;position:relative;z-index:1;}
.area-card h3{font:800 clamp(1.22rem,1.7vw,1.5rem)/1.3 Manrope,sans-serif;color:#f4faf4!important;position:relative;z-index:1;margin:0;}
.area-card p{font-size:.92rem;line-height:1.75;color:#d0e3d2!important;position:relative;z-index:1;}
.area-bottom-mark{position:absolute;bottom:12px;right:22px;color:#bde2c5;font-size:1.4rem;opacity:.6;}
.section-divider-large{margin:3.3rem 0 2rem;height:1px;background:linear-gradient(90deg,#4b7e58,rgba(143,202,151,.07));}
.feature-heading{display:flex;justify-content:space-between;gap:2rem;align-items:center;margin:0 0 1rem;}
.feature-heading h3{font:800 clamp(1.5rem,2.4vw,2.25rem) Manrope,sans-serif;letter-spacing:-.04em;color:#f1f8f1;margin:.6rem 0 .4rem;}
.feature-heading p{color:#bfd2c4;font-size:.95rem;max-width:640px;line-height:1.7;margin:0;}
.feature-pill{font-size:.67rem;letter-spacing:.12em;border:1px solid #4c805a;background:#234331;color:#ceebd5;padding:9px 13px;border-radius:22px;white-space:nowrap;}
/* Navigation and step-by-step narrative */
.nav-area-name{font-size:.8rem;font-weight:800;letter-spacing:.12em;color:#b7dec2;padding:0 .2rem;}
.nav-area-name span{color:#87a99a;font-size:.68rem;font-weight:600;}
.navigation-divider{margin:1.2rem 0 1.55rem;border-bottom:1px solid #345347;}
.step-heading{display:flex;align-items:flex-start;gap:1rem;padding:1.1rem 0 .65rem;margin:1.45rem 0 .7rem;border-top:1px solid #345546;}
.step-index{flex:0 0 auto;color:#c7e8cc;background:#1d3e2e;border:1px solid #41694c;border-radius:11px;font:800 1rem Manrope,sans-serif;padding:.7rem .75rem;line-height:1;}
.step-copy h3{font:800 clamp(1.18rem,2.1vw,1.45rem)/1.4 Manrope,sans-serif;color:#eff8f0;margin:0;letter-spacing:-.025em;}
.step-copy p{font-size:.93rem;color:#b8cebf;line-height:1.7;margin:.4rem 0 0;}
.brief-note{padding:1.35rem 1.4rem;border-radius:15px;border:1px solid #426b51;min-height:155px;background:#163326;margin:.6rem 0 1.2rem;}
.brief-note.pine{background:linear-gradient(145deg,#1b3b2c,#12271f);}
.brief-note.moss{background:linear-gradient(145deg,#214335,#172e27);}
.brief-note.sage{background:linear-gradient(145deg,#2c4c3b,#1d362c);}
.brief-note.gold{background:linear-gradient(145deg,#3b3627,#2c291e);border-color:#6a6140;}
.brief-note-label{font-size:.68rem;font-weight:800;letter-spacing:.14em;color:#c9edce;line-height:1.5;}
.brief-note p{margin:.7rem 0 0;color:#e2f0e5!important;line-height:1.7;font-size:.91rem;}
/* Read-only tables use real HTML, keeping them truly dark across browsers */
.kinetic-table-scroll{border:1px solid #426650!important;background:#10251f!important;border-radius:14px!important;margin:.9rem 0 1.6rem!important;overflow-x:auto!important;}
.kinetic-table{font-family:'DM Sans',sans-serif;min-width:650px;color:#e9f7ec!important;font-size:.85rem!important;}
.kinetic-table thead th{background:#234434!important;color:#e0f2e4!important;padding:18px!important;font-size:.69rem!important;text-transform:uppercase;letter-spacing:.07em!important;}
.kinetic-table td{background:#12291f;color:#eff9ef;border-color:#2c4838!important;padding:17px 18px!important;line-height:1.6!important;}
.kinetic-table tbody tr:nth-child(even) td{background:#193529!important;}
.kinetic-table tbody tr:hover td{background:#274b37!important;}
.kinetic-table td.cell-emphasis{font-weight:800;color:#bceec5!important;}
/* Market signal cards */
.content-label{color:#b2d5b6!important;letter-spacing:.09em;font-size:.72rem;margin:1rem 0;}
.signal-card{border:1px solid #3c654a;background:linear-gradient(135deg,#1b392d,#112720);padding:clamp(1.25rem,2.5vw,2rem);border-radius:17px;margin:1.8rem 0 .5rem;}
.signal-top{display:flex;align-items:center;gap:.75rem;flex-wrap:wrap;}
.signal-number{color:#d7f5db;font:800 1rem Manrope,sans-serif;}
.signal-sector{padding:6px 11px;background:#305d3d;color:#e4f6e5;border-radius:999px;font-size:.70rem;font-weight:700;}
.signal-date{margin-left:auto;font-size:.75rem;color:#bbd5c2;}
.signal-card h3{font:800 clamp(1.2rem,2vw,1.5rem)/1.35 Manrope,sans-serif;color:#f2fbf3!important;letter-spacing:-.028em;margin:1.2rem 0 1.45rem;}
.signal-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;align-items:stretch;}
.signal-pane{padding:1.1rem 1rem;border-radius:12px;min-height:170px;}
.signal-pane.fact{background:#173d2c;}.signal-pane.meaning{background:#24513c;}.signal-pane.question{background:#345b44;}
.signal-pane h4{font-size:.78rem;font-weight:800;letter-spacing:.035em;color:#ddf5df!important;margin:0 0 .6rem;}
.signal-pane p{color:#e0ede1!important;font-size:.85rem;line-height:1.67;margin:0;}
.signal-source{margin:1.2rem 0 0;font-size:.74rem;color:#9fbca5;letter-spacing:.035em;line-height:1.65;}
.signal-source a{color:#d1f4d8!important;font-weight:600;}
/* Export preview is a document, not an edit box */
.brief-preview{background:linear-gradient(135deg,#1a382a,#112921)!important;border:1px solid #456d50;border-radius:14px;padding:1.55rem 1.7rem;max-height:460px;overflow-y:auto;margin:.8rem 0 1.4rem;}
.brief-preview pre{font:500 .86rem/1.82 ui-monospace,Menlo,Consolas,monospace;color:#e7f5ea!important;white-space:pre-wrap;overflow-wrap:anywhere;margin:0;}
.main-intro{margin:0 0 1.5rem;}
.main-intro .page-title{font-size:clamp(1.85rem,3.7vw,2.8rem);margin:.45rem 0 .9rem;}
.main-intro .page-desc{max-width:850px;color:#c4d7c8;font-size:1rem;line-height:1.8;}
.glass-card{min-height:168px!important;border-color:#3b5b49!important;border-radius:15px!important;background:linear-gradient(145deg,#19382c,#102720)!important;}
.glass-card .card-value{overflow-wrap:anywhere;line-height:1.34;font-size:1.13rem;}
[data-testid="stPlotlyChart"]{background:linear-gradient(145deg,#11271f,#0d211f);border:1px solid #335440;border-radius:15px;padding:.8rem!important;margin:0 0 1.1rem;}
@media(max-width:1100px){.welcome-stage{grid-template-columns:minmax(0,1fr) minmax(290px,.9fr);gap:1rem;padding:2rem;}.welcome-headline{font-size:clamp(2.7rem,4.9vw,4.4rem);}.constellation{height:340px;}}
@media(max-width:850px){.signal-grid{grid-template-columns:1fr;}.signal-pane{min-height:unset;}.area-card{min-height:230px;}}
@media(max-width:760px){.welcome-stage{grid-template-columns:1fr;padding:1.7rem;gap:0;}.kinetic-brand{font-size:clamp(3rem,12vw,4.8rem);letter-spacing:.07em;}.kinetic-brand-subtitle{font-size:.62rem;letter-spacing:.12em;}.welcome-headline{font-size:clamp(2.55rem,9vw,4.2rem);}.constellation{height:315px;max-width:470px;}.feature-pill{display:none;}.brief-note{min-height:unset;}}
@media(prefers-reduced-motion:reduce){.mesh-lines line,.mesh-nodes .mesh-node{animation:none!important;}.mesh-pulses{display:none!important;}}


.check-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:1.1rem 0 1.7rem;}
.check-card{background:linear-gradient(135deg,#1a3b2d,#122a24);border:1px solid #426950;border-radius:13px;padding:1.3rem;}
.check-card h4{font:800 .88rem/1.5 Manrope,sans-serif;color:#dff3df;margin:0 0 .5rem;}
.check-card p{font-size:.86rem;line-height:1.65;color:#d6e9d9;margin:0;}
@media(max-width:780px){.check-grid{grid-template-columns:1fr;}}

.area-card{box-sizing:border-box;min-height:275px;}
.brief-note.compact{min-height:0;padding:1.1rem 1.4rem;margin-bottom:1.1rem;}
.brief-note.compact p{margin-top:.35rem;}
.signal-pane{min-height:145px;}

/* DEPLOYMENT-HARDENED WIDGET THEME (v4).
   Native .streamlit/config.toml does the primary work. The rules below catch
   alternate BaseWeb/popover structure across hosted Streamlit versions. */
html,body,[data-testid="stAppViewContainer"],.stApp{color-scheme:dark!important;}
[data-testid="stAppViewContainer"]{background:#091815!important;}
[data-testid="stSidebar"]{background:#0d241d!important;}
[data-testid="stSelectbox"] [data-baseweb="select"],
[data-testid="stMultiSelect"] [data-baseweb="select"],
[data-baseweb="select"] > div,
[data-baseweb="select"] [role="combobox"],
[data-testid="stTextInput"] [data-baseweb="base-input"],
[data-testid="stTextArea"] [data-baseweb="textarea"],
[data-testid="stNumberInput"] [data-baseweb="base-input"],
[data-testid="stDateInput"] [data-baseweb="base-input"],
[data-baseweb="input-container"],
[data-baseweb="base-input"]{
 background-color:#17352a!important;color:#edf8ef!important;
 border-color:#42684d!important;box-shadow:none!important;
}
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input,
[data-testid="stDateInput"] input,
[data-testid="stSelectbox"] input,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
textarea,input[type="text"],input[type="number"],input[type="date"]{
 background-color:#17352a!important;color:#edf8ef!important;
 -webkit-text-fill-color:#edf8ef!important;caret-color:#c9f3d5!important;
}
input::placeholder,textarea::placeholder{color:#acc7b7!important;opacity:1!important;}
/* BaseWeb renders some menus outside the selectbox element in a portal. */
[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="popover"] [role="listbox"],
[data-baseweb="menu"],
[data-baseweb="menu"] ul,
[role="listbox"],
ul[role="listbox"] {
  background:#153226!important;
  color:#edf8ef!important;
  border-color:#497454!important;
}
[data-baseweb="popover"] li,
[data-baseweb="popover"] [role="option"],
[role="listbox"] [role="option"],
li[role="option"] {
  color:#edf8ef!important;
  background:#153226!important;
  -webkit-text-fill-color:#edf8ef!important;
}
[data-baseweb="popover"] li:hover,
[role="option"][aria-selected="true"],
[role="option"][data-highlighted="true"],
[role="option"]:hover {background:#2f5d43!important;color:#fff!important;}
[data-baseweb="select"] svg,[data-baseweb="input"] svg{fill:#c6e8d2!important;color:#c6e8d2!important;}
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p,
[data-testid="stSelectbox"] label,
[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label,
[data-testid="stDateInput"] label{
 color:#dff2e4!important;
}
/* Secondary native controls, if a hosted frontend renders them separately. */
[data-baseweb="calendar"],
[data-baseweb="calendar"] > div,
[data-baseweb="datepicker"],
[data-baseweb="timepicker"],
[data-baseweb="file-uploader"],
[data-testid="stFileUploader"] section,
[data-testid="stFileUploaderDropzone"]{
 background-color:#17352a!important;color:#effaef!important;border-color:#42684d!important;
}
[data-baseweb="calendar"] button,
[data-baseweb="calendar"] span,
[data-baseweb="calendar"] div,
[data-testid="stFileUploader"] *{
 color:#e5f7e9!important;
}
/* Welcome: side-by-side Streamlit columns rather than SVG inside Markdown. */
.welcome-headline{font-family:Manrope,sans-serif!important;font-size:clamp(3rem,5.4vw,5.25rem)!important;font-weight:800!important;letter-spacing:-.058em!important;line-height:1.08!important;color:#f1faf2!important;margin:1rem 0 .95rem!important;} 
.welcome-headline em{font-style:normal;color:#cbf7d3;} 
.welcome-introduction{color:#d5e7d8!important;font-size:1.14rem!important;line-height:1.86!important;max-width:520px;} 
[data-testid="stImage"] img{border-radius:20px;max-width:100%;height:auto;}
@media(max-width:820px){.welcome-headline{font-size:clamp(2.35rem,7.5vw,3.9rem)!important;}}

.cta-kicker{margin:.1rem 0 .55rem;text-align:center;color:#d8f3de;font-size:.72rem;font-weight:800;letter-spacing:.2em;}

/* KINETIC v6 — restrained editorial finish. Scoped to the welcome and entry CTA. */
.kinetic-brand:not(.compact){
  font-size:clamp(4.0rem,8.1vw,7.4rem)!important;
  font-weight:800!important;
  letter-spacing:.115em!important;
  line-height:1.02!important;
  margin:.55rem 0 .35rem!important;
  text-shadow:0 2px 30px rgba(140,234,170,.09);
}
.kinetic-brand-subtitle{
  font-size:clamp(.66rem,.85vw,.81rem)!important;
  font-weight:800!important;
  letter-spacing:.185em!important;
  line-height:1.65!important;
  color:#c4edcf!important;
  margin-bottom:1.35rem!important;
}
.welcome-headline{
  font-family:Manrope,'DM Sans',sans-serif!important;
  font-size:clamp(2.5rem,4.2vw,4.35rem)!important;
  line-height:1.16!important;
  font-weight:800!important;
  color:#f6fdf7!important;
  letter-spacing:-.057em!important;
  margin:1.05rem 0 1.25rem!important;
  text-wrap:balance;
}
.welcome-headline em{color:#b8f0c5!important;font-style:normal!important;}
.welcome-introduction{
  font-size:1.065rem!important;
  line-height:1.85!important;
  max-width:510px!important;
  color:#d3e6d8!important;
}
.cta-kicker{
  color:#c7e8cf!important;
  font-size:.70rem!important;
  line-height:1.5!important;
  font-weight:800!important;
  letter-spacing:.205em!important;
  margin:0 0 .65rem!important;
  text-align:center!important;
}
/* Streamlit renders button text in p/span elements, so style descendants explicitly. */
div[class*="st-key-enter_kinetic"] button{
  background:linear-gradient(105deg,#b3e9c3 0%,#c8f2d1 50%,#dffbe7 100%)!important;
  border:1px solid #dffbe7!important;
  color:#103425!important;
  border-radius:13px!important;
  min-height:3.85rem!important;
  box-shadow:0 11px 34px rgba(84,207,137,.26), inset 0 1px 0 rgba(255,255,255,.56)!important;
  font-weight:800!important;
  transition:transform .16s ease,box-shadow .16s ease,filter .16s ease!important;
}
div[class*="st-key-enter_kinetic"] button *{
  color:#103425!important;
  -webkit-text-fill-color:#103425!important;
  font-size:1.08rem!important;
  font-weight:800!important;
  letter-spacing:.02em!important;
}
div[class*="st-key-enter_kinetic"] button:hover{
  background:linear-gradient(105deg,#cff9da 0%,#e1ffe9 55%,#f1fff2 100%)!important;
  box-shadow:0 15px 38px rgba(80,204,125,.32),inset 0 1px 0 rgba(255,255,255,.65)!important;
  transform:translateY(-2px)!important;
}
div[class*="st-key-enter_kinetic"] button:focus-visible{
  outline:3px solid #e1ffe6!important;
  outline-offset:3px!important;
}
[data-testid="stImage"] img{border:1px solid rgba(136,208,157,.24)!important;box-shadow:0 18px 44px rgba(0,0,0,.20)!important;}
@media(max-width:900px){
  .kinetic-brand:not(.compact){font-size:clamp(3rem,10.5vw,5rem)!important;letter-spacing:.065em!important;}
  .welcome-headline{font-size:clamp(2.25rem,4.65vw,3.25rem)!important;}
  .welcome-introduction{font-size:1rem!important;}
}
@media(max-width:600px){
  .kinetic-brand-subtitle{font-size:.65rem!important;letter-spacing:.085em!important;}
  .welcome-headline{font-size:clamp(2.05rem,8.5vw,2.85rem)!important;letter-spacing:-.047em!important;}
  .cta-kicker{font-size:.62rem!important;letter-spacing:.14em!important;}
  div[class*="st-key-enter_kinetic"] button{min-height:3.65rem!important;}
}
@media(prefers-reduced-motion:reduce){
  div[class*="st-key-enter_kinetic"] button{transition:none!important;transform:none!important;}
}


/* KINETIC v7 — final interface polish. Accessible state-specific overrides.
   Streamlit theme controls the base; these rules cover BaseWeb portal and
   expander interaction states which can otherwise flash white on click. */
:root{
  --k-bg:#091815;
  --k-surface:#143126;
  --k-surface-hover:#234735;
  --k-surface-active:#2c5840;
  --k-ink:#edf8ef;
  --k-muted:#bdd6c5;
  --k-accent:#baf0c9;
  --k-border:#42684d;
}
::selection{background:#437c58;color:#f7fff8;}

/* Expanders (including Assess Value: Change Building and Optional Comparison).
   These are DETAILS/SUMMARY, not Streamlit selectboxes. */
[data-testid="stExpander"]{
  background:linear-gradient(145deg,#112a22,#0d211b)!important;
  border:1px solid #3d634c!important;
  border-radius:16px!important;
  overflow:hidden!important;
  box-shadow:0 5px 18px rgba(0,0,0,.10)!important;
  margin:.55rem 0 1.05rem!important;
}
[data-testid="stExpander"] details,
[data-testid="stExpander"] details > summary,
[data-testid="stExpander"] summary,
[data-testid="stExpander"] [data-testid="stExpanderHeader"]{
  background:#153329!important;
  color:#f1fbf4!important;
  -webkit-text-fill-color:#f1fbf4!important;
  border-color:#3d634c!important;
}
[data-testid="stExpander"] details > summary{
  padding:1rem 1.2rem!important;
  min-height:3.25rem!important;
  border-radius:15px!important;
  transition:background-color .16s ease,border-color .16s ease!important;
  font-weight:700!important;
}
[data-testid="stExpander"] details > summary:hover,
[data-testid="stExpander"] details > summary:active,
[data-testid="stExpander"] details > summary:focus,
[data-testid="stExpander"] details > summary:focus-visible,
[data-testid="stExpander"] details > summary[aria-expanded="true"],
[data-testid="stExpander"] details[open] > summary{
  background:#28513b!important;
  color:#ffffff!important;
  -webkit-text-fill-color:#ffffff!important;
}
[data-testid="stExpander"] details > summary:focus-visible{outline:2px solid #b6eac4!important;outline-offset:-3px!important;}
[data-testid="stExpander"] details > summary :is(p,span,div,svg),
[data-testid="stExpander"] [data-testid="stExpanderToggleIcon"],
[data-testid="stExpander"] [data-testid="stExpanderHeader"] :is(p,span,div,svg){
  color:#f2fbf3!important;
  fill:currentColor!important;
  -webkit-text-fill-color:#f2fbf3!important;
}
[data-testid="stExpander"] details[open] > div:not(summary){
  background:linear-gradient(160deg,#102820,#0e221c)!important;
  color:#edf8ef!important;
}

/* Dropdowns, open menus, selected/highlighted rows and multiselect chips. */
[data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stSelectbox"] [data-baseweb="select"] > div:hover,
[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within,
[data-testid="stMultiSelect"] [data-baseweb="select"] > div,
[data-testid="stMultiSelect"] [data-baseweb="select"] > div:hover,
[data-testid="stMultiSelect"] [data-baseweb="select"] > div:focus-within,
[data-baseweb="select"] [role="combobox"],
[data-baseweb="select"] [role="combobox"]:focus,
[data-baseweb="select"] [aria-expanded="true"]{
  background-color:#17392b!important;
  color:#f0faf3!important;
  border-color:#5e9971!important;
  -webkit-text-fill-color:#f0faf3!important;
  box-shadow:none!important;
}
[data-testid="stSelectbox"] [data-baseweb="select"] :is(span,div,p),
[data-testid="stMultiSelect"] [data-baseweb="select"] :is(span,p),
[data-baseweb="select"] [aria-selected="true"] :is(span,div,p){
  color:#f0faf3!important;
  -webkit-text-fill-color:#f0faf3!important;
}
[data-baseweb="popover"],
[data-baseweb="popover"] [role="listbox"],
[data-baseweb="popover"] [role="option"],
[data-baseweb="menu"],
[data-baseweb="menu"] [role="option"]{
  background-color:#143126!important;
  color:#f0faf3!important;
  -webkit-text-fill-color:#f0faf3!important;
}
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="popover"] [role="option"]:focus,
[data-baseweb="popover"] [role="option"][aria-selected="true"],
[data-baseweb="popover"] [role="option"][data-highlighted="true"],
[data-baseweb="menu"] [role="option"]:hover,
[data-baseweb="menu"] li:hover{
  background-color:#2e5b41!important;
  color:#ffffff!important;
  -webkit-text-fill-color:#ffffff!important;
}
[data-baseweb="tag"]{
  background:#2e5a40!important;
  border:1px solid #4b8060!important;
  color:#f0fff3!important;
}
[data-baseweb="tag"] :is(span,svg){color:#f0fff3!important;fill:currentColor!important;}

/* Numeric and text fields: retain green backgrounds on hover, click and focus. */
[data-testid="stNumberInput"] [data-baseweb="input"],
[data-testid="stTextInput"] [data-baseweb="input"],
[data-testid="stTextArea"] [data-baseweb="textarea"],
[data-testid="stDateInput"] [data-baseweb="input"],
[data-baseweb="base-input"]:focus-within,
[data-baseweb="textarea"]:focus-within{
  background:#17392b!important;
  color:#f0faf3!important;
  border-color:#78b98b!important;
  box-shadow:none!important;
}
[data-testid="stNumberInput"] button,
[data-testid="stNumberInput"] button:hover,
[data-testid="stNumberInput"] button:focus{
  background:#214535!important;
  color:#e8f7ed!important;
  border-color:#436c51!important;
}
[data-testid="stForm"]{
  background:linear-gradient(145deg,#143126,#10271f)!important;
  border:1px solid #3b624c!important;
  border-radius:17px!important;
  padding:1.2rem!important;
}
[data-testid="stWidgetLabel"] :is(p,span),
[data-testid="stExpander"] label :is(p,span){color:#e2f1e6!important;}

/* Cards and key data: stronger hierarchy without visual noise. */
.main .block-container{max-width:1320px;padding-bottom:5rem;}
.main-intro{padding:.3rem 0 .5rem;margin-bottom:1.65rem!important;}
.main-intro .page-title{font-size:clamp(2rem,3.75vw,3rem)!important;line-height:1.18!important;letter-spacing:-.05em!important;}
.main-intro .page-desc{max-width:880px;font-size:1.03rem!important;line-height:1.8!important;}
.portal-eyebrow,.eyebrow{letter-spacing:.13em!important;color:#aeddbb!important;}
[data-testid="stMetric"]{
  background:linear-gradient(145deg,#173b2c 0%,#10281f 100%)!important;
  border:1px solid #3e6850!important;
  border-radius:17px!important;
  min-height:128px!important;
  padding:19px 20px!important;
  box-shadow:0 7px 21px rgba(0,0,0,.11)!important;
}
[data-testid="stMetricLabel"] :is(p,span){color:#bddac5!important;line-height:1.55!important;}
[data-testid="stMetricValue"]{color:#f0fff3!important;letter-spacing:-.04em!important;}
[data-testid="stPlotlyChart"]{
  background:linear-gradient(155deg,#142d24,#0b211c)!important;
  border:1px solid #3a5e47!important;
  border-radius:17px!important;
  padding:1.15rem!important;
  box-shadow:0 8px 22px rgba(0,0,0,.12)!important;
}
.area-card{
  border-color:#558064!important;
  border-radius:19px!important;
  box-shadow:0 14px 30px rgba(0,0,0,.14)!important;
}
.area-card.pine{background:linear-gradient(150deg,#1a4434,#10281f)!important;}
.area-card.moss{background:linear-gradient(150deg,#28543c,#163025)!important;}
.area-card.sage{background:linear-gradient(150deg,#37634b,#203c30)!important;}
.area-card h3{font-size:clamp(1.3rem,1.9vw,1.64rem)!important;}
.area-card p{line-height:1.78!important;}
.step-heading{gap:1.1rem!important;padding-top:1.4rem!important;margin-top:1.65rem!important;}
.step-index{
  min-width:3.05rem;text-align:center;
  background:linear-gradient(145deg,#2a6140,#1b3f2f)!important;
  border-color:#5c936c!important;
  color:#e3f8e9!important;
  border-radius:13px!important;
  font-size:1.1rem!important;
}
.signal-number{font-size:1.14rem!important;color:#e6f9eb!important;}
.signal-card,.topic-card,.brief-note,.check-card,.glass-card{
  box-shadow:0 8px 25px rgba(0,0,0,.10)!important;
}
.signal-pane.fact{background:linear-gradient(150deg,#1a4430,#153529)!important;}
.signal-pane.meaning{background:linear-gradient(150deg,#28593f,#1c4231)!important;}
.signal-pane.question{background:linear-gradient(150deg,#356349,#24513d)!important;}
.kinetic-table-scroll{box-shadow:0 7px 23px rgba(0,0,0,.13)!important;}
.kinetic-table tbody tr:hover td{background:#2c5740!important;}
.nav-area-name{line-height:1.6;}
.navigation-divider{margin:1.4rem 0 1.8rem!important;}

/* Native buttons retain visible labels, particularly on selected/hovered tabs. */
.stButton > button[kind="primary"] :is(p,span,strong),
.stDownloadButton > button[kind="primary"] :is(p,span,strong){
  color:#092319!important;
  -webkit-text-fill-color:#092319!important;
  font-weight:800!important;
}
.stButton > button[kind="secondary"] :is(p,span,strong),
.stDownloadButton > button[kind="secondary"] :is(p,span,strong){color:#ebf6ed!important;-webkit-text-fill-color:#ebf6ed!important;}
.stButton > button:disabled :is(p,span,strong){color:#eaf8ec!important;-webkit-text-fill-color:#eaf8ec!important;}
.stButton > button,.stDownloadButton > button{transition:background-color .16s ease,border-color .16s ease,box-shadow .16s ease!important;}
.stButton > button:not(:disabled):hover,.stDownloadButton > button:not(:disabled):hover{box-shadow:0 5px 18px rgba(87,188,119,.16)!important;}

@media(max-width:850px){
  .main .block-container{padding-left:1rem;padding-right:1rem;}
  .signal-card{padding:1.25rem!important;}
  .signal-pane{min-height:0!important;}
  .area-card{min-height:245px!important;}
  .kinetic-table th,.kinetic-table td{padding:13px!important;}
}
@media(prefers-reduced-motion:reduce){
 .stButton > button,.stDownloadButton > button,[data-testid="stExpander"] details > summary{transition:none!important;}
}


/* KINETIC v7 — final contrast, interaction and spacing refinement.
   Target the actual deployed Streamlit/BaseWeb structures, including OPEN,
   FOCUSED and SELECTED states (not only the resting controls). */
:root {
  --kin-field:#15352a;
  --kin-field-hover:#1d4334;
  --kin-field-active:#2b5941;
  --kin-field-border:#52785e;
  --kin-focus:#a8e8bc;
  --kin-foreground:#effaf1;
}

/* Expander headers in Streamlit are SUMMARY elements. Prevent them from
   turning white on click, hover, keyboard focus or when expanded. */
[data-testid="stExpander"],
details[data-testid="stExpander"],
[data-testid="stExpander"] > details,
[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
  background-color:#122b23!important;
  color:var(--kin-foreground)!important;
  border-color:#3a634b!important;
}
[data-testid="stExpander"] summary,
details[data-testid="stExpander"] > summary {
  background-color:#18382b!important;
  color:var(--kin-foreground)!important;
  border-radius:12px!important;
  box-shadow:none!important;
  transition:background-color .16s ease, border-color .16s ease!important;
}
[data-testid="stExpander"] summary:hover,
[data-testid="stExpander"] summary:focus,
[data-testid="stExpander"] summary:active,
[data-testid="stExpander"] summary:focus-visible,
[data-testid="stExpander"] details[open] > summary,
details[data-testid="stExpander"][open] > summary,
[data-testid="stExpander"] summary[aria-expanded="true"] {
  background-color:#27553c!important;
  color:#fff!important;
  box-shadow:inset 0 0 0 1px rgba(163,226,183,.28)!important;
}
[data-testid="stExpander"] summary:focus-visible,
details[data-testid="stExpander"] > summary:focus-visible {
  outline:2px solid var(--kin-focus)!important;
  outline-offset:2px!important;
}
[data-testid="stExpander"] summary *,
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] summary svg,
details[data-testid="stExpander"] > summary * {
  color:#effaf1!important;
  -webkit-text-fill-color:#effaf1!important;
  fill:currentColor!important;
}
[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
  padding-top:1.25rem!important;
  padding-bottom:.9rem!important;
}

/* Native selector focus and expanded/selected states; these override the
   white highlight introduced by some versions of BaseWeb. */
[data-testid="stSelectbox"] [data-baseweb="select"]:focus-within > div,
[data-testid="stMultiSelect"] [data-baseweb="select"]:focus-within > div,
[data-testid="stSelectbox"] [role="combobox"]:focus,
[data-testid="stSelectbox"] [role="combobox"][aria-expanded="true"],
[data-testid="stNumberInput"] [data-baseweb="base-input"]:focus-within,
[data-testid="stTextInput"] [data-baseweb="base-input"]:focus-within,
[data-testid="stTextArea"] [data-baseweb="textarea"]:focus-within,
[data-testid="stDateInput"] [data-baseweb="base-input"]:focus-within {
  background-color:var(--kin-field-hover)!important;
  border-color:#89c9a0!important;
  color:var(--kin-foreground)!important;
  box-shadow:0 0 0 1px #89c9a0!important;
}
[data-baseweb="popover"] [role="option"],
[data-baseweb="menu"] [role="option"],
[data-baseweb="select"] [role="option"],
[role="listbox"] [role="option"] {
  background-color:var(--kin-field)!important;
  color:var(--kin-foreground)!important;
}
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="popover"] [role="option"][aria-selected="true"],
[data-baseweb="popover"] [role="option"][data-highlighted="true"],
[data-baseweb="menu"] [role="option"]:hover,
[data-baseweb="menu"] [role="option"][aria-selected="true"],
[data-baseweb="menu"] [role="option"][data-highlighted="true"],
[role="listbox"] [role="option"]:hover,
[role="listbox"] [role="option"][aria-selected="true"],
[role="listbox"] [role="option"][data-highlighted="true"],
[data-baseweb="select"] [aria-selected="true"],
[data-baseweb="select"] [data-highlighted="true"] {
  background-color:var(--kin-field-active)!important;
  color:#fff!important;
}
[data-baseweb="popover"] [role="option"] *,
[data-baseweb="menu"] [role="option"] *,
[role="listbox"] [role="option"] * {
  color:inherit!important;
  -webkit-text-fill-color:currentColor!important;
}

/* Other controls that often inherit browser-white focus/hover styling */
[data-testid="stNumberInput"] button,
[data-testid="stDateInput"] button {
  background-color:#204333!important;
  color:#edf8f0!important;
  border-color:#4c7658!important;
}
[data-testid="stNumberInput"] button:hover,
[data-testid="stDateInput"] button:hover {
  background-color:#315e44!important;
  color:#fff!important;
}
[data-testid="stRadio"] label:hover,
[data-testid="stCheckbox"] label:hover {
  background-color:rgba(127,200,146,.07)!important;
  border-radius:9px!important;
}

/* Editorial spacing and contrast, shared across all three work areas */
[data-testid="stMainBlockContainer"] {max-width:1320px!important;}
.main-intro{margin-bottom:1.85rem!important;}
.main-intro .page-title{letter-spacing:-.045em!important;line-height:1.16!important;}
.main-intro .page-desc{color:#c9e2cf!important;}
.navigation-divider{margin:1.35rem 0 1.9rem!important;}
div[class*="st-key-top_nav_"] button {
  border:1px solid #466a54!important;
  border-radius:12px!important;
  color:#e0f3e3!important;
  min-height:3.25rem!important;
  background:linear-gradient(145deg,#1a3b2d,#122b24)!important;
  transition:background-color .16s ease, border-color .16s ease!important;
}
div[class*="st-key-top_nav_"] button * {color:inherit!important;-webkit-text-fill-color:currentColor!important;}
div[class*="st-key-top_nav_"] button:not(:disabled):hover {
  background:linear-gradient(145deg,#28563b,#1b3c2e)!important;
  border-color:#a4dbb5!important;
}
div[class*="st-key-top_nav_"] button:disabled {
  background:linear-gradient(145deg,#3b7450,#285e40)!important;
  color:#fff!important;
  border-color:#95d1a9!important;
  opacity:1!important;
}
.step-heading{padding-top:1.35rem!important;margin-top:1.7rem!important;}
.step-index{
  border-radius:12px!important;
  color:#10281c!important;
  background:linear-gradient(135deg,#c6f5d4,#8fd4a5)!important;
  border:1px solid #bceccc!important;
  min-width:3.05rem!important;
  text-align:center!important;
  box-shadow:0 6px 22px rgba(67,157,101,.13)!important;
}
.kinetic-table-scroll{box-shadow:0 8px 32px rgba(0,0,0,.11)!important;}
.kinetic-table thead th{background:#26513a!important;color:#f0fff3!important;}
.kinetic-table tbody tr:hover td{background:#28503b!important;}
.area-card{box-shadow:0 14px 38px rgba(0,0,0,.12)!important;}
.area-number{font-size:.78rem!important;letter-spacing:.15em!important;color:#d2f7db!important;}
.glass-card,.brief-note,.signal-card,.check-card,[data-testid="stMetric"]{
  box-shadow:inset 0 1px 0 rgba(232,255,235,.045),0 8px 26px rgba(0,0,0,.10)!important;
}
.glass-card .card-value{color:#f2fff3!important;}
[data-testid="stPlotlyChart"] {border-color:#416d50!important;}
[data-testid="stCaptionContainer"] p {color:#bcd5c2!important;}

/* Modest, clearly attributable creator credit — never compete with the CTA */
.creator-credit{
  display:flex;
  flex-wrap:wrap;
  align-items:center;
  justify-content:center;
  gap:.5rem .9rem;
  margin:1.35rem auto .55rem;
  padding-top:1rem;
  color:#b6d7c1;
  font-family:'DM Sans',sans-serif;
}
.creator-credit span{font-size:.67rem;font-weight:700;letter-spacing:.2em;color:#a2c6ad!important;}
.creator-credit strong{font-size:.97rem;font-weight:700;letter-spacing:.03em;color:#e7ffed!important;}
@media(max-width:850px){
  .navigation-divider{margin:1rem 0 1.35rem!important;}
  div[class*="st-key-top_nav_"] button{min-height:3rem!important;}
  .creator-credit{margin-top:1.1rem;}
}
@media(prefers-reduced-motion:reduce){
  div[class*="st-key-top_nav_"] button,[data-testid="stExpander"] summary{transition:none!important;}
}

</style>
"""
