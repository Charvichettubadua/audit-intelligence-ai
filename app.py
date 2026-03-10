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

    /* Transforming Sign Out Button into a Black Hyperlink Style */
    div.stButton > button {
        background: none !important;
        border: none !important;
        color: #000000 !important; /* Pure Black */
        text-decoration: underline !important;
        padding: 0 !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: none !important;
        background-color: transparent !important;
    }
    
    /* Upload Section Label - Black Hyperlink Style on Blue Background for visibility */
    .stFileUploader label {
        color: #000000 !important; /* Pure Black Text */
        text-decoration: underline !important;
        font-weight: bold !important;
        background-color: #38bdf8; 
        padding: 8px 15px;
        border-radius: 5px;
        display: inline-block;
    }

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

# --- AUTHENTICATION PAGE (Keeping your original Login/Register) ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
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
        # SIGN OUT is now a Black Hyperlink
        if st.button("SIGN OUT"):
            st.session_state.auth = False
            st.rerun()

    st.divider()

    # Risk Images (Using direct high-res IDs)
    st.markdown("### 🔍 Forensic Surveillance Metrics")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping", use_container_width=True)
    i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Transaction Anomaly", use_container_width=True)
    i3.image("https://images.unsplash.com/photo-1558494949-ef010cbdcc51?w=400", caption="AI Forensic Scan", use_container_width=True)

    st.divider()
    
    # File Upload - Label is now a Black Hyperlink style
    uploaded_file = st.file_uploader("Upload Forensic Audit Ledger (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Data Authenticated.")
        st.dataframe(df.head(20), use_container_width=True)
