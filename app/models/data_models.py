from pydantic import BaseModel


class CourseData(BaseModel):
    id_curso: int
    curso: str
    ano: int
    modalidade: str
    vagas_novas: int
    candidatos_novos: int


class Question(BaseModel):
    question: str