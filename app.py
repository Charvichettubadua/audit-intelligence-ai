import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Page Config
st.set_page_config(page_title="RiskShield AI Portal", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for exact Screenshot (87) Login and Dashboard UI
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background-color: #050a12;
        color: white;
    }
    
    /* Login Page Styling - Exact match to Screenshot (87) */
    .login-container {
        max-width: 600px;
        margin: 0 auto;
        padding-top: 50px;
        text-align: center;
    }
    .main-title {
        color: #4cc9f0;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #a0a0a0;
        font-size: 18px;
        margin-bottom: 40px;
    }
    .input-label {
        text-align: left;
        color: #4d4d4d;
        font-size: 14px;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    
    /* Authorize Button */
    .stButton>button {
        background-color: #4cc9f0 !important;
        color: black !important;
        font-weight: bold !important;
        width: 150px;
        height: 45px;
        border-radius: 5px;
        border: none;
        margin-top: 20px;
    }

    /* Dashboard Cards - From Video */
    .metric-card {
        background-color: #0d1117;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #1f2937;
        text-align: center;
    }
    .alert-box {
        background-color: #1a1010;
        border-left: 5px solid #ff4b4b;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State for Login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN PAGE (Exact Screenshot 87) ---
if not st.session_state.logged_in:
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">RiskShield AI Portal</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Next-Gen Forensic Intelligence</p>', unsafe_allow_html=True)
    st.markdown('<hr style="border-top: 1px solid #333;">', unsafe_allow_html=True)
    
    # Form layout
    with st.container():
        corp_id = st.text_input("CORPORATE ID", value="gdv.ch.charvisri@gmail.com")
        access_key = st.text_input("SECURE ACCESS KEY", type="password", value="************")
        
        if st.button("AUTHORIZE"):
            # Simple check for demo
            if corp_id == "gdv.ch.charvisri@gmail.com":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("ACCESS DENIED: Please Check Credentials")
    st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD PAGE (Exact Video Layout) ---
else:
    # Header from Video
    st.markdown("<h1 style='text-align: center; color: #4cc9f0;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey;'>CHARVI SRI | FORENSIC TECH ENTHUSIAST</p>", unsafe_allow_html=True)
    
    # Metrics Row
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metric-card"><h4>High Risk Flags</h4><h2 style="color:#ff4b4b;">34176</h2><p>↑ Anomalies Found</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><h4>Neural Accuracy</h4><h2 style="color:#4cc9f0;">99.2%</h2><p>✓ System Stable</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><h4>Risk Status</h4><h2 style="color:#ff4b4b;">ALERT</h2><p>↑ Review Needed</p></div>', unsafe_allow_html=True)

    st.write("---")

    # Main Visuals Row
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("Neural Risk Trend")
        # Creating a mockup graph similar to the video
        chart_data = pd.DataFrame({
            'index': range(16),
            'Audit Risk': np.random.randn(16).cumsum(),
            'Fraud Probability': np.random.randn(16).cumsum()
        })
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=chart_data['index'], y=chart_data['Audit Risk'], name='Audit Risk', line=dict(color='#4cc9f0', width=3)))
        fig.add_trace(go.Scatter(x=chart_data['index'], y=chart_data['Fraud Probability'], name='Fraud Probability', line=dict(color='#ffffff', width=2, dash='dot')))
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("Neural Alerts")
        st.markdown('<div class="alert-box"><strong>Critical:</strong> High-value transaction mismatch detected in Node-7.</div>', unsafe_allow_html=True)
        st.markdown('<div style="background-color: #1a1610; border-left: 5px solid #ffaa00; padding: 15px; border-radius: 5px;"><strong>Warning:</strong> Duplicate vendor IDs identified.</div>', unsafe_allow_html=True)

    # Forensic Stream (The Table at the bottom of the video)
    st.subheader("Forensic Stream")
    dummy_data = pd.DataFrame(np.random.randn(10, 16), columns=[f'V{i}' for i in range(1, 17)])
    st.dataframe(dummy_data, use_container_width=True)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
