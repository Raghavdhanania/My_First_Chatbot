# Llama 3.2B Chatbot with Streamlit & Groq

A simple yet powerful chatbot web application built with Streamlit and powered by Groq's Llama 3.2B model.

## Features

- 🤖 Real-time chat interface using Streamlit
- 🚀 Powered by Groq's Llama 3.2B model (fast inference)
- 💬 Conversation history tracking
- 🔄 Clear conversation button to reset chat
- 📱 Responsive and user-friendly interface

## Project Structure

```
My_First_Chatbot/
├── app.py                 # Main Streamlit web application
├── chatbot.py            # Groq chatbot module
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API key)
├── .env.example          # Example environment file
└── README.md            # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- Groq API key (get one from [console.groq.com](https://console.groq.com))

## Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "My_First_Chatbot"
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   - The `.env` file already contains your Groq API key
   - Make sure not to share your `.env` file with others
   - For production, use environment variables or secrets management

## Usage

1. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Access the application**
   - The app will open automatically in your browser (usually at `http://localhost:8501`)
   - Or manually navigate to `http://localhost:8501`

3. **Start chatting**
   - Type your message in the input field
   - Click "Send" or press Enter
   - The chatbot will respond using Llama 3.2B

## How It Works

### `chatbot.py`
- Initializes the Groq client with your API key
- Manages conversation history
- Sends messages to Llama 3.2B model via Groq API
- Handles responses and maintains context

### `app.py`
- Creates the Streamlit web interface
- Displays chat messages
- Manages user input
- Provides settings sidebar (clear conversation, info)

## Configuration

### Model Settings
You can modify the model in `chatbot.py`:
- Current: `llama-3.2b-vision-preview`
- Other Groq models available: Check [Groq documentation](https://console.groq.com/docs/models)

### Chat Parameters
In `chatbot.py`, you can adjust:
- `temperature`: Controls randomness (0.7 is default)
- `max_tokens`: Maximum response length (1024 is default)
- `top_p`: Nucleus sampling parameter

## API Key Security

⚠️ **Important**: The `.env` file contains your API key. 

For security best practices:
- Never commit `.env` files with real keys to version control
- Use `.env.example` as a template for other developers
- For production, use:
  - Environment variables
  - Secrets management services
  - CI/CD pipeline secret management

## Troubleshooting

### "GROQ_API_KEY environment variable not set"
- Make sure the `.env` file exists in the project root
- Check that your API key is correctly entered

### "ModuleNotFoundError: No module named 'groq'"
- Run `pip install -r requirements.txt` again
- Make sure your virtual environment is activated

### "Connection error" or "API error"
- Verify your Groq API key is valid
- Check your internet connection
- Ensure you haven't exceeded API rate limits

## Performance Tips

- Groq API is very fast! Response times are typically under 1 second
- The model maintains conversation history, so it remembers context
- Use the "Clear Conversation" button to start fresh if the context gets too long

## Future Enhancements

- Add support for multiple models
- Implement system prompts for custom bot personalities
- Add conversation export/import functionality
- Support for file uploads
- Rate limiting and usage statistics

## License

This project is open source and available for personal and educational use.

## Support

For issues with:
- **Streamlit**: Visit [Streamlit documentation](https://docs.streamlit.io/)
- **Groq API**: Check [Groq console](https://console.groq.com/)
- **This project**: Review the code comments in `app.py` and `chatbot.py`

---

**Enjoy your chatbot!** 🚀