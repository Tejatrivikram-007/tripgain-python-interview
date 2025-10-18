from google import genai
from config import genai_key

client = genai.Client(api_key = genai_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)











# from config import genaikey1
# from config import openaikey
# client = OpenAI(api_key=genaikey)

# res = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": "Tell me a joke"}]
# )
# print(res.choices[0].message.content)