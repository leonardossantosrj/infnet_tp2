API em FastAPI que recebe uma frase em JSON e usa o modelo GPT-2 da HuggingFace, pela biblioteca `transformers`, para gerar a continuação do texto.

## Requisitos

- Python 3.10 ou mais recente

## Como executar

1. Entre na pasta do projeto:
   ```
   cd p1q1-fastapi-gpt2
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

**Pelo navegador:** abra http://127.0.0.1:8000/docs, clique na rota `POST /gerar`, depois em **Try it out**, preencha o JSON e clique em **Execute**.

**Pelo terminal:**
```
curl -X POST "http://127.0.0.1:8000/gerar" \
  -H "Content-Type: application/json" \
  -d '{"texto": "Artificial intelligence will"}'
```

**Formato da resposta:**
```json
{
  "entrada": "Artificial intelligence will",
  "texto_gerado": "Artificial intelligence will <continuação gerada pelo GPT-2>"
}
```

## Observações

- Na primeira execução, o modelo `openai-community/gpt2` é baixado da HuggingFace (algumas centenas de MB). Depois fica salvo no computador.
- O texto gerado muda a cada chamada, porque o GPT-2 sorteia as próximas palavras.
- `max_new_tokens=50` limita a continuação a cerca de 50 tokens.