import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("No API key found. Please create a .env file with your GOOGLE_API_KEY.")
    st.stop()

# Configure the Gemini API
genai.configure(api_key=api_key)

# Initialize session state for chat history and model
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "chat" not in st.session_state:
    st.session_state.chat = None
    
if "current_model" not in st.session_state:
    st.session_state.current_model = "gemini-1.5-flash"

# Configure page
st.set_page_config(page_title="Context-Aware Gemini Chat")
st.title("Context-Aware Gemini Chat")

# Sidebar for configuration
st.sidebar.title("Model Configuration")
temperature = st.sidebar.slider(
    "Temperature", 
    min_value=0.0, 
    max_value=1.0, 
    value=0.7, 
    step=0.1,
    help="Higher values (e.g., 0.8) make output more random, lower values (e.g., 0.2) make it more focused."
)

model_choice = st.sidebar.selectbox(
    "Model",
    ["gemini-1.5-flash", "gemini-1.0-pro"],
    index=0,
    help="Select which Gemini model to use."
)

# Initialize or reset chat
def initialize_chat(model_name):
    model = genai.GenerativeModel(model_name=model_name)
    st.session_state.current_model = model_name
    return model.start_chat(history=[])

# Function to generate response
def get_gemini_response(user_input, temperature=0.7):
    try:
        # Send the message to the existing chat
        response = st.session_state.chat.send_message(
            user_input,
            generation_config={"temperature": temperature}
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Check if model has changed and reinitialize if needed
if st.session_state.current_model != model_choice:
    st.session_state.chat = initialize_chat(model_choice)
    st.sidebar.success(f"Changed model to {model_choice}")

# Initialize chat if needed
if st.session_state.chat is None:
    st.session_state.chat = initialize_chat(model_choice)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_gemini_response(user_input, temperature=temperature)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Instructions
if not st.session_state.messages:
    st.info("Send a message to start chatting with Gemini AI. The conversation context will be maintained across messages.")
    
# Display a note about the temperature setting
st.sidebar.markdown("---")
st.sidebar.markdown("""
**About Temperature:**
- Lower temperature (closer to 0): More deterministic, focused responses
- Higher temperature (closer to 1): More creative, diverse responses
""")

# Display current conversation length
st.sidebar.markdown("---")
st.sidebar.markdown(f"Current conversation: {len(st.session_state.messages)//2} turns")

# Add a reset button
if st.sidebar.button("Reset Conversation"):
    st.session_state.messages = []
    st.session_state.chat = initialize_chat(model_choice)
    st.rerun() 