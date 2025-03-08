import openai

openai.api_key = "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"

def chatbot_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5",  # or gpt-4
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_input = input("Ask the chatbot: ")
    print(chatbot_response(user_input))
