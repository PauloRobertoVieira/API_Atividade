from fastapi import FastAPI
from app.routes import course, classification, chatgpt, log


description = """
    Construção de API - Pós Graduação Agentes Inteligentes",
    - /v1/curso/: Retorna dados de um curso
    - /v1/classifica-curso: Classifica um curso com IA
    - /v1/pergunta-chatgpt: Faz uma pergunta ao ChatGPT.
"""


app = FastAPI(
    title="Trabalho Disciplina API",
    description=description,
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "names": "Marcos, Patrick e Paulo",
        "url": "http://example.com/contact",
        "email": "equipe_api@yahoo.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(course.router)
app.include_router(classification.router)
app.include_router(chatgpt.router)
app.include_router(log.router)