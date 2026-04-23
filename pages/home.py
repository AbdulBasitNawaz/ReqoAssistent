import streamlit as st

st.set_page_config(page_title="Reqo Assistant", page_icon="Images\logo3.png", layout="wide")

st.set_page_config(page_title="Reqo Assistant", layout="centered")

# --- Header ---
st.markdown(
    """
    <style>
    .custom-heading {
        color: #7127f6;
        font-size: 60px;
        font-family: Montserrat, sans-serif;
        font-weight: 900;
        transition: all 0.3s ease;  /* smooth hover effect */
    }

    .custom-heading:hover {
        color: #9b4fff;       /* brighter color on hover */
        font-size: 66px;      /* slightly larger */
        cursor: pointer;      /* pointer cursor */
    }
    </style>

    <h1 class="custom-heading">Reqo Assistant</h1>
    """,
    unsafe_allow_html=True
)

st.subheader("Smart Requirement Collection & Documentation Tool")

st.write("""
Welcome!  
This assistant will help you collect and structure software requirements
and generate a clean Requirement Document automatically.
""")

st.write("---")


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
# --- Start Form Button ---
st.markdown('<h1 style="color:#333bee;">Get Started</h1>', unsafe_allow_html=True)

st.write("Click the button below to begin filling the Requirement Form.")

if st.button("Start Requirement Form"):
    st.switch_page("pages/req_form.py")

st.write("---")

# --- Optional: Workflow Steps ---
st.markdown('<h1 style="color:#45d082;">How It Works</h1>', unsafe_allow_html=True)

st.markdown("""
1. **Fill Requirement Form** – Tell us your project details  
2. **AI Chat Assistant** – Ask questions or clarify your ideas  
3. **Generate Document** – Automatically create a clean requirement document  
4. **Submit** – Finalize and send your requirements  
""")

