# Parte 2, Questão 3: tradutor inglês-alemão com HuggingFace, LangChain e FastAPI

API em FastAPI que recebe um texto em inglês e o traduz para o alemão com o modelo `Helsinki-NLP/opus-mt-en-de` da HuggingFace, carregado e chamado pelo LangChain (`HuggingFacePipeline`).

## Requisitos

- Python 3.10 ou mais recente

## Como executar

1. Entre na pasta do projeto:
   ```
   cd p2q3-langchain-huggingface-en-de
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
  "traducao": "<texto traduzido para o alemão>"
}
```

## Observações

- Na primeira execução, o modelo é baixado da HuggingFace (algumas centenas de MB). Depois fica salvo no computador.
- O modelo roda no próprio computador, sem chave de API.
- O `transformers` está fixado na versão 4.57.6 porque a versão 5 removeu o pipeline de tradução, que o `HuggingFacePipeline` usa.
