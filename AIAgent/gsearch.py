import openai
from googleapiclient.discovery import build

# Set up the API keys
OPENAI_API_KEY = 'your-openai-api-key'
GOOGLE_API_KEY = 'your-google-api-key'
SEARCH_ENGINE_ID = 'your-custom-search-engine-id'

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def search_query(query):
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID).execute()
    return res['items']

# Example: Search for something
results = search_query('latest trends in AI')
for result in results:
    print(result['title'], result['link'])
