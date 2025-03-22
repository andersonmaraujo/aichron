import os
import streamlit as st
import openai
import speech_recognition as sr
from dotenv import load_dotenv
from prompts import get_formatted_prompt

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# App title and description
st.set_page_config(
    page_title="Crohn Compass",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #3366cc;
    }
    .sub-header {
        font-size: 1.1rem;
        font-style: italic;
        color: #666666;
    }
    .disclaimer {
        font-size: 0.8rem;
        color: #888888;
        border-top: 1px solid #dddddd;
        padding-top: 10px;
    }
    .stButton button {
        background-color: #3366cc;
        color: white;
        font-weight: bold;
        border-radius: 20px;
        padding: 0.5rem 1rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
    }
    .user-message {
        background-color: #e6f2ff;
    }
    .assistant-message {
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">Crohn Compass</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your voice-powered companion for navigating Crohn\'s disease</p>', unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm Crohn Compass, your voice-powered assistant for navigating Crohn's disease. How can I help you today?"}
    ]

# Function to get response from OpenAI
def get_llm_response(prompt):
    # Get formatted messages with system prompt and examples
    messages = get_formatted_prompt(prompt)
    
    # Get response from OpenAI
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
    )
    
    return response.choices[0].message.content

# Voice input function
def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Visual feedback during recording
        recording_placeholder = st.empty()
        recording_placeholder.info("🎤 Listening... Speak now.")
        audio = r.listen(source)
        recording_placeholder.info("🔍 Processing your speech...")
    
    try:
        text = r.recognize_google(audio)
        recording_placeholder.empty()
        return text
    except sr.UnknownValueError:
        recording_placeholder.error("Sorry, I couldn't understand your speech. Please try again.")
        return None
    except sr.RequestError:
        recording_placeholder.error("Sorry, there was an error with the speech recognition service.")
        return None

# Display chat messages
for message in st.session_state.messages:
    message_class = "user-message" if message["role"] == "user" else "assistant-message"
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="chat-message {message_class}">{message["content"]}</div>', unsafe_allow_html=True)

# Create two columns for input options
col1, col2 = st.columns(2)

# Voice input button
with col1:
    if st.button("🎤 Speak to Crohn Compass"):
        user_input = voice_to_text()
        if user_input:
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(f'<div class="chat-message user-message">{user_input}</div>', unsafe_allow_html=True)
            
            # Get and display assistant response
            with st.spinner("Thinking..."):
                response = get_llm_response(user_input)
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(f'<div class="chat-message assistant-message">{response}</div>', unsafe_allow_html=True)

# Text input as fallback
with col2:
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm Crohn Compass, your voice-powered assistant for navigating Crohn's disease. How can I help you today?"}
        ]
        st.experimental_rerun()

# Text input field
text_input = st.chat_input("Type your question here...")
if text_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": text_input})
    with st.chat_message("user"):
        st.markdown(f'<div class="chat-message user-message">{text_input}</div>', unsafe_allow_html=True)
    
    # Get and display assistant response
    with st.spinner("Thinking..."):
        response = get_llm_response(text_input)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(f'<div class="chat-message assistant-message">{response}</div>', unsafe_allow_html=True)

# Suggested topics
st.markdown("### Try asking about:")
topic_col1, topic_col2 = st.columns(2)

with topic_col1:
    if st.button("What is Crohn's disease?"):
        text_input = "What is Crohn's disease?"
        st.session_state.messages.append({"role": "user", "content": text_input})
        with st.chat_message("user"):
            st.markdown(f'<div class="chat-message user-message">{text_input}</div>', unsafe_allow_html=True)
        
        with st.spinner("Thinking..."):
            response = get_llm_response(text_input)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(f'<div class="chat-message assistant-message">{response}</div>', unsafe_allow_html=True)

with topic_col2:
    if st.button("Common symptoms"):
        text_input = "What are the main symptoms of Crohn's disease?"
        st.session_state.messages.append({"role": "user", "content": text_input})
        with st.chat_message("user"):
            st.markdown(f'<div class="chat-message user-message">{text_input}</div>', unsafe_allow_html=True)
        
        with st.spinner("Thinking..."):
            response = get_llm_response(text_input)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(f'<div class="chat-message assistant-message">{response}</div>', unsafe_allow_html=True)

# Disclaimer at the bottom
st.markdown('<p class="disclaimer">**Disclaimer**: This is not medical advice. Always consult a licensed physician for diagnosis and treatment.</p>', unsafe_allow_html=True) 