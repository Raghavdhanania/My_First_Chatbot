"""
Groq Chatbot Module
Handles communication with Groq API using Llama 3.2B model
"""

from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GroqChatbot:
    """A chatbot powered by Groq's Llama 3.2B model"""
    
    def __init__(self):
        """Initialize the Groq client with API key"""
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        self.client = Groq(api_key=api_key)
        self.conversation_history = []
        self.model = "llama-3.2b-vision-preview"  # Llama 3.2B model
    
    def chat(self, user_message: str) -> str:
        """
        Send a message to the chatbot and get a response
        
        Args:
            user_message: The user's input message
            
        Returns:
            The chatbot's response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stream=False
            )
            
            # Extract assistant response
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset_conversation(self):
        """Clear the conversation history"""
        self.conversation_history = []
    
    def get_conversation_history(self):
        """Get the current conversation history"""
        return self.conversation_history
