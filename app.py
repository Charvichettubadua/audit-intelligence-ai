import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Simple but Premium CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: white; }
    .header-box { text-align: center; padding: 20px; border-bottom: 2px solid #38bdf8; }
    .risk-card { border-radius: 10px; border: 1px solid #1e293b; padding: 10px; background: #161e2e; }
    .stMetric { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #38bdf8; }
    </style>
    """, unsafe_allow_html=True)

# --- Session State for Login ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- LOGIN SCREEN ---
if not in st.session_state.auth:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown("<h2 style='text-align: center; color: #38bdf8;'>🛡️ RiskShield Portal</h2>", unsafe_allow_html=True)
        user = st.text_input("IDENTITY", key="u1")
        pw = st.text_input("SECURE KEY", type="password", key="p1")
        if st.button("AUTHORIZE"):
            if user.strip() == " " and pw.strip() == " ":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied: Check Credentials")

# --- DASHBOARD SCREEN ---
else:
    # 1. TOP ROW: ANDROID | CS | USER
    t1, t2, t3 = st.columns([1, 2, 1])
    with t1:
        # Android Style Logo
        st.image("https://cdn-icons-png.flaticon.com/512/11516/11516905.png", width=120)
    with t2:
        st.markdown("<h1 style='text-align: center; letter-spacing: 15px; color: #38bdf8; font-size: 60px;'>C S</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 20px; color: #94a3b8;'>CHARVI SRI | FORENSIC AUDIT COMMAND</p>", unsafe_allow_html=True)
    with t3:
        st.write(f"Logged: **Charvi Sri**")
        if st.button("Log Out"):
            st.session_state.auth = False
            st.rerun()

    st.divider()

    # 2. RISK RELATED IMAGES COLUMN (Professional & High-Res)
    st.markdown("### 🔍 Risk Monitoring Systems")
    i1, i2, i3 = st.columns(3)
    with i1:
        st.image("https://images.unsplash.com/photo-1551288049-bbda48658a7d?w=400", caption="Anomalous Trend Analysis")
    with i2:
        st.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Financial Risk Graph")
    with i3:
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", caption="Global Cyber Surveillance")

    st.divider()

    # 3. DATA UPLOAD SECTION
    st.markdown("### 📥 Neural Data Ingestion")
    uploaded_file = st.file_uploader("Upload Audit CSV File", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Data Authenticated. Showing Top Records:")
        st.dataframe(df.head(10), use_container_width=True)


