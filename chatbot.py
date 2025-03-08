from dotenv import load_dotenv
import openai
import os

# openai.api_key = "#############"

# Load environment variables from the .env file
load_dotenv()

# Get API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to interact with the chatbot using the new API
def chatbot_response(prompt):
     response = openai.completions.create(
        model="gpt-3.5-turbo",  # Or use gpt-4 if you have access
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

if __name__ == "__main__":
    user_input = input("Ask the chatbot: ")
    print(chatbot_response(user_input))
