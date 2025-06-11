# Context-Aware Gemini Chat

A simple Streamlit application that allows you to chat with Google's Gemini AI model while maintaining conversation context.

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Google AI API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```
   streamlit run app.py
   ```

## Features

- Interactive chat interface
- Maintains conversation context across turns
- Allows adjusting temperature parameter to influence response creativity
- Uses Gemini 1.5 Flash model 