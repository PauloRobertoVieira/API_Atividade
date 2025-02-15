from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.data_service import DataService
from app.models.data_models import CourseData, Tags
from app.utils.security import verify_token
from app.utils.logger import logger

router = APIRouter(prefix="")
security = HTTPBearer()
data_service = DataService('2022_2023.xlsx')

description_v1 = "Retorna dados de um curso específico com base no ID informado."

@router.get("/v1/curso/{course_id}", response_model=CourseData, summary="Retorna dados de um curso", description=description_v1, tags=[Tags.curso])
async def get_course(course_id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials)
    course = data_service.get_course_data(course_id)
    if not course:
        logger.error(f"Curso com ID {course_id} não encontrado")
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    logger.info(f"Curso com ID {course_id} retornado com sucesso")
    return course



description_v2 = "Retorna dados de um curso específico com base no nome e ano informados."

@router.get("/v2/curso/{course_nome}/{course_ano}", response_model=CourseData, summary="Retorna dados de um curso", description=description_v2, tags=[Tags.curso])
async def get_course(course_nome: str, course_ano: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials)
    course = data_service.get_course_nome_ano(course_nome, course_ano)
    if not course:
        logger.error(f"Curso com nome {course_nome} do ano {course_ano} não encontrado")
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    logger.info(f"Curso {course_nome} de {course_ano} retornado com sucesso")
    return course