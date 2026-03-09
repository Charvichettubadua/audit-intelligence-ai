import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Luxury Corporate CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    
    /* Login Container */
    .auth-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #38bdf8;
        text-align: center;
        margin: auto;
        max-width: 450px;
    }
    
    /* Headers */
    .auth-header {
        color: #38bdf8;
        font-size: 28px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }
    
    /* Middle CS Logo */
    .cs-logo-main {
        font-size: 70px;
        font-weight: 200;
        color: #38bdf8;
        letter-spacing: 20px;
        text-align: center;
        margin: 20px 0;
    }

    /* Input Fields */
    input {
        background-color: #111 !important;
        color: #38bdf8 !important;
        border: 1px solid #333 !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- LOGIN SCREEN ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        # Android Robot Logo
        st.markdown("<center><img src='https://cdn-icons-png.flaticon.com/512/11516/11516905.png' width='100'></center>", unsafe_allow_html=True)
        
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.markdown('<div class="auth-header">SECURE AUTHENTICATION</div>', unsafe_allow_html=True)
        
        u = st.text_input("CORPORATE IDENTITY", placeholder="charvisri")
        p = st.text_input("SECURITY KEY", type="password", placeholder="••••••••")
        
        if st.button("VERIFY IDENTITY"):
            if u.strip() == "charvisri" and p.strip() == "charvi@2026":
                st.session_state.auth = True
                st.rerun()
            else:
                # No "Access Denied" - professional message instead
                st.warning("Credential Validation Required. Please ensure your key meets security standards.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    # Top Section: Android Logo | CS Middle | Name
    h1, h2, h3 = st.columns([1, 2, 1])
    with h1:
        st.image("https://cdn-icons-png.flaticon.com/512/11516/11516905.png", width=100)
    with h2:
        st.markdown('<div class="cs-logo-main">C S</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888;'>CHARVI SRI | ENTERPRISE AUDIT COMMAND</p>", unsafe_allow_html=True)
    with h3:
        st.write(f"Logged in: **Charvi Sri**")
        if st.button("Sign Out"):
            st.session_state.auth = False
            st.rerun()

    st.divider()

    # Risk Column Images
    st.markdown("### 🔍 Risk Surveillance")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1551288049-bbda48658a7d?w=400", caption="Neural Risk Mapping")
    i2.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Transaction Anomaly")
    i3.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", caption="Cyber Forensic Scan")

    st.divider()
    
    # Upload Section
    uploaded_file = st.file_uploader("📥 Ingest Forensic Data (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Identity Verified. Data Stream Active.")
        st.dataframe(df.head(20), use_container_width=True)
