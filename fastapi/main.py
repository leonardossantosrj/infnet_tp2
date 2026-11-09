from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Gerador de texto com GPT-2")

gerador = pipeline("text-generation", model="openai-community/gpt2")

class Entrada(BaseModel):
    texto: str


@app.post("/gerar")
def gerar_texto(entrada: Entrada):
    resultado = gerador(entrada.texto, max_new_tokens=50)
    return {"entrada": entrada.texto, "texto_gerado": resultado[0]["generated_text"]}
