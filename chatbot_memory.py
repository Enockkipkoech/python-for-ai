import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

st.title("Chatbot with Memory")

if "conversation" not in st.session_state:
    st.session_state.conversation = [] # {"role": "user", "parts": [{"text": user_input}]}

for message in st.session_state.conversation:
    role = "user" if message["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message["parts"][0]["text"])    

user_input = st.chat_input("Say something...")

if user_input:
    # Add the user's message to memory and show it
    st.session_state.conversation.append({"role": "user", "parts": [{"text": user_input}]})
    with st.chat_message("user"):
        st.markdown(user_input)

     # send the ENTIRE conversation so the model has context
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=st.session_state.conversation
                )  
                reply = response.text

            except Exception as e:
                reply = f"Sorry, something went wrong: {e}"
           
        # Add the AI's reply to memory and show it
        st.markdown(reply)  
    st.session_state.conversation.append({"role": "model", "parts": [{"text": reply}]})

if st.session_state.conversation:
    if st.button("Clear Conversation"):
        st.session_state.conversation = []
        st.rerun()    

# A simple "new chat" button that wipes the memory
if st.sidebar.button("🗑️ Clear chat"):
    st.session_state.conversation = []
    st.rerun()
