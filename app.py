import streamlit as st
import pandas as pd
import plotly.express as px
from risk_engine import calculate_risk
from agent import generate_audit_report
import time

# Chrome-like Full Page Setup
st.set_page_config(page_title="RiskShield AI", page_icon="🛡️", layout="wide")

# --- PREMIUM GLASSMORPHISM UI ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: radial-gradient(circle, #0d1117 0%, #010409 100%);
        color: #c9d1d9;
    }
    
    /* Modern Sidebar */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 2px solid #30363d;
    }
    
    /* High-end Metric Cards */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }

    /* Professional Blue Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #1f6feb 0%, #58a6ff 100%);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(88, 166, 255, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR DESIGN ---
with st.sidebar:
    st.markdown("<h1 style='color: #58a6ff;'>🛡️ RiskShield</h1>", unsafe_allow_html=True)
    st.caption("Intelligence Unit | Enterprise")
    st.markdown("---")
    uploaded_file = st.file_uploader("📂 Ingest Transaction Data", type="csv")
    st.markdown("---")
    st.markdown("### **System Health**")
    st.success("Core Engine: Active")
    st.info("AI Model: GPT-3.5 Turbo")

# --- MAIN DASHBOARD ---
st.markdown("<h2 style='color: white;'>Executive Risk Overview</h2>", unsafe_allow_html=True)

if uploaded_file:
    # --- AUTO-RUN LOGIC ---
    df = pd.read_csv(uploaded_file)
    df.columns = [c.capitalize() for c in df.columns]
    
    # Fast Processing Effect
    with st.spinner('🔄 Synchronizing Neural Patterns...'):
        processed_df = calculate_risk(df)
        time.sleep(1)

    # --- METRICS ---
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("TOTAL RECORDS", f"{len(processed_df):,}")
    with m2: 
        high_risk_n = len(processed_df[processed_df['Risk_Level'] == 'High'])
        st.metric("CRITICAL ANOMALIES", f"{high_risk_n}", delta="Action Required", delta_color="inverse")
    with m3:
        exposure = processed_df['Amount'].sum() if 'Amount' in processed_df.columns else 0
        st.metric("TOTAL EXPOSURE", f"${exposure:,.0f}")
    with m4: st.metric("RISK COVERAGE", "100%")

    st.markdown("---")

    # --- VISUALIZATIONS ---
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("📊 Risk Segmentation")
        fig = px.pie(processed_df, names='Risk_Level', hole=0.6,
                     color='Risk_Level',
                     color_discrete_map={'High':'#f85149', 'Medium':'#d29922', 'Low':'#3fb950'})
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="white", showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("🚩 Priority Inspection Table")
        # Clean Table View
        st.dataframe(processed_df.head(15), use_container_width=True, height=350)

    # --- AI FORENSIC REPORT ---
    st.markdown("---")
    st.subheader("🤖 GenAI Forensic Narrative")
    if st.button("EXECUTE DEEP SCAN"):
        with st.chat_message("assistant"):
            try:
                report = generate_audit_report(processed_df)
                st.markdown(f"<div style='background: #161b22; padding: 20px; border-radius: 10px; border-left: 4px solid #58a6ff;'>{report}</div>", unsafe_allow_html=True)
            except:
                st.error("API Error: Please check your OpenAI Key in .env file.")

else:
    st.info("Awaiting Data Ingestion... Please upload your CSV to begin.")