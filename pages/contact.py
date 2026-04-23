import streamlit as st

st.set_page_config(page_title="Reqo Assistant", page_icon="Images\logo3.png", layout="wide")

st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #28a745;
        color: white;
        height: 3em;
        width: 100%;
        border-radius: 5px;
        border: 1px solid #28a745;
        transition: 0.5s;
    }
    div.stButton > button:hover {
        background-color: transparent;
        border: 1px solid #28a745;
        color: #68f789;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HERO SECTION ---
coll, col2 = st.columns(2, gap="small", vertical_alignment="center")
with coll:
    st.image("Images\logo2.png", width=230)
with col2:
    st.title("Contact Form", anchor=False)
    st.write(
        "Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.",
        "If there is any inquery or want to contact the team or have found bugs or error, you can report here:."
    )
    if st.button("Contact Us"):
        st.text_input("First Name")
        st.text_input("Email")
        st.text_area("Message")
        if st.button("Send"):
            st.success("Message sent!")