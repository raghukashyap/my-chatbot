def get_user_query():
    user_query = input("Enter your search query: ")
    search_results = search_query(user_query)
    search_content = "\n".join([result['snippet'] for result in search_results])
    chatgpt_response = process_with_chatgpt(search_content)
    print(f"ChatGPT Response: {chatgpt_response}")

# Start the interaction with the user
get_user_query()
