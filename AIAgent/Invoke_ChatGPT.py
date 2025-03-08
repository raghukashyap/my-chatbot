def process_with_chatgpt(query):
    # Call OpenAI API (GPT-4) to summarize or process the query
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Provide a concise summary of the following search results:\n\n{query}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example of processing with ChatGPT
user_query = "latest trends in AI"
search_results = search_query(user_query)
search_content = "\n".join([result['snippet'] for result in search_results])
chatgpt_response = process_with_chatgpt(search_content)

print(f"ChatGPT Response: {chatgpt_response}")
