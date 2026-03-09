import streamlit as st
import pandas as pd

st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide")

# Static Login for immediate result
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<center><h1>🛡️ RISKSHIELD PORTAL</h1></center>", unsafe_allow_html=True)
    user = st.text_input("User ID")
    pw = st.text_input("Key", type="password")
    if st.button("ENTER"):
        if user == "charvi" and pw == "2026":
            st.session_state.auth = True
            st.rerun()
else:
    st.markdown("<h1 style='color:#38bdf8;'>C S Dashboard</h1>", unsafe_allow_html=True)
    st.write("Welcome, Charvi Sri")
    st.image("https://img.icons8.com/color/512/android-os.png", width=100)
    if st.button("Logout"):
        st.session_state.auth = False
        st.rerun()
