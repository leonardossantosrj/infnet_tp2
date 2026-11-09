# Parte 2, Questão 2: tradutor inglês-francês com OpenAI, LangChain e FastAPI

API em FastAPI que recebe um texto em inglês e o traduz para o francês com o modelo `gpt-5.4-nano` da OpenAI, chamado pelo LangChain (`ChatOpenAI`).

## Requisitos

- Python 3.10 ou mais recente

## Como executar

1. Entre na pasta do projeto:
   ```
   cd p2q2-langchain-openai-en-fr
   ```
2. Crie e ative o ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows
   ```
3. Instale as bibliotecas:
   ```
   python -m pip install -r requirements.txt
   ```
4. Configure a chave da OpenAI. Copie o arquivo de exemplo e coloque a sua chave nele:
   ```
   cp .env.example .env
   ```
   Abra o `.env` e troque `coloque-sua-chave-aqui` pela sua chave, criada em https://platform.openai.com/api-keys. O `.env` está no `.gitignore` e não vai para o GitHub.
5. Suba a API:
   ```
   python -m uvicorn main:app --reload
   ```

## Como testar

**Pelo navegador:** abra http://127.0.0.1:8000/docs, clique na rota `POST /traduzir`, depois em **Try it out**, preencha o JSON e clique em **Execute**.

**Pelo terminal:**
```
curl -X POST "http://127.0.0.1:8000/traduzir" \
  -H "Content-Type: application/json" \
  -d '{"texto": "Hello, how are you? The weather is nice today."}'
```

**Formato da resposta:**
```json
{
  "texto_original": "Hello, how are you? The weather is nice today.",
  "traducao": "<texto traduzido para o francês>"
}
```

## Observações

- Cada chamada consome créditos da conta da OpenAI.
- O `gpt-5.4-nano` foi escolhido por ser o modelo mais rápido e barato da OpenAI. Para trocar, altere o parâmetro `model` no `main.py`.
- O cliente da OpenAI é criado uma vez, quando a API sobe, com `timeout=30` segundos e até 2 novas tentativas em caso de falha.
