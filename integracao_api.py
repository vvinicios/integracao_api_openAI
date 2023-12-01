import openai
import dotenv
import os

# Identificar api_key
dotenv.load_dotenv()
openai.api_key = os.getenv("openai_api_key")

# Testando resposta
resposta = openai.chat.completions.create(
  model = "gpt-3.5-turbo",
    messages = [
      {
       "role" : "system",
         "content" : "Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário."
      },
      {
       "role" : "user",
         "content" : "Gere 5 produtos"
         }
    ],

temperature=1,
max_tokens=256,
top_p=1,
frequency_penalty=0,
presence_penalty=0

)

print(resposta)
