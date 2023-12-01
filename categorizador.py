import openai
import dotenv
import os

# Identificar api_key
dotenv.load_dotenv()
openai.api_key=os.getenv("openai_api_key")

# Engenharia de prompt
prompt_sistema = """
Você é um categorizador de produtos.
Você deve escolher uma categoria da lista abaixo:
##### Lista de categorias válidas
Beleza e Saúde
Entretenimento
Esportes
##### Exemplo
bola de tênis
Esportes
"""
resposta = openai.chat.completions.create(
  model = "gpt-3.5-turbo",
  messages = [
    {
      "role": "system",
      "content": prompt_sistema
    },
    {
      "role": "user",
      "content": "escova de dentes"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  n=5
)

# Testando a consistencia das respostas
for i in range(0,5):
    print(resposta.choices[i].message.content)
    print("--------------")