import openai

say = input('say:')

# apikey
openai.api_key = "AIGC10241-EpfPi81JulQLPixe0jyWTVHexOSl59"

# api-url
openai.api_base = "https://api.aigc2d.com/v1"

# ChatGPT4
res4 = openai.ChatCompletion.create(
    max_tokens=1000,
    model="gpt-4",
    messages=[{"role": "user",
               "content": say}],
)

print(res4)