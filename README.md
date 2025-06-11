# 🤖 Gemini Multi-Turn Chat

A versatile project demonstrating context-aware conversations using Google's Gemini AI model in both console and web interfaces.

## 📱 Interfaces

### Streamlit Web App
An interactive web application that allows you to chat with Google's Gemini AI model while maintaining conversation context.

### Console Chatbot
A simple console-based chatbot that demonstrates multi-turn conversations using Google's Gemini API.

## 🌟 What This Project Does

This project creates chat applications that:

- Initialize a Gemini chat session using the "gemini-1.5-flash" model
- Prompt the user for inputs and send them to Gemini
- Preserve context between messages for natural conversations
- Display responses from Gemini
- Allow customization of the temperature parameter to control response creativity

## 🚀 How to Run

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key

### Setup

1. **Clone Repository**

   ```bash
   git clone https://github.com/nandigamakarti/gemini-multi-turn-chat.git
   cd gemini-multi-turn-chat
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   - Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the same directory as the script with the following content:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     ```


### Running the Console Application

```bash
python gemini_chat.py
```

#### Using the Console Application:

1. Enter a temperature value
   - Lower values (e.g., 0.2) for more focused, deterministic responses
   - Higher values (e.g., 0.8) for more creative, varied responses
2. Follow the prompts
   - Enter your first message
   - View Gemini's response
   - Enter your second message (follow-up or additional detail)
   - Continue the conversation naturally
   - Type 'bye' when you want to exit

## 🔒 Security Note

The `.env` file contains your API key and should not be shared or committed to version control. A `.gitignore` file has been included to prevent this.

## 🛠️ Features & Error Handling

- Interactive chat interface (web and console versions)
- Maintains conversation context across turns
- Allows adjusting temperature parameter
- Uses Gemini 1.5 Flash model
- Error handling for:
  - Missing API key
  - Invalid temperature values
  - API errors during conversation

## 📝 Example Conversation

```
Welcome to the Gemini Console Chatbot!

Enter temperature (0.0-1.0, lower for deterministic, higher for creative): 0.7

Chat started! Context will be preserved between messages.

Enter your first message: What are the main features of Python?

Gemini: Python has several key features that make it popular among developers:

Easy to Learn and Read: Python's syntax is clear and intuitive, resembling English.

Interpreted Language: Code executes line by line, making debugging easier.

Dynamically Typed: No need to declare variable types explicitly.

Object-Oriented: Supports object-oriented programming paradigms.

Extensive Standard Library: Comes with a rich set of modules and packages.

Cross-Platform: Works on various operating systems (Windows, macOS, Linux).

High-Level Language: Abstracts complex details from the programmer.

Versatile Applications: Used in web development, data science, AI, automation, etc.

Strong Community Support: Large community contributing to libraries and frameworks.

Free and Open Source: Available for anyone to use and modify.

Enter your second message (follow-up or additional detail): Which of these features make it good for data science specifically?

Gemini: Python excels in data science due to several of its features:

Rich Ecosystem of Libraries: Python offers specialized libraries like NumPy (for numerical computing), pandas (for data manipulation), Matplotlib and Seaborn (for visualization), scikit-learn (for machine learning), and TensorFlow/PyTorch (for deep learning).

Easy to Learn and Read: Data scientists can focus on analyzing data rather than complex syntax, making it accessible to those without extensive programming backgrounds.

Interpreted Nature: Allows for interactive data exploration in notebooks like Jupyter, enabling iterative analysis and immediate visualization of results.

Versatility: Can handle various aspects of the data science workflow from data cleaning and preprocessing to modeling and deployment.

Integration Capabilities: Easily interfaces with other languages (like R, SQL, C++) and data sources.

Community Support: Extensive documentation, tutorials, and forums specifically for data science applications.

Reproducibility: Tools like virtual environments and notebooks make it easier to share and reproduce analyses.

Scalability: Can handle everything from small datasets on a laptop to big data processing with frameworks like PySpark.

Visualization Tools: Rich visualization capabilities make communicating insights straightforward.

Free and Open Source: Accessibility to everyone, including students, researchers, and organizations of all sizes.

You: Can you recommend some good Python libraries for beginners in data science?

Gemini: Absolutely! For beginners in data science with Python, I recommend starting with these libraries:

pandas: Essential for data manipulation and analysis. It provides data structures like DataFrames that make working with structured data intuitive.

NumPy: The foundation for numerical computing in Python. It provides efficient array operations and mathematical functions.

Matplotlib: The most basic visualization library. It's great for creating standard plots and understanding visualization fundamentals.

Seaborn: Built on Matplotlib but provides a higher-level interface for creating attractive statistical graphics with less code.

scikit-learn: Perfect for beginners in machine learning. It has consistent APIs, good documentation, and implements many common algorithms.

Jupyter Notebooks: Not a library per se, but an interactive environment that's excellent for learning and experimenting with code.

Start with simple projects like:

Data cleaning and exploration with pandas
Basic visualizations with Matplotlib/Seaborn
Simple predictive models with scikit-learn
As you grow more comfortable, you can explore more specialized libraries like TensorFlow or PyTorch for deep learning, or Plotly for interactive visualizations.

You: bye

Conversation ended. Thank you for using Gemini Console Chatbot! 
