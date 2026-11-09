import re

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Tradutor inglês-francês com Helsinki-NLP")

tradutor = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")


class Entrada(BaseModel):
    texto: str


@app.post("/traduzir")
def traduzir(entrada: Entrada):
    frases = re.split(r"(?<=[.!?])\s+", entrada.texto.strip())
    resultados = tradutor(frases)
    traducao = " ".join(r["translation_text"] for r in resultados)
    return {"texto_original": entrada.texto, "traducao": traducao}
