import openai

# Point to your proxy
openai.api_base = "http://localhost:8000/v1"
openai.api_key = "your_proxy_api_key"  # If you set PROXY_API_KEY

# Use OpenAI API as usual
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
