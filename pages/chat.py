

import streamlit as st
import google.generativeai as genai
import time
import json

st.set_page_config(page_title="AI Chat Assistant", layout="wide")
st.title("💬 Requirement Clarification Assistant")

st.logo("Images/logo2.png")

# ---------------------------
# Load Form Data
# ---------------------------
form_data = st.session_state.get("form_data", None)

if form_data is None:
    st.error("⚠️ No form data found. Please fill the Requirement Form first.")
    st.stop()

# ---------------------------
# Configure Gemini
# ---------------------------
genai.configure(api_key="*******************************")

system_instruction = f"""
You are REQO — an AI Requirement Clarification Assistant.
Use the form_data to guide the conversation.
Your job is to see the data collected from the form and ask more questions 
related to requirement engineering. Identify missing details and capture 
functional & non-functional requirements.

Form data:
{form_data}

Ask organized, helpful, clear requirement questions.
"""

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=system_instruction
)

# ---------------------------
# Chat Session Setup
# ---------------------------
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "is_bot_typing" not in st.session_state:
    st.session_state.is_bot_typing = False


# ---------------------------
# Stream Response Animation
# ---------------------------
def stream_response(text, container):
    displayed = ""
    for char in text:
        displayed += char
        container.markdown(displayed)
        time.sleep(0.015)


# ---------------------------
# Show Chat History
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# ---------------------------
# Chat Input
# ---------------------------
if st.session_state.is_bot_typing:
    user_input = st.chat_input("AI is typing...", disabled=True)
else:
    user_input = st.chat_input("Type your message...")


# ---------------------------
# Handle User Message
# ---------------------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.is_bot_typing = True
    st.rerun()


# ---------------------------------------------------------
# 📘 Generate Document Button
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #28a745;
        color: white;
        height: 3em;
        width: 100%;
        border-radius: 5px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #218838;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.divider()
st.subheader("📄 Finalize & Generate Requirement Document")

if st.button("Generate Requirement Document"):
    st.session_state.generate_doc_request = True
    st.rerun()


# ---------------------------------------------------------
# 🤖 Bot Answers (DO NOT TOUCH)
# ---------------------------------------------------------
if st.session_state.is_bot_typing:

    last_user_msg = st.session_state.messages[-1]["content"]

    response = st.session_state.chat_session.send_message(last_user_msg)
    bot_text = response.text

    with st.chat_message("assistant"):
        text_box = st.empty()
        stream_response(bot_text, text_box)

    st.session_state.messages.append({"role": "assistant", "content": bot_text})

    st.session_state.is_bot_typing = False
    st.rerun()


# ---------------------------------------------------------
# 📄 STEP 2 — Process Data & Fill Missing Fields Using Gemini
# ---------------------------------------------------------
if st.session_state.get("generate_doc_request", False):

    with st.spinner("Analyzing your data with REQO..."):

        prompt = f"""
You are REQO — a Requirement Engineering Assistant.

TASK:
You MUST return ONLY valid JSON. 
No explanations. No text outside JSON. No markdown. No comments.

JSON FORMAT YOU MUST OUTPUT:
{{
  "purpose": "",
  "problem": "",
  "vision": "",
  "target_users": [],
  "user_goals": "",
  "core_features": [],
  "special_features": "",
  "platform": "",
  "preference": "",
  "timeline": "",
  "budget": "",
  "performance": "",
  "security": "",
  "expected_users": "",
  "name": "",
  "email": "",
  "phone": "",
  "functional_requirements": [],
  "non_functional_requirements": []
}}

INSTRUCTIONS:
1. Read form_data and fill all missing or empty fields.
2. Read chat history and extract important requirement details.
3. Generate functional & non-functional requirements.
4. Ensure the output is STRICTLY valid JSON.

Here is the form_data:
{st.session_state.form_data}

Here is the chat history:
{st.session_state.messages}
"""


        result = model.generate_content(prompt)

        raw_output = result.text.strip()
        # Remove unwanted text before/after JSON
        if raw_output.startswith("```"):
            raw_output = raw_output.strip("`")

        # Extract JSON inside braces
        start = raw_output.find("{")
        end = raw_output.rfind("}")

        if start != -1 and end != -1:
            refined_json = raw_output[start:end+1]
        else:
            refined_json = raw_output
        

    # Convert JSON → dict
    try:
        refined_data = json.loads(refined_json)
        st.session_state.form_data = refined_data

    except json.JSONDecodeError as e:
        st.error("❌ Gemini still returned invalid JSON.")
        st.write("Raw Output:")
        st.code(raw_output)
        st.stop()


    st.session_state.generate_doc_request = False
    st.switch_page("pages/document_gen.py")







