import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Custom Premium CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    
    /* CS Top Left Logo */
    .top-left-logo {
        position: fixed;
        top: 40px;
        left: 20px;
        font-size: 22px;
        font-weight: bold;
        color: #38bdf8;
        border: 2px solid #38bdf8;
        padding: 5px 15px;
        letter-spacing: 5px;
        z-index: 999;
    }

    /* Auth Card */
    .auth-container {
        background: rgba(255, 255, 255, 0.02);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #38bdf8;
        text-align: center;
    }

    input { background-color: #111 !important; color: #38bdf8 !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- Session State for Auth ---
if 'user_db' not in st.session_state:
    st.session_state.user_db = {} 
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- AUTHENTICATION PAGE ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    # Android Robot Center
    st.markdown("<center><img src='https://img.icons8.com/color/512/android-os.png' width='100'></center>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#38bdf8; letter-spacing:2px;'>RISKSHIELD PORTAL</h2>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔒 LOGIN", "📝 REGISTER"])
        
        with tab2:
            st.write("New Auditor Registration")
            reg_u = st.text_input("Create User ID", key="reg_u")
            reg_p = st.text_input("Create Security Key", type="password", key="reg_p")
            if st.button("REGISTER ACCOUNT"):
                if reg_u and reg_p:
                    st.session_state.user_db[reg_u] = reg_p
                    st.success("Account Created! Switch to Login tab.")
                else:
                    st.warning("Please fill all fields.")

        with tab1:
            st.write("Identity Verification")
            log_u = st.text_input("User ID", key="log_u")
            log_p = st.text_input("Security Key", type="password", key="log_p")
            if st.button("VERIFY & ENTER"):
                if log_u in st.session_state.user_db and st.session_state.user_db[log_u] == log_p:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Invalid Identity or Key.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    # CS Logo Top Left
    st.markdown('<div class="top-left-logo">C S</div>', unsafe_allow_html=True)
    
    t1, t2, t3 = st.columns([1, 2, 1])
    with t2:
        st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>RISK COMMAND CENTER</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888;'>CHARVI SRI | FORENSIC AUDIT COMMAND</p>", unsafe_allow_html=True)
    with t3:
        if st.button("SIGN OUT"):
            st.session_state.auth = False
            st.rerun()

    st.divider()

    # Risk Images (Using high-reliability links)
    st.markdown("### 🔍 Forensic Surveillance Metrics")
    i1, i2, i3 = st.columns(3)
    # Image 1: Network/Digital
    i1.image("https://www.shutterstock.com/image-vector/digital-cyber-security-background-shield-260nw-2127264803.jpg", caption="Neural Risk Mapping", use_container_width=True)
    # Image 2: Data/Analysis
    i2.image("https://www.shutterstock.com/image-photo/financial-business-graph-digital-interface-260nw-1383344660.jpg", caption="Transaction Anomaly", use_container_width=True)
    # Image 3: AI/Technology
    i3.image("https://www.shutterstock.com/image-photo/data-science-technology-concept-human-260nw-2180017121.jpg", caption="AI Forensic Scan", use_container_width=True)

    st.divider()
    
    # File Upload
    uploaded_file = st.file_uploader("Upload Forensic Audit Ledger (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Data Authenticated.")
        st.dataframe(df.head(20), use_container_width=True)
