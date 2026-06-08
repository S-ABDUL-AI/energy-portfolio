import streamlit as st

st.set_page_config(
    page_title="Sherriff Abdul-Hamid | Energy Data Science Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── HIDE SIDEBAR AND STREAMLIT DEFAULTS ──────────────────────────────────────
st.markdown("""
<style>
    [data-testid="collapsedControl"] { display: none; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    .main { background-color: #f8f9fa; }

    .hero {
        background: linear-gradient(135deg, #1F3864 0%, #0d2137 100%);
        padding: 60px 40px;
        border-radius: 16px;
        margin-bottom: 40px;
        text-align: center;
    }
    .hero h1 {
        color: white;
        font-size: 2.6rem;
        font-weight: 700;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    .hero .title {
        color: #90CAF9;
        font-size: 1.15rem;
        margin-bottom: 16px;
        font-weight: 400;
    }
    .hero .tagline {
        color: #CFD8DC;
        font-size: 1.0rem;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
    }
    .section-heading {
        font-size: 1.35rem;
        font-weight: 700;
        color: #1F3864;
        border-bottom: 3px solid #1F3864;
        padding-bottom: 8px;
        margin-bottom: 24px;
        margin-top: 40px;
    }
    .app-card {
        background: white;
        border-radius: 14px;
        padding: 28px 24px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.09);
        border-top: 5px solid #1F3864;
        height: 100%;
        transition: box-shadow 0.2s;
    }
    .app-card:hover {
        box-shadow: 0 6px 20px rgba(0,0,0,0.14);
    }
    .app-card .icon {
        font-size: 2.2rem;
        margin-bottom: 12px;
    }
    .app-card h3 {
        color: #1F3864;
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 8px;
        line-height: 1.3;
    }
    .app-card .tag {
        display: inline-block;
        background: #E3F2FD;
        color: #1565C0;
        font-size: 0.72rem;
        font-weight: 600;
        padding: 3px 9px;
        border-radius: 20px;
        margin: 2px 2px 10px 0;
        letter-spacing: 0.02em;
        text-transform: uppercase;
    }
    .app-card .description {
        color: #555;
        font-size: 0.90rem;
        line-height: 1.55;
        margin-bottom: 18px;
    }
    .btn-primary {
        display: inline-block;
        background: #1F3864;
        color: white !important;
        padding: 9px 20px;
        border-radius: 8px;
        font-size: 0.88rem;
        font-weight: 600;
        text-decoration: none !important;
        margin-right: 8px;
        margin-bottom: 6px;
    }
    .btn-secondary {
        display: inline-block;
        background: transparent;
        color: #1F3864 !important;
        padding: 8px 18px;
        border-radius: 8px;
        font-size: 0.88rem;
        font-weight: 600;
        text-decoration: none !important;
        border: 2px solid #1F3864;
        margin-bottom: 6px;
    }
    .method-box {
        background: white;
        border-radius: 12px;
        padding: 28px 32px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        border-left: 5px solid #1F3864;
    }
    .method-box p {
        color: #444;
        font-size: 0.95rem;
        line-height: 1.7;
        margin-bottom: 12px;
    }
    .stat-card {
        background: white;
        border-radius: 12px;
        padding: 24px 20px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    }
    .stat-card .number {
        font-size: 2.0rem;
        font-weight: 700;
        color: #1F3864;
    }
    .stat-card .label {
        font-size: 0.82rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 4px;
    }
    .contact-card {
        background: linear-gradient(135deg, #1F3864 0%, #0d2137 100%);
        border-radius: 14px;
        padding: 36px 40px;
        text-align: center;
        margin-top: 40px;
    }
    .contact-card h3 {
        color: white;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .contact-card p {
        color: #CFD8DC;
        font-size: 0.95rem;
        margin-bottom: 20px;
    }
    .contact-link {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        color: white !important;
        padding: 10px 22px;
        border-radius: 8px;
        font-size: 0.90rem;
        font-weight: 600;
        text-decoration: none !important;
        margin: 4px 6px;
        border: 1px solid rgba(255,255,255,0.25);
    }
    .footer {
        text-align: center;
        color: #999;
        font-size: 0.80rem;
        padding: 30px 0 10px 0;
    }
</style>
""", unsafe_allow_html=True)


# ── SECTION 1: HERO HEADER ───────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="icon" style="font-size:2.8rem; margin-bottom:16px;">⚡</div>
    <h1>Sherriff Abdul-Hamid</h1>
    <div class="title">Data Scientist · Energy Economist · Public Infrastructure Analytics</div>
    <div class="tagline">
        Applying econometric modeling, machine learning, and expected-value optimization
        to the analytical problems that utility infrastructure teams face — from wildfire
        risk scoring and capital investment prioritization to demand forecasting and
        energy price shock transmission.
    </div>
</div>
""", unsafe_allow_html=True)


# ── SECTION 2: STATS ROW ─────────────────────────────────────────────────────
s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown("""<div class="stat-card">
        <div class="number">4</div>
        <div class="label">Energy Tools Built</div>
    </div>""", unsafe_allow_html=True)
with s2:
    st.markdown("""<div class="stat-card">
        <div class="number">14+</div>
        <div class="label">Years Applied Research</div>
    </div>""", unsafe_allow_html=True)
with s3:
    st.markdown("""<div class="stat-card">
        <div class="number">MSc</div>
        <div class="label">Economics — Energy Track</div>
    </div>""", unsafe_allow_html=True)
with s4:
    st.markdown("""<div class="stat-card">
        <div class="number">EB-1A</div>
        <div class="label">Extraordinary Ability</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ── SECTION 3: APP CARDS ─────────────────────────────────────────────────────
st.markdown('<div class="section-heading">⚡ Energy Data Science Portfolio</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="app-card">
        <div class="icon">🔥</div>
        <h3>California Grid Asset Risk & Wildfire Vulnerability Dashboard</h3>
        <span class="tag">Random Forest</span>
        <span class="tag">Risk Scoring</span>
        <span class="tag">CPUC RBDM</span>
        <span class="tag">Budget Optimization</span>
        <div class="description">
            AI-powered wildfire risk scoring across 600 simulated Southern California
            utility assets. Predicts failure probability using 9 environmental and
            operational features — wind exposure, vegetation density, fire proximity,
            asset age — and optimizes maintenance budgets to maximize risk reduction
            per dollar spent. Aligned to CPUC Risk-Based Decision-Making thresholds.
        </div>
        <a class="btn-primary" href="https://california-grid-asset-risk-wildfire-vulnerability-dashboard-hm.streamlit.app" target="_blank">🚀 Open App</a>
        <a class="btn-secondary" href="https://github.com/S-ABDUL-AI/California-Grid-Asset-Risk-Wildfire-Vulnerability-Dashboard" target="_blank">⌥ GitHub</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="app-card">
        <div class="icon">📊</div>
        <h3>Grid Investment Prioritization Engine</h3>
        <span class="tag">Benefit-Cost Analysis</span>
        <span class="tag">Portfolio Optimization</span>
        <span class="tag">Monte Carlo</span>
        <span class="tag">Efficient Frontier</span>
        <div class="description">
            Expected-value optimization engine for utility infrastructure capital
            decisions. Ranks 100 simulated investment projects by benefit-cost ratio,
            builds optimized portfolios under budget constraints, generates efficient
            frontier curves, and runs Monte Carlo uncertainty analysis with P10–P90
            confidence intervals. Aligned to CPUC RBDM benefit-cost filing requirements.
        </div>
        <a class="btn-primary" href="https://grid-investment-prioritization-engine.streamlit.app" target="_blank">🚀 Open App</a>
        <a class="btn-secondary" href="https://github.com/S-ABDUL-AI/grid-investment-prioritization-engine" target="_blank">⌥ GitHub</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown("""
    <div class="app-card">
        <div class="icon">📈</div>
        <h3>California Electric Load Forecasting & Grid Demand Planning</h3>
        <span class="tag">SARIMA</span>
        <span class="tag">Demand Forecasting</span>
        <span class="tag">EV Adoption</span>
        <span class="tag">Solar Integration</span>
        <div class="description">
            Time series demand forecasting and scenario planning for Southern California
            grid operations. SARIMA model forecasting load 12–24 months ahead across
            four service territory zones. Interactive scenario builder models how EV
            adoption rates, rooftop solar penetration, and commercial load growth shift
            peak demand and grid stress under conservative, base, and aggressive futures.
        </div>
        <a class="btn-primary" href="https://california-grid-demand-forecast.streamlit.app" target="_blank">🚀 Open App</a>
        <a class="btn-secondary" href="https://github.com/S-ABDUL-AI/california-grid-demand-forecast" target="_blank">⌥ GitHub</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="app-card">
        <div class="icon">🛢️</div>
        <h3>Oil Price Shock Transmission Dashboard</h3>
        <span class="tag">VAR / VECM</span>
        <span class="tag">Johansen Cointegration</span>
        <span class="tag">Impulse Response</span>
        <span class="tag">MSc Thesis Research</span>
        <div class="description">
            Interactive econometric research tool built directly from MSc Economics
            thesis research (KNUST, 2022). Explores how oil price shocks transmit
            into Ghana's public, domestic, and external debt using Johansen
            cointegration, VAR estimation, orthogonalized impulse response functions,
            and forecast error variance decomposition across 37 years of annual data.
        </div>
        <a class="btn-primary" href="https://oil-price-shock-transmission.streamlit.app" target="_blank">🚀 Open App</a>
        <a class="btn-secondary" href="https://github.com/S-ABDUL-AI/oil-price-shock-transmission" target="_blank">⌥ GitHub</a>
    </div>
    """, unsafe_allow_html=True)


# ── SECTION 4: METHODOLOGY NOTE ──────────────────────────────────────────────
st.markdown('<div class="section-heading">🧠 Methodology & Background</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="method-box">
    <p>
        My approach to utility data science is grounded in a background that most data
        scientists in this space do not have: formal graduate training in
        <strong>Energy Economics, Resource Economics, Oil & Gas Economics, and
        Environmental Economics & Policy</strong>, combined with 14+ years of applying
        econometric and machine learning methods to high-stakes resource allocation
        problems in public-sector and infrastructure contexts.
    </p>
    <p>
        The four tools in this portfolio apply the same analytical framework I have used
        across development economics — <strong>expected value optimization, benefit-cost
        analysis, uncertainty quantification, and causal inference</strong> — to the
        specific operational and regulatory problems that electric utilities face: wildfire
        risk, capital prioritization, demand forecasting, and energy price dynamics.
    </p>
    <p>
        Every tool uses simulated but realistic Southern California data, is built for
        non-technical executive audiences as well as technical reviewers, and is aligned
        to CPUC regulatory frameworks where applicable. All source code is open and
        available on GitHub.
    </p>
</div>
""", unsafe_allow_html=True)


# ── SECTION 5: CONTACT ───────────────────────────────────────────────────────
st.markdown("""
<div class="contact-card">
    <h3>Sherriff Abdul-Hamid</h3>
    <p>Data Scientist · Energy Economist · Public Infrastructure Analytics<br>
    Los Angeles, CA · U.S. Permanent Resident (EB-1A)</p>
    <a class="contact-link" href="https://www.linkedin.com/in/abdul-hamid-sherriff-08583354/" target="_blank">💼 LinkedIn</a>
    <a class="contact-link" href="https://github.com/S-ABDUL-AI" target="_blank">⌥ GitHub</a>
    <a class="contact-link" href="https://poverty360.org" target="_blank">🌍 poverty360.org</a>
    <a class="contact-link" href="mailto:sherriffhamid001@gmail.com">✉️ Email</a>
</div>
""", unsafe_allow_html=True)


# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built with Streamlit · All tools use simulated data for portfolio demonstration purposes ·
    Not official utility or regulatory data
</div>
""", unsafe_allow_html=True)
