from fastapi import FastAPI
from langchain_core.language_models import FakeListLLM
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel

app = FastAPI(title="Chatbot com Fake LLM")

# Perguntas pré-definidas e as respostas que o Fake LLM vai devolver
RESPOSTAS = {
    "oi": "Olá! Como posso ajudar?",
    "qual o horário de atendimento?": "Atendemos de segunda a sexta, das 9h às 18h.",
    "como abro um chamado?": "Envie um e-mail para o suporte com a descrição do problema.",
    "tchau": "Até logo!",
}
RESPOSTA_PADRAO = "Desculpe, não sei responder essa pergunta."

prompt = PromptTemplate.from_template("Usuário: {mensagem}\nAssistente:")


class Pergunta(BaseModel):
    mensagem: str


@app.post("/chat")
def chat(pergunta: Pergunta):
    resposta = RESPOSTAS.get(pergunta.mensagem.lower().strip(), RESPOSTA_PADRAO)

    
    llm = FakeListLLM(responses=[resposta])

    cadeia = prompt | llm
    return {"pergunta": pergunta.mensagem, "resposta": cadeia.invoke({"mensagem": pergunta.mensagem})}
