from pydantic import BaseModel
from enum import Enum


class CourseData(BaseModel):
    id_curso: int
    curso: str
    ano: int
    modalidade: str
    vagas_novas: int
    candidatos_novos: int


class Question(BaseModel):
    question: str

class Tags(str, Enum):
    curso = "Busca cursos"
    ia = "Implementação com IA"
    logs = "Logs"