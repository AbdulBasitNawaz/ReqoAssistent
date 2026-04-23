import streamlit as st

st.set_page_config(page_title="Reqo Assistant", page_icon="Images\logo3.png", layout="wide")

pages = {
    "Overview": [
         st.Page("pages/home.py", title="Home", icon=":material/home:", default=True),
    ],
    "Requirements Workspace": [
        st.Page("pages/req_form.py", title="Requirement Form", icon=":material/list_alt:"),
        st.Page("pages/document_gen.py", title="Generate Document", icon=":material/description:"),
        st.Page("pages/chat.py", title="AI Chat Assistant", icon=":material/smart_toy:"),
    ],
    "Support": [
        st.Page("pages/contact.py", title="Csutomer Support", icon=":material/contact_mail:"),
    ],
    "Admin": [
        st.Page("pages/admin_dashboard.py", title="Admin Panel", icon=":material/admin_panel_settings:"),
    ],
}

# ➤ Only show ADMIN SECTION if user is an admin
if st.session_state.get("role") == "admin":
    pages["Admin"] = [
        st.Page("pages/admin_dashboard.py", title="Admin Panel", icon=":material/admin_panel_settings:")
    ]

pg = st.navigation(pages)
pg.run()


st.logo("Images\logo2.png")
st.sidebar.text("Copy right Claims Protected")


