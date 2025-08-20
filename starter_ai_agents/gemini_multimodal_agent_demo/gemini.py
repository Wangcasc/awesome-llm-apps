import os
import google.generativeai as genai

# 配置 API key
os.environ['GOOGLE_API_KEY'] = "Your API Key"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
# 配置模型
model = genai.GenerativeModel('')

# 提出问题，生成回答
response = model.generate_content("List 5 planets each with an interesting fact")
print(response.text)

# 提出问题，生成回答
response = model.generate_content("what are top 5 frequently used emojis?")
print(response.text)
