import streamlit as st
import pandas as pd
from io import StringIO
from datetime import datetime

st.set_page_config(page_title="Admin Dashboard", layout="wide")

st.title("Reqo Assistant — Admin Dashboard")
st.write("Manage submissions, view form data, and monitor user interactions.")

st.logo("Images/logo2.png")
st.sidebar.text("Admin Access Only")


# ---------------------------------------------------
# 1. Ensure data containers exist
# ---------------------------------------------------
if "form_submissions" not in st.session_state:
    st.session_state.form_submissions = []  # List of dicts

if "chat_logs" not in st.session_state:
    st.session_state.chat_logs = []  # (Optional) List of chat session dicts


# ---------------------------------------------------
# 2. Admin Panel Tabs
# ---------------------------------------------------
tab1, tab2 = st.tabs(["📄 Requirement Form Submissions", "💬 Chat Logs"])


# ===================================================
# 📄 TAB 1 — VIEW FORM SUBMISSIONS
# ===================================================
with tab1:

    st.subheader("📄 Requirement Form Submissions")

    submissions = st.session_state.form_submissions

    if len(submissions) == 0:
        st.info("No submissions found yet.")
    else:
        # Convert to DataFrame
        df = pd.DataFrame(submissions)
        st.dataframe(df, use_container_width=True)

        # Download all as CSV
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        st.download_button(
            label="⬇ Download All Submissions (CSV)",
            data=csv_buffer.getvalue(),
            file_name="reqo_submissions.csv",
            mime="text/csv"
        )

        # Clear button
        if st.button("🗑 Clear All Submissions"):
            st.session_state.form_submissions = []
            st.success("All submissions cleared.")
            st.rerun()



# ===================================================
# 💬 TAB 2 — VIEW CHAT LOGS
# ===================================================
with tab2:

    st.subheader("💬 Chat Logs (optional)")

    logs = st.session_state.chat_logs

    if len(logs) == 0:
        st.info("No chat logs recorded.")
    else:
        for i, chat in enumerate(logs):
            with st.expander(f"Chat Session #{i+1}"):
                for m in chat:
                    role = "🧑 User" if m["role"] == "user" else "🤖 Assistant"
                    st.write(f"**{role}:** {m['content']}")

        if st.button("🗑 Clear All Chats"):
            st.session_state.chat_logs = []
            st.success("Chat logs cleared.")
            st.rerun()
