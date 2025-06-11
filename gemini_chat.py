import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

def get_valid_temperature():
    """Get a valid temperature value from the user."""
    while True:
        try:
            temp = float(input("Enter temperature (default 0.7): ").strip() or "0.7")
            if 0 <= temp <= 1:
                return temp
            print("🔍 Temperature must be between 0 and 1. Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number between 0 and 1.")
        except KeyboardInterrupt:
            print("\n👋 Chat setup cancelled. Goodbye!")
            sys.exit(0)

def initialize_gemini(api_key, temperature=0.7):
    """Initialize the Gemini model with the given API key and temperature."""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash',
                                    generation_config=genai.types.GenerationConfig(
                                        temperature=temperature
                                    ))
        return model
    except Exception as e:
        print(f"❌ Unable to initialize Gemini model: {str(e)}")
        print("🔍 Please check your internet connection and API key validity.")
        sys.exit(1)

def get_user_input(prompt):
    """Get input from the user with the given prompt."""
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print("\n👋 Chat cancelled. Goodbye!")
        sys.exit(0)

def send_message_with_retry(chat, message, max_retries=3):
    """Send a message to the chat with retry logic."""
    retries = 0
    while retries < max_retries:
        try:
            return chat.send_message(message)
        except Exception as e:
            retries += 1
            if retries >= max_retries:
                print(f"❌ Failed to get a response after {max_retries} attempts.")
                print(f"🔍 Error details: {str(e)}")
                print("💡 Try again with a different query or check your connection.")
                return None
            print(f"⚠️ Communication error (attempt {retries}/{max_retries}): {str(e)}")
            print("🔄 Retrying...")

def main():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variable
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("❌ API key not found!")
            print("💡 Please create a .env file in the project folder with:")
            print("   GOOGLE_API_KEY=your_api_key_here")
            print("🔗 Get your API key from: https://makersuite.google.com/app/apikey")
            return

        # Get temperature from user
        print("\n⚙️ Configure model parameters:")
        temperature = get_valid_temperature()

        # Initialize chat
        print("\n🚀 Initializing Gemini chat...")
        try:
            model = initialize_gemini(api_key, temperature)
            chat = model.start_chat(history=[])
            print("✅ Connected to Gemini AI successfully!")
            print("💬 Start chatting (type 'exit' when you want to end the conversation)")
        except Exception as e:
            print(f"❌ Failed to initialize chat: {str(e)}")
            print("🔍 Please check your internet connection and try again.")
            return

        # Chat loop
        turn_count = 1
        while True:
            print(f"\n💬 Turn {turn_count}:")
            user_input = get_user_input("Enter your message (or type 'exit' to quit): ")
            
            if user_input.lower() == 'exit':
                print("👋 Exiting chat. Thanks for using Gemini Chat!")
                break
                
            if not user_input:
                print("⚠️ Message cannot be empty. Please try again.")
                continue
                
            print("🔄 Sending to Gemini...")
            response = send_message_with_retry(chat, user_input)
            if response:
                print("\n🤖 Gemini's response:")
                print(response.text)
            else:
                print("❌ Failed to get a response.")
                print("💡 Try rephrasing your message or check your connection.")
            
            turn_count += 1
            
    except KeyboardInterrupt:
        print("\n👋 Chat cancelled by user. Goodbye!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {str(e)}")
        print("💡 Please try restarting the application.")
    finally:
        print("\n✨ Chat session ended. Have a great day!")

if __name__ == "__main__":
    main() 