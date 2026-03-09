import streamlit as st
import pandas as pd
import time

# --- Ultra-Premium Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Custom Styling for Luxury Risk Interface ---
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #020617 100%) !important;
        color: #f8fafc;
    }
    
    /* Elegant Input Fields */
    .stTextInput>div>div>input {
        background-color: #1a1a1a !important;
        color: #38bdf8 !important; /* Cyber Blue */
        border: 1px solid #333 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }
    
    /* Professional Action Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8 0%, #0ea5e9 100%) !important;
        color: #0c0a09 !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border-radius: 8px !important;
        letter-spacing: 2px;
        width: 100%;
        height: 3.5em;
        margin-top: 20px;
    }
    
    /* Image Row Styling */
    .risk-image-col img {
        border-radius: 8px;
        width: 100%;
        height: 150px;
        object-fit: cover;
    }
    
    /* Login Card */
    .login-container {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 60px;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- credentials ---
CRED_USER = "charvisri"
CRED_PASS = "charvi@2026"

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- LOGIN SCREEN ---
if not st.session_state.authenticated:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #38bdf8;'>RiskShield AI Portal</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #ccc; font-size: 14px;'>Next-Gen Forensic Intelligence</p>", unsafe_allow_html=True)
        st.markdown("<hr style='border: 0.5px solid #333;'>", unsafe_allow_html=True)
        
        user = st.text_input("CORPORATE ID", placeholder="User ID")
        pw = st.text_input("SECURE ACCESS KEY", type="password", placeholder="Access Key")
        
        if st.button("AUTHORIZE"):
            if user == CRED_USER and pw == CRED_PASS:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("ACCESS DENIED: Please Check Credentials")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    # Top Row: Android Logo, CS in Middle, User details
    row1_cols = st.columns([1, 3, 1])
    
    with row1_cols[0]:
        st.image("https://cdn-icons-png.flaticon.com/512/11516/11516905.png", width=80) # Cyber Shield Logo
        
    with row1_cols[1]:
        st.markdown("<h1 style='text-align: center; letter-spacing: 15px; font-weight: 200;'>C <span style='color:#38bdf8'>S</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888;'>CHARVI SRI FORENSIC AUDIT CENTER</p>", unsafe_allow_html=True)
        
    with row1_cols[2]:
        st.write(f"Logged in as: `{CRED_USER}`")
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

    st.divider()

    # Risk Images Row
    row2_cols = st.columns([1, 1, 1], gap="small")
    with row2_cols[0]:
        st.image("https://images.unsplash.com/photo-1610427909340-df5beff090ea?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTkyMXwwfDF8c2VhcmNofDgzfHxyaXNrfGVufDB8fHx8MTY3ODk0OTEwNA&ixlib=rb-4.0.3&q=80&w=400", use_container_width=True) # Graph and Money
        st.markdown("<p style='text-align: center; font-size: 14px;'>Fraud Analytics</p>", unsafe_allow_html=True)
        
    with row2_cols[1]:
        st.image("https://images.unsplash.com/photo-1599381403222-29774a350488?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTkyMXwwfDF8c2VhcmNofDE3fHxyaXNrfGVufDB8fHx8MTY3ODk0OTEwNA&ixlib=rb-4.0.3&q=80&w=400", use_container_width=True) # Network Security
        st.markdown("<p style='text-align: center; font-size: 14px;'>Network Risk</p>", unsafe_allow_html=True)
        
    with row2_cols[2]:
        st.image("https://images.unsplash.com/photo-1628701977934-8c8d8b9f67a6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTkyMXwwfDF8c2VhcmNofDU0fHxyaXNrfGVufDB8fHx8MTY3ODk0OTEwNA&ixlib=rb-4.0.3&q=80&w=400", use_container_width=True) # Security Cameras
        st.markdown("<p style='text-align: center; font-size: 14px;'>Anomaly Detection</p>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Drag and Drop Ingestion Area
    with st.expander("📂 INGEST AUDIT DATA", expanded=True):
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df, use_container_width=True)
            st.success("AUTHENTICATED DATA LOADED.")
