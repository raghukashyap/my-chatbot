import openai

openai.api_key = "your-api-key-here"

def chatbot_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4",  # or gpt-3.5
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_input = input("Ask the chatbot: ")
    print(chatbot_response(user_input))
