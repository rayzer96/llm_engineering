from openai import OpenAI
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

MODEL = "gpt-oss:20b"

messages = [
    {"role": "system", "content": "You are a code expert"},
    {"role": "user", "content": "Write a Python script that generates an image of a black and white long haired cat using different types of models and saves it as 'cat_image.png'."}
    ]
response = openai.chat.completions.create(
    model=MODEL,
    messages=messages
)

print(response.choices[0].message.content)

#