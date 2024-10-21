from openai import OpenAI

secret_key = ""
prompt = "Tell me last ten world cup winners"

client = OpenAI(api_key=secret_key)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ],
  max_tokens=100,
  temperature=1,
)

print(completion.choices[0].message.content)
