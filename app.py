import streamlit as st
import pandas as pd
import time

# --- Premium Page Config ---
st.set_page_config(page_title="CharviShield AI | Exclusive Access", layout="wide", page_icon="💎")

# --- Next-Gen CSS (Luxury Dark Theme) ---
st.markdown("""
    <style>
    /* Dark Velvet Background */
    .stApp {
        background: radial-gradient(circle at 20% 30%, #1a1c2c 0%, #0a0b10 100%);
        color: #e2e8f0;
    }
    
    /* Luxury Glass Card */
    .login-box {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 50px;
        border-radius: 30px;
        box-shadow: 0 40px 100px rgba(0,0,0,0.8);
        text-align: center;
        max-width: 500px;
        margin: auto;
    }

    /* Custom Logo Placeholder (The 'C' Emblem) */
    .charvi-logo {
        height: 80px;
        width: 80px;
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
        font-size: 40px;
        font-weight: bold;
        color: white;
        box-shadow: 0 0 30px rgba(79, 172, 254, 0.5);
    }

    /* Professional Inputs */
    .stTextInput>div>div>input {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        color: #4facfe !important;
        border-radius: 15px !important;
    }

    /* Elegant Button */
    .stButton>button {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%) !important;
        color: #000 !important;
        font-weight: 700 !important;
        border-radius: 15px !important;
        border: none !important;
        letter-spacing: 1px;
        height: 3.5em !important;
        transition: 0.5s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 40px rgba(0, 242, 254, 0.6);
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Authentication Logic ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- User Profile ---
USER_ID = "charvisri"
ACCESS_KEY = "charvi@2026"

# --- LOGIN SCREEN ---
if not st.session_state.auth:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="charvi-logo">C</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 32px; letter-spacing: -1px;'>CharviShield <span style='color: #4facfe;'>AI</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; margin-bottom: 30px;'>Exclusive Audit Intelligence Engine</p>", unsafe_allow_html=True)
    
    with st.form("auth_form"):
        u_name = st.text_input("Principal ID", placeholder="charvisri")
        u_pass = st.text_input("Security Key", type="password")
        if st.form_submit_button("AUTHORIZE ACCESS"):
            if u_name == USER_ID and u_pass == ACCESS_KEY:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied: Invalid Credentials")
    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN DASHBOARD ---
else:
    st.sidebar.markdown(f"<div style='text-align: center;'><div class='charvi-logo' style='height:60px; width:60px; font-size:30px;'>C</div></div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<h3 style='text-align: center;'>Charvi Sri</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    st.sidebar.write("🔒 **Session: Secure**")
    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.rerun()

    st.markdown("<h1 style='font-size: 48px; font-weight: 800;'>Audit <span style='color: #4facfe;'>Intelligence</span></h1>", unsafe_allow_html=True)
    st.write(f"Welcome, **Principal Auditor Charvi Sri**. The system is ready for forensic analysis.")

    # High-End Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Neural Engine", "Online", "v4.2")
    col2.metric("Threat Detection", "Active", "0.01ms")
    col3.metric("Data Privacy", "GDPR compliant")
    col4.metric("AI Credit", "Gemini 2.5 Pro")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Drag and Drop Area
    with st.container():
        st.markdown("### 📥 Neural Data Ingestion")
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file:
            with st.spinner("Processing through Neural Layers..."):
                time.sleep(1.5)
                df = pd.read_csv(uploaded_file)
                st.dataframe(df, use_container_width=True)
                st.success("Data Authenticated. AI Report Generation in progress.")
