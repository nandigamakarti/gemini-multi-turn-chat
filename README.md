# 🤖 Gemini Multi-Turn Chat

An interactive chatbot application using Google's Gemini AI that maintains conversation context across multiple turns, with robust error handling and a visually appealing interface.

<div align="center">
  <img src="https://i.imgur.com/8wEwwQa.png" alt="Gemini AI Logo" width="250"/>
  <p><em>Powered by Google's Gemini 1.5 Flash model</em></p>
</div>

## ✨ Key Features

- 🧠 **Context-Aware Conversations** - Full conversation history preservation
- 🔄 **Unlimited Chat Turns** - Chat for as long as you want
- 🌡️ **Customizable Responses** - Adjust temperature to control AI creativity
- 💬 **User-Friendly Interface** - Intuitive console interface with emoji indicators
- 🛡️ **Smart Error Handling** - Automatic retries and helpful error messages
- ⌨️ **Graceful Exits** - Support for keyboard interrupts and exit commands
- 🔐 **Secure Credentials** - API key management via environment variables

## 📋 Requirements

- Python 3.6+
- Google API key for Gemini AI
- Internet connection

## 🚀 Quick Start Guide

### 1️⃣ Get Your API Key

First, you'll need a Google API key for Gemini:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create or sign in to your Google account
3. Click "Get API key" and copy your new key

### 2️⃣ Setup the Project

```bash
# Clone the repository
git clone https://github.com/yourusername/gemini-multi-turn-chat.git
cd gemini-multi-turn-chat

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

### 3️⃣ Start Chatting!

```bash
python gemini_chat.py
```

## 🎮 How to Use

### Temperature Setting

When you start the application, you'll be prompted to set a temperature value:

```
⚙️ Configure model parameters:
Enter temperature (default 0.7): 
```

🌡️ **Temperature Guide**:
- `0.0` - Most predictable, consistent responses
- `0.3` - Balanced, less variation but still creative
- `0.7` - Default, good balance of creativity and relevance
- `1.0` - Maximum creativity, more varied and unpredictable

### Chat Commands

During your chat session:
- Type your message and press Enter to send
- Type `exit` to end the conversation
- Press `Ctrl+C` at any time to quit

## 📝 Example Conversation

```
🚀 Initializing Gemini chat...
✅ Connected to Gemini AI successfully!
💬 Start chatting (type 'exit' when you want to end the conversation)

💬 Turn 1:
Enter your message (or type 'exit' to quit): What are the best practices for writing clean code?
🔄 Sending to Gemini...

🤖 Gemini's response:
Clean code is code that is easy to understand, maintain, and extend. Here are some best practices:

1. **Use meaningful names** for variables, functions, and classes
   - Names should clearly convey purpose and intent
   - Avoid single-letter names except for counters or temporary variables

2. **Keep functions small and focused**
   - Each function should do one thing and do it well
   - Aim for 20 lines or less per function

3. **Follow consistent formatting**
   - Use consistent indentation, spacing, and bracing styles
   - Follow language or team style guides

4. **Write meaningful comments**
   - Explain "why" not "what" (the code shows what)
   - Keep comments current as code changes

5. **Avoid deep nesting**
   - Return early to reduce indentation levels
   - Extract complex conditions into well-named functions

6. **Don't Repeat Yourself (DRY)**
   - Extract duplicated code into reusable functions
   - Use abstraction to eliminate repetition

7. **Write tests**
   - Unit tests verify functionality and prevent regressions
   - Tests document expected behavior

8. **Refactor regularly**
   - Continuously improve existing code
   - Address technical debt early

9. **Use proper error handling**
   - Handle exceptions appropriately
   - Fail fast and visibly

10. **Keep it simple**
    - Simple code is easier to understand and maintain
    - Avoid premature optimization

Remember that clean code is not just about following rules but about making thoughtful decisions that prioritize readability and maintainability.

💬 Turn 2:
Enter your message (or type 'exit' to quit): Can you give me an example of clean vs messy code?
🔄 Sending to Gemini...

🤖 Gemini's response:
Here's a comparison of messy code versus clean code in Python:

### Messy Code Example:

```python
def p(d, s=0):
    r = 0
    for i in range(len(d)):
        if (s == 0 and d[i] > 0) or (s == 1 and d[i] < 0):
            r += d[i]
    return r
```

### Clean Code Example:

```python
def sum_filtered_values(numbers, select_positive=True):
    """
    Sum values from the list based on whether they are positive or negative.
    
    Args:
        numbers: List of numeric values
        select_positive: If True, sum positive values; otherwise sum negative values
        
    Returns:
        Sum of filtered values
    """
    total = 0
    
    for number in numbers:
        if (select_positive and number > 0) or (not select_positive and number < 0):
            total += number
            
    return total
```

### What Makes the Clean Version Better:

1. **Meaningful names**: `sum_filtered_values` clearly describes what the function does, unlike `p`
   
2. **Readable parameters**: `numbers` and `select_positive` vs cryptic `d` and `s`
   
3. **Comments and documentation**: The clean version has a docstring explaining purpose, parameters, and return value
   
4. **Default parameter clarity**: `select_positive=True` is clearer than `s=0`
   
5. **Consistent naming**: The clean version uses consistent naming conventions
   
6. **Logical expression**: The boolean logic is more readable with explicit naming

Clean code might be longer, but it saves time in the long run by making maintenance and debugging much easier.

💬 Turn 3:
Enter your message (or type 'exit' to quit): exit
👋 Exiting chat. Thanks for using Gemini Chat!

✨ Chat session ended. Have a great day!
```

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| **API Key Not Found** | Check that your `.env` file exists with `GOOGLE_API_KEY=your_key` |
| **Connection Errors** | Verify your internet connection and try again |
| **Rate Limiting** | Wait a few minutes if you hit API rate limits |
| **Empty Responses** | Try rephrasing your question or check API quota |
| **Python Errors** | Ensure you have Python 3.6+ and required packages installed |

## 🛠️ Advanced Configuration

You can modify the code to:

- Change the Gemini model (1.5-flash, 1.5-pro, etc.)
- Adjust retry settings for API calls
- Save conversation history to files
- Implement system prompts for specific use cases

Check the code comments for guidance on these customizations.

## 🔒 Privacy & Security

- Your conversations are processed on Google's servers
- API keys should be kept confidential
- Review [Google's AI Privacy Policy](https://ai.google.dev/privacy) for details

## 📊 Resources

- [Google Generative AI Documentation](https://ai.google.dev/docs)
- [Gemini API Reference](https://ai.google.dev/api/python/google/generativeai)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

## 📜 License

[MIT License](LICENSE)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin amazing-feature`)
5. Open a Pull Request

---

<div align="center">
  <p>Made with ❤️ by Your Name</p>
  <p>⭐ Star this repo if you found it useful! ⭐</p>
</div> 