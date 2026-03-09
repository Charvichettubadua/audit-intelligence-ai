import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# --- Premium Global CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    
    /* Login Box */
    .auth-card {
        background: rgba(255, 255, 255, 0.02);
        padding: 50px;
        border-radius: 20px;
        border: 1px solid #38bdf8;
        text-align: center;
        margin: auto;
    }
    
    /* Header Styles */
    .main-header {
        color: #38bdf8;
        font-weight: 800;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    /* CS Top Left Logo Style */
    .top-left-logo {
        font-size: 24px;
        font-weight: bold;
        color: #38bdf8;
        letter-spacing: 5px;
        border: 1px solid #38bdf8;
        padding: 5px 15px;
        display: inline-block;
    }

    input { background-color: #111 !important; color: #38bdf8 !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- LOGIN SCREEN ---
if not st.session_state.auth:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.5, 1])
    
    with c2:
        # Android Robot Logo Center
        st.markdown("<center><img src='https://cdn-icons-png.flaticon.com/512/11516/11516905.png' width='100'></center>", unsafe_allow_html=True)
        
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.markdown('<h2 class="main-header">SECURE AUTHENTICATION</h2>', unsafe_allow_html=True)
        st.markdown("<p style='color: #666;'>RiskShield AI Forensic Portal</p>", unsafe_allow_html=True)
        
        user_id = st.text_input("CORPORATE IDENTITY", key="uid", placeholder="charvisri")
        access_key = st.text_input("SECURITY KEY", type="password", key="akey", placeholder="••••••••")
        
        if st.button("VERIFY IDENTITY"):
            if user_id.strip() == "charvisri" and access_key.strip() == "charvi@2026":
                st.session_state.auth = True
                st.rerun()
            else:
                # Removed "Access Denied" -> Professional Warning
                st.warning("Credential mismatch. Please verify your Identity and Security Key.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    # Top Row: CS Logo Left | Empty Middle | Name Right
    t1, t2, t3 = st.columns([1, 2, 1])
    with t1:
        st.markdown('<div class="top-left-logo">C S</div>', unsafe_allow_html=True)
    with t2:
        st.markdown("<h2 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>RISK MONITORING CENTER</h2>", unsafe_allow_html=True)
    with t3:
        st.write(f"Auditor: **Charvi Sri**")
        if st.button("Sign Out"):
            st.session_state.auth = False
            st.rerun()

    st.divider()

    # Risk Images Row
    st.markdown("### 🔍 Forensic Surveillance Metrics")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1551288049-bbda48658a7d?w=400", caption="Anomalous Neural Mapping")
    i2.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="High-Risk Transaction Flow")
    i3.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", caption="AI Forensic Scan")

    st.divider()
    
    # Upload Section
    st.markdown("### 📥 Neural Data Ingestion")
    uploaded_file = st.file_uploader("Upload Forensic Audit Ledger (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Identity Authenticated. Data Analysis Stream Active.")
        st.dataframe(df.head(20), use_container_width=True)
