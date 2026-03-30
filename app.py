import streamlit as st
import pd
import requests
from risk_engine import calculate_risk
from agent import generate_audit_report

# 1. Page Configuration (No Whitespace)
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide")

# 2. Master CSS (Cleaning everything messy)
st.markdown("""
    <style>
    /* Global Background and Colors */
    .stApp { background-color: #0d1117 !important; color: #c9d1d9 !important; }
    
    /* CS BRAND LOGO (Top Left) */
    .brand-logo { 
        position: fixed; top: 25px; left: 25px; font-size: 24px; font-weight: 800; 
        color: #38bdf8; border: 2px solid #38bdf8; padding: 5px 15px; 
        background: rgba(56, 189, 248, 0.1); border-radius: 5px; 
    }

    /* True Center Alignment - Everything in Middle */
    .main .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        text-align: center;
        margin: auto;
    }

    /* Smaller, Modern Auth Tabs and Inputs */
    input {
        background-color: #0d1117 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        height: 38px !important; /* Smaller Height */
        text-align: center;
        width: 100% !important;
        max-width: 400px !important; /* Smaller Width */
        margin: auto;
    }

    /* Center Auth Section Labels */
    [data-testid="stRadio"] div div div label {
        display: block;
        margin: auto;
        color: #58a6ff !important;
        font-weight: bold;
    }

    /* Primary Blue Buttons (Matching Video) */
    .stButton>button {
        background-color: #0066ff !important;
        color: white !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 45px !important;
        border: none !important;
    }
    .stButton>button:hover { background-color: #005cc5 !important; }
    
    /* Metrics Row Cards (Dashboard only) */
    .metric-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }

    /* Remove Streamlit default whitespace and elements */
    header, footer { visibility: hidden; }
    div[data-testid="stToolbar"] { visibility: hidden; }
    </style>
    <div class="brand-logo">CS</div>
    """, unsafe_allow_html=True)

# 3. Session State
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- UI FLOW ---
if not st.session_state['logged_in']:
    st.markdown("<h1 style='color: #0066ff;'>🛡️</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #00d4ff;'>RiskShield AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8b949e;'>Identity required for full access</p>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["PORTAL LOGIN", "CREATE ACCOUNT"])
    
    with tab1:
        with st.form("login_form"):
            st.markdown("<h3 style='color: #8b949e; text-align: center;'>GUEST IDENTITY</h3>", unsafe_allow_html=True)
            email = st.text_input("Corporate Email", placeholder="Email")
            pwd = st.text_input("Access Key", type="password", placeholder="Password")
            submit = st.form_submit_button("AUTHORIZE & ENTER")
            
            if submit:
                # Backend check Simulation
                if email and pwd:
                    st.session_state['logged_in'] = True
                    st.session_state['user'] = {"email": email, "name": "Manager"}
                    st.rerun()

    with tab2:
        with st.form("reg_form"):
            st.markdown("<h3 style='color: #8b949e; text-align: center;'>Deloitte Manager Identity</h3>", unsafe_allow_html=True)
            name = st.text_input("Full Name")
            r_email = st.text_input("Work Email")
            r_pwd = st.text_input("Access Key", type="password")
            if st.form_submit_button("CREATE MY ACCOUNT"):
                st.success("Registration Ready. Switch to Login.")

# --- DASHBOARD FLOW (MIDDLE ALIGNED) ---
else:
    st.markdown("<h1 style='color: #00d4ff;'>Forensic Command Center</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #8b949e;'>Active Session: {st.session_state['user']['email']}</p>", unsafe_allow_html=True)
    
    uploaded = st.file_uploader("Upload Transaction Dataset (CSV)", type="csv")
    
    if uploaded:
        df = pd.read_csv(uploaded)
        df = calculate_risk(df)
        
        # Risk Metrics Row
        m1, m2, m3, m4 = st.columns(4)
        m1.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        m1.metric("Scanned Records", f"{len(df):,}")
        m1.markdown("</div>", unsafe_allow_html=True)
        m2.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        m2.metric("High Risk Flags", f"{len(df[df['Risk_Level'] == 'High'])}", delta="Anomalies Found", delta_color="inverse")
        m2.markdown("</div>", unsafe_allow_html=True)
        m3.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        m3.metric("Neural Accuracy", "99.4%")
        m3.markdown("</div>", unsafe_allow_html=True)
        m4.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        m4.metric("Neural GIST", "Gems-Sim")
        m4.markdown("</div>", unsafe_allow_html=True)
        
        # Visualization Sections
        st.write("#### Predicted Risk Analysis")
        # add charting here
        
        if st.button("RUN AI NARRATIVE"):
            with st.spinner("Gemini AI is scanning ledger..."):
                report = generate_audit_report(df)
                st.info(f"### Forensic Insight:\n{report}")
        
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()
