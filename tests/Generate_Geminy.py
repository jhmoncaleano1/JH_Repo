from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Write a story about a magic backpack."
)
print(response.text)