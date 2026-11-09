from fastapi import FastAPI
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from pydantic import BaseModel

app = FastAPI(title="Tradutor inglês-alemão com HuggingFace e LangChain")


llm = HuggingFacePipeline.from_model_id(
    model_id="Helsinki-NLP/opus-mt-en-de",
    task="translation",
)


prompt = PromptTemplate.from_template("{texto}")

cadeia = prompt | llm


class Entrada(BaseModel):
    texto: str


@app.post("/traduzir")
def traduzir(entrada: Entrada):
    traducao = cadeia.invoke({"texto": entrada.texto})
    return {"texto_original": entrada.texto, "traducao": traducao}
