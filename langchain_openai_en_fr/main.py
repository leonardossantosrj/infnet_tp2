from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

load_dotenv()  

app = FastAPI(title="Tradutor inglês-francês com OpenAI e LangChain")


llm = ChatOpenAI(model="gpt-5.4-nano", timeout=30, max_retries=2)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the user's text from English to French. Reply only with the translation."),
        ("user", "{texto}"),
    ]
)

cadeia = prompt | llm | StrOutputParser()


class Entrada(BaseModel):
    texto: str


@app.post("/traduzir")
def traduzir(entrada: Entrada):
    traducao = cadeia.invoke({"texto": entrada.texto})
    return {"texto_original": entrada.texto, "traducao": traducao}
