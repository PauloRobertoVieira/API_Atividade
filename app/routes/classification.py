from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.ai_service import AIService
from app.utils.security import verify_token
from app.utils.logger import logger

router = APIRouter(prefix="/v1")
security = HTTPBearer()
ai_service = AIService()

@router.post("/classifica-curso", summary="Classifica curso", description="Descrição")
async def classify_course(description: str, credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials)
    classification = ai_service.classify_course(description)
    logger.info(f"Curso classificado: {classification}")
    return {"classification": classification}