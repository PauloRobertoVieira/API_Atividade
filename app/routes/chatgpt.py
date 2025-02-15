from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.chatgpt_service import ChatGPTService
from app.models.data_models import Question
from app.utils.security import verify_token
from app.utils.logger import logger
from app.services.data_service import DataService

data_service = DataService('2022_2023.xlsx')
chatgpt_service = ChatGPTService(data_service)

router = APIRouter(prefix="/v1")
security = HTTPBearer()

@router.post("/pergunta-chatgpt", summary="Pergunta para o chatgpt", description="Descrição")
async def ask_chatgpt(question: Question, credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials)
    answer = chatgpt_service.ask_question(question.question)
    logger.info(f"Resposta do ChatGPT: {answer}")
    return {"answer": answer}
