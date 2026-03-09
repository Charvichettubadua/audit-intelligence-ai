import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Luxury Dark CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    
    /* CS Top Left Logo */
    .top-left-logo {
        position: absolute;
        top: -50px;
        left: 0px;
        font-size: 24px;
        font-weight: bold;
        color: #38bdf8;
        border: 2px solid #38bdf8;
        padding: 5px 15px;
        letter-spacing: 5px;
    }

    /* Auth Card Styling */
    .auth-card {
        background: rgba(255, 255, 255, 0.02);
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #38bdf8;
        text-align: center;
        margin-top: 50px;
    }

    /* Input Field Styling */
    .stTextInput>div>div>input {
        background-color: #111 !important;
        color: #38bdf8 !important;
        border: 1px solid #333 !important;
        border-radius: 8px !important;
    }

    /* Professional Warning (Replaces Access Denied) */
    .stWarning {
        background-color: rgba(255, 165, 0, 0.1) !important;
        color: orange !important;
        border: 1px solid orange !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- LOGIN SCREEN ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.5, 1])
    
    with c2:
        # Android Robot Center
        st.markdown("<center><img src='https://cdn-icons-png.flaticon.com/512/11516/11516905.png' width='100'></center>", unsafe_allow_html=True)
        
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='color: #38bdf8; letter-spacing: 2px;'>IDENTITY VERIFICATION</h2>", unsafe_allow_html=True)
        
        user_id = st.text_input("CORPORATE ID", key="user_id", placeholder="Enter Identity")
        secure_key = st.text_input("SECURITY KEY", type="password", key="secure_key", placeholder="Enter Key")
        
        if st.button("VERIFY"):
            if user_id.strip() == "" and secure_key.strip() == "":
                st.session_state.auth = True
                st.rerun()
            else:
                st.warning("⚠️ AUTHENTICATION PENDING: Please provide valid credentials to access the forensic engine.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    # Top Row: CS Logo Left | Empty Middle | Sign Out Right
    t1, t2, t3 = st.columns([1, 2, 1])
    with t1:
        st.markdown('<div class="top-left-logo">C S</div>', unsafe_allow_html=True)
    with t2:
        st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>RISK COMMAND CENTER</h1>", unsafe_allow_html=True)
    with t3:
        st.write(f"Auditor: **Charvi Sri**")
        if st.button("SIGN OUT"):
            st.session_state.auth = False
            st.rerun()

    st.divider()

    # Risk Images Row
    st.markdown("### 📊 Forensic Monitoring")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1551288049-bbda48658a7d?w=400", caption="Neural Risk Mapping")
    i2.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Anomalous Transaction Data")
    i3.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", caption="Cyber Surveillance")

    st.divider()
    
    # Upload Section
    st.markdown("### 📥 Data Ingestion")
    uploaded_file = st.file_uploader("Upload Forensic CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Identity Authenticated. Showing Ledger Stream:")
        st.dataframe(df.head(20), use_container_width=True)
