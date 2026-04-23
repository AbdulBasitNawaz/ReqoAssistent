import streamlit as st

st.set_page_config(page_title="Reqo Assistant", page_icon="Images\logo3.png", layout="wide")

st.title("Requirement Form")
st.write("This page will collect all project requirement details from the user.")

# -----------------------------
# MAIN FORM
# -----------------------------


with st.form("requirements_form", clear_on_submit=False):

    st.header("1️⃣ Project Overview")

    purpose = st.text_area(
        "Q1. What is the main purpose of the project? (Short description)", 
        placeholder="Example: An app for managing orders in a restaurant..."
    )

    problem = st.text_area(
        "Q2. What problem does this software solve?", 
        placeholder="Explain the real challenge you want to fix..."
    )

    vision = st.text_area(
        "Q3. What is your long-term vision for this product?"
    )

    # ------------ Target Users ------------

    st.header("2️⃣ Target Users")

    target_users = st.multiselect(
        "Q4. Who will use this software?",
        ["Customers", "Employees", "Admins", "Vendors", "General Public"]
    )

    user_goals = st.text_area(
        "Q5. What actions should users be able to perform?",
        placeholder="Example: Customers can order food, track delivery..."
    )

    # ------------ Feature Requirements ------------

    st.header("3️⃣ Feature Requirements")

    core_features = st.multiselect(
        "Q6. Select the core features you need:",
        [
            "User Login/Signup",
            "Admin Dashboard",
            "File Upload",
            "Messaging/Chat",
            "Payments",
            "Reports & Analytics",
            "API Integrations",
            "Notifications",
            "Location Tracking",
            "Data Entry Forms",
            "Role-Based Access Control",
        ]
    )

    special_features = st.text_area(
        "Q7. Any special or unique functionality?",
        placeholder="Example: AI-based detection, automation, scheduling..."
    )

    # ------------ Platform ------------

    st.header("4️⃣ Platform Choices")

    platform = st.radio(
        "Q8. What type of application do you want?",
        ["Web App", "Mobile App (Android)", "Mobile App (iOS)", "Both Android & iOS", "Desktop App", "Backend/API Only"],
        index=None,
        key="platform"
    )

    preference = st.radio(
        "Q9. Do you prefer any specific technology?",
        ["No preference", "React", "Next.js", "Flutter", "React Native", "Python", "Node.js", "Java", ".NET"],
        index=None,
        key="tech_pref"
    )

    # ------------ Timeline & Budget ------------

    st.header("5️⃣ Timeline & Budget")

    timeline = st.selectbox(
        "Q10. Expected project timeline?",
        ["ASAP (1–2 months)", "3–6 months", "6–12 months", "Not sure"]
    )

    budget = st.selectbox(
        "Q11. What is your budget range?",
        ["$1,000–$5,000", "$5,000–$15,000", "$15,000–$50,000", "$50,000+", "Not decided yet"]
    )

    # ------------ Non-Functional ------------

    st.header("6️⃣ Non-Functional Requirements")

    performance = st.radio(
        "Q12. Expected performance level?",
        ["Normal", "High Performance (Fast/Real-time)", "Heavy Data Handling"],
        index=None,
        key="performance_level"
    )

    security = st.text_area(
        "Q13. Any security requirements?",
        placeholder="Example: encryption, role-based access, GDPR compliance..."
    )

    expected_users = st.selectbox(
        "Q14. Expected number of users?",
        ["< 100", "100–1k", "1k–10k", "10k–50k", "50k+"]
    )

    # ------------ Attachments ------------

    st.header("7️⃣ Attachments")

    attachment = st.file_uploader(
        "Q15. Upload any reference documents, wireframes, or diagrams (optional)"
    )

    # ------------ Contact ------------

    st.header("8️⃣ Contact Details")

    name = st.text_input("Q16. Your name or company (optional)")
    email = st.text_input("Q17. Your email (required)")
    phone = st.text_input("Q18. Phone number (optional)")

    # ------------ SUBMIT BUTTON ------------

    submitted = st.form_submit_button("Submit Requirements")

    # ---------------- Submission Handling ----------------

    if submitted:
        if not email:
            st.error("❌ Email is required to submit the form.")
        else:
            st.success("✅ Your requirements have been submitted successfully!")
            st.info("You will now be redirected to the AI assistant for deeper requirement exploration.")
            # SAVE ALL FORM VALUES INTO SESSION STATE
            st.session_state.form_data = {
                "purpose": purpose,
                "problem": problem,
                "vision": vision,
                "target_users": target_users,
                "user_goals": user_goals,
                "core_features": core_features,
                "special_features": special_features,
                "platform": platform,
                "preference": preference,
                "timeline": timeline,
                "budget": budget,
                "performance": performance,
                "security": security,
                "expected_users": expected_users,
                "name": name,
                "email": email,
                "phone": phone,
        }

        st.success("✅ Your requirements have been submitted successfully!")
        st.info("You will now be redirected to the AI assistant for deeper requirement exploration.")
        st.switch_page("pages/chat.py")
