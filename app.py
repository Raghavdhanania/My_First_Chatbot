"""
Streamlit Chatbot Web Application
A simple chatbot interface powered by Groq's Llama 3.2B model
"""

import streamlit as st
from chatbot import GroqChatbot

# Page configuration
st.set_page_config(
    page_title="Llama Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0.5rem;
        display: flex;
        gap: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        flex-direction: row-reverse;
    }
    .assistant-message {
        background-color: #f5f5f5;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🤖 Llama 3.2B Chatbot")
st.markdown("Powered by Groq API | Chat with Llama 3.2B")

# Initialize session state
if "chatbot" not in st.session_state:
    try:
        st.session_state.chatbot = GroqChatbot()
    except ValueError as e:
        st.error(f"Error initializing chatbot: {e}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("Settings")
    
    if st.button("🔄 Clear Conversation", use_container_width=True):
        st.session_state.chatbot.reset_conversation()
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown(
        """
        This chatbot uses:
        - **Model**: Llama 3.2B
        - **Provider**: Groq API
        - **Framework**: Streamlit
        
        Enjoy chatting! 💬
        """
    )

# Chat display area
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
                <div class="chat-message user-message">
                    <div><b>You:</b> {message["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message assistant-message">
                    <div><b>Llama:</b> {message["content"]}</div>
                </div>
                """, unsafe_allow_html=True)

# Input area
st.markdown("---")

# Create columns for input and button
col1, col2 = st.columns([0.85, 0.15])

with col1:
    user_input = st.text_input(
        "Your message:",
        placeholder="Ask me anything...",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send", use_container_width=True)

# Process user input
if send_button and user_input:
    # Add user message to display
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show typing indicator
    with st.spinner("Thinking..."):
        response = st.session_state.chatbot.chat(user_input)
    
    # Add assistant response to display
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Rerun to update chat display
    st.rerun()
elif send_button:
    st.warning("Please enter a message!")
