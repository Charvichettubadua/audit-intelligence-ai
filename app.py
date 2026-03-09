import streamlit as st

# --- LOGIN LOGIC ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🛡️ RiskShield AI Login")
    with st.form("login_form"):
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if user == "admin" and pw == "audit123": # Ikkada nee passwords pettu
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Credentials!")

# --- MAIN APP ---
if not st.session_state.logged_in:
    login()
else:
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))
    st.title("🛡️ RiskShield AI Dashboard")
    
    # Ee kinda nee Data Upload and AI logic antha untundi...
    uploaded_file = st.file_uploader("Upload Audit CSV File", type="csv")
    # ... rest of your code ...
