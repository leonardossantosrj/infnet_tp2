# Parte 2, Questão 1: chatbot com Fake LLM, LangChain e FastAPI

Protótipo de chatbot: a API em FastAPI recebe uma mensagem, monta o prompt com o LangChain e devolve a resposta de um Fake LLM (`FakeListLLM`), que simula um LLM real sem custo e sem internet.

## Requisitos

- Python 3.10 ou mais recente

## Como executar

1. Entre na pasta do projeto:
   ```
   cd p2q1-langchain-fake-llm
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
4. Suba a API:
   ```
   python -m uvicorn main:app --reload
   ```

## Como testar

**Pelo navegador:** abra http://127.0.0.1:8000/docs, clique na rota `POST /chat`, depois em **Try it out**, preencha o JSON e clique em **Execute**.

**Pelo terminal:**
```
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"mensagem": "Qual o horário de atendimento?"}'
```

**Formato da resposta:**
```json
{
  "pergunta": "Qual o horário de atendimento?",
  "resposta": "Atendemos de segunda a sexta, das 9h às 18h."
}
```

## Observações

- Perguntas pré-definidas: `oi`, `qual o horário de atendimento?`, `como abro um chamado?` e `tchau` (maiúsculas e minúsculas não importam).
- Qualquer outra pergunta recebe a resposta padrão: "Desculpe, não sei responder essa pergunta."
- Não precisa de chave de API nem de download de modelo.
