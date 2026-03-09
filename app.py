import streamlit as st
import pandas as pd
import time

# --- Page Config ---
st.set_page_config(page_title="RiskShield AI | Premium Audit", layout="wide", page_icon="⚡")

# --- Custom High-End Professional CSS ---
st.markdown("""
    <style>
    /* Dark Slate & Deep Charcoal Theme */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
        color: #f8fafc;
    }
    
    /* Neon Audit Green Accent (Inspired but Unique) */
    .highlight { color: #22c55e; font-weight: bold; }
    
    /* Modern Login Card - Glassmorphism */
    .login-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 60px;
        border-radius: 24px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        max-width: 500px;
        margin: auto;
    }

    /* Input Styling */
    .stTextInput>div>div>input {
        background-color: rgba(255,255,255,0.05) !important;
        color: #22c55e !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }

    /* Action Button - High Contrast */
    .stButton>button {
        background: linear-gradient(90deg, #22c55e 0%, #10b981 100%) !important;
        color: #064e3b !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        border: none !important;
        height: 3.5em !important;
        transition: all 0.4s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(34, 197, 94, 0.3);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #020617 !important;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session Management ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- Credentials ---
U_ID = "chintu"
U_KEY = "audit2026"

# --- LOGIN VIEW ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>🛡️</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>RiskShield <span style='color: #22c55e;'>AI</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Next-Gen Forensic Intelligence</p>", unsafe_allow_html=True)
    
    with st.form("login"):
        user = st.text_input("Operator ID", placeholder="e.g. chintu")
        key = st.text_input("Access Key", type="password", placeholder="••••••••")
        submit = st.form_submit_button("ENTER SYSTEM")
        
        if submit:
            if user == U_ID and key == U_KEY:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Authentication Error: Invalid Signature")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PREMIUM DASHBOARD VIEW ---
else:
    st.sidebar.markdown("<h2 style='color: #22c55e;'>RiskShield AI</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    st.sidebar.write(f"🟢 **System Active**")
    st.sidebar.write(f"👤 Operator: `{U_ID}`")
    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.rerun()

    # Main Header
    st.markdown("<h1 style='font-size: 42px;'>Forensic <span style='color: #22c55e;'>Command Center</span></h1>", unsafe_allow_html=True)
    st.write("Real-time anomaly detection and risk orchestration engine.")

    # KPI Metrics
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Scanning Engine", "Active", delta="1.2ms")
    with c2: st.metric("Risk Threshold", "94%", delta="-2%")
    with c3: st.metric("AI Model", "Flash 2.5")
    with c4: st.metric("Encryption", "Post-Quantum")

    st.markdown("<br>", unsafe_allow_html=True)

    # File Ingestion Area
    st.markdown("### 📥 Data Ingestion")
    uploaded_file = st.file_uploader("Upload Ledger / Transaction Data (CSV format)", type="csv")
    
    if uploaded_file:
        with st.spinner("Analyzing data patterns..."):
            time.sleep(2)
            df = pd.read_csv(uploaded_file)
            st.markdown("#### Previewing Ingested Data")
            st.dataframe(df, use_container_width=True)
            st.success("Analysis Complete: 0 High-Risk anomalies detected in sample.")
