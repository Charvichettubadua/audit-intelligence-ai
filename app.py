import streamlit as st
import pandas as pd

# --- FORCE REFRESH CONFIG ---
st.set_page_config(page_title="CHARVI SRI | RISKSHIELD", layout="wide", page_icon="🤖")

# --- ULTRA-MODERN CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; color: #ffffff !important; }
    .login-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 50px; border-radius: 15px;
        border: 1px solid #38bdf8; text-align: center;
        margin: auto; width: 400px;
    }
    input { background-color: #111 !important; color: #38bdf8 !important; border: 1px solid #333 !important; }
    .stButton>button {
        background: #38bdf8 !important; color: black !important;
        font-weight: bold; width: 100%; border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- LOGIN SCREEN ---
if not st.session_state.auth:
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown("<h1 style='color: #38bdf8;'>RiskShield AI</h1>", unsafe_allow_html=True)
        u = st.text_input("IDENTITY", key="user_input")
        p = st.text_input("KEY", type="password", key="pass_input")
        if st.button("AUTHORIZE"):
            # STRICT CHECK
            if u.strip() == "charvisri" and p.strip() == "charvi@2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("INVALID CREDENTIALS")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    # 1. TOP ROW: ANDROID | CS | DETAILS
    t1, t2, t3 = st.columns([1, 2, 1])
    with t1:
        st.image("https://cdn-icons-png.flaticon.com/512/11516/11516905.png", width=100)
    with t2:
        st.markdown("<h1 style='text-align: center; letter-spacing: 20px; color: #38bdf8;'>C S</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>CHARVI SRI FORENSIC COMMAND CENTER</p>", unsafe_allow_html=True)
    with t3:
        st.write(f"Logged: **CHARVI SRI**")
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()

    st.divider()

    # 2. RISK IMAGES ROW
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Fraud Analytics")
    i2.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Network Risk")
    i3.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Data Anomaly")

    st.divider()
    uploaded_file = st.file_uploader("UPLOAD AUDIT DATA", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, use_container_width=True)
