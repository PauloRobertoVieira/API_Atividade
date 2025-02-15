from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.data_service import DataService
from app.models.data_models import CourseData
from app.utils.security import verify_token
from app.utils.logger import logger

router = APIRouter(prefix="/v1")
security = HTTPBearer()
data_service = DataService('2022_2023.xlsx')

@router.get("/curso/{course_id}", response_model=CourseData, summary="Busca curso", description="Descrição")
async def get_course(course_id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials)
    course = data_service.get_course_data(course_id)
    if not course:
        logger.error(f"Curso com ID {course_id} não encontrado")
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    logger.info(f"Curso com ID {course_id} retornado com sucesso")
    return course