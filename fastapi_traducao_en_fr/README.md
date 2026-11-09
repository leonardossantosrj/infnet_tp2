# Parte 1, Questão 2: tradutor inglês-francês com FastAPI

API em FastAPI que recebe um texto em inglês e o traduz para o francês com o modelo `Helsinki-NLP/opus-mt-en-fr` da HuggingFace, pela biblioteca `transformers`.

## Requisitos

- Python 3.10 ou mais recente

## Como executar

1. Entre na pasta do projeto:
   ```
   cd p1q2-fastapi-traducao-en-fr
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
  "traducao": "<texto traduzido para o francês>"
}
```

## Observações

- Na primeira execução, o modelo é baixado da HuggingFace (algumas centenas de MB). Depois fica salvo no computador.
- Textos longos são divididos em frases antes da tradução, para não passar do limite de tamanho do modelo.
- O `transformers` está fixado na versão 4.57.6 porque a versão 5 removeu o pipeline de tradução.
