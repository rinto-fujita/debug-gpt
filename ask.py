import openai

openai.api_key = "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"

ask_gpt = input('How can I help you?😀：')

chat_completion = openai.ChatCompletion.create(
model="gpt-3.5-turbo-16k",
messages=[
        {"role": "system", "content": "あなたはpythonのデバッグの助けになってくれるアシスタントです"},
        {"role": "user", "content": ask_gpt},
        {"role": "user", "content": '短い回答をお願いします'}
    ]
)

response = chat_completion["choices"][0]["message"]["content"]
print(response)
