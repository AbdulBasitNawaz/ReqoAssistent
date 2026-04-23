import streamlit as st

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "123":
        st.session_state["role"] = "admin"
        st.success("Logged in as Admin")
        st.rerun()
    else:
        st.session_state["role"] = "user"
        st.success("Logged in as User")
        st.rerun()
