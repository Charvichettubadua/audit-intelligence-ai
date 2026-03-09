import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Custom CSS for Black Hyperlinks & Design ---
st.markdown("""
    <style>
    /* Main Background */
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

    /* Transforming Sign Out Button into a Black Hyperlink */
    div.stButton > button {
        background: none !important;
        border: none !important;
        color: #000000 !important; /* Pure Black */
        text-decoration: underline !important;
        padding: 0 !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: none !important;
    }
    
    /* Upload Section - Black Hyperlink Style */
    .stFileUploader label {
        color: #000000 !important; /* Pure Black */
        text-decoration: underline !important;
        font-weight: bold !important;
        background-color: #38bdf8; /* Blue background to make black text visible */
        padding: 5px 10px;
        border-radius: 5px;
    }

    .auth-container {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #38bdf8;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State ---
if 'user_db' not in st.session_state:
    st.session_state.user_db = {} 
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- AUTHENTICATION PAGE ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<center><img src='https://img.icons8.com/color/512/android-os.png' width='100'></center>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#38bdf8; letter-spacing:2px;'>RISKSHIELD PORTAL</h2>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🔒 LOGIN", "📝 REGISTER"])
        
        with tab2:
            reg_u = st.text_input("Identity ID", key="reg_u")
            reg_p = st.text_input("Security Key", type="password", key="reg_p")
            if st.button("REGISTER"):
                if reg_u and reg_p:
                    st.session_state.user_db[reg_u] = reg_p
                    st.success("Identity Created! Go to Login.")
        with tab1:
            log_u = st.text_input("Identity ID", key="log_u")
            log_p = st.text_input("Security Key", type="password", key="log_p")
            if st.button("VERIFY"):
                if log_u in st.session_state.user_db and st.session_state.user_db[log_u] == log_p:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Authentication Pending.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- EXECUTIVE DASHBOARD ---
else:
    st.markdown('<div class="top-left-logo">C S</div>', unsafe_allow_html=True)
    
    t1, t2, t3 = st.columns([1, 2, 1])
    with t2:
        st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>RISK COMMAND CENTER</h1>", unsafe_allow_html=True)
    with t3:
        # Sign out is now a Black Hyperlink
        if st.button("Sign Out"):
            st.session_state.auth = False
            st.rerun()

    st.divider()

    # Images Section (Refreshed Links)
    st.markdown("### 🔍 Forensic Surveillance Metrics")
    i1, i2, i3 = st.columns(3)
    # Using specific high-res Unsplash IDs for reliability
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping")
    i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Transaction Anomaly")
    i3.image("https://images.unsplash.com/photo-1558494949-ef010cbdcc51?w=400", caption="AI Forensic Scan")

    st.divider()
    
    # Upload Section
    st.markdown("### 📥 Neural Data Ingestion")
    # File uploader label is now a Black Hyperlink style
    uploaded_file = st.file_uploader("Upload Forensic CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Identity Authenticated.")
        st.dataframe(df.head(20), use_container_width=True)
