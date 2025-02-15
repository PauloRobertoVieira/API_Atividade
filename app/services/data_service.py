import pandas as pd
from app.utils.logger import logger
import unicodedata

def normalize_text(text):
    return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8").lower()

class DataService:
    def __init__(self, file_path):
        self.data = pd.read_excel(file_path, engine="openpyxl")

        
    def get_course_data(self, course_id):
        course = self.data[self.data['ID_CURSO'] == course_id]
        if course.empty:
            logger.error(f'O curso com ID {course_id} não foi encontrado.')
            return None
        
        course = course.rename(columns={
            "ID_CURSO": "id_curso",
            "CURSO": "curso",
            "ANO": "ano",
            "MODALIDADE": "modalidade",
            "VAGAS NOVAS": "vagas_novas",
            "CANDIDATOS NOVOS": "candidatos_novos"
        })

        return course.to_dict(orient='records')[0] 
    
    def get_course_nome_ano(self, course_nome, curso_ano):
        
        self.data['CURSO_NORMALIZADO'] = self.data['CURSO'].apply(normalize_text)

        course_nome = normalize_text(course_nome)

        course = self.data[(self.data['CURSO_NORMALIZADO'] == course_nome) & (self.data['ANO'] == curso_ano)]

        if course.empty:
            logger.error(f'O curso com nome {course_nome} do ano {curso_ano} não foi encontrado.')
            return None
        
        course = course.rename(columns={
            "ID_CURSO": "id_curso",
            "CURSO": "curso",
            "ANO": "ano",
            "MODALIDADE": "modalidade",
            "VAGAS NOVAS": "vagas_novas",
            "CANDIDATOS NOVOS": "candidatos_novos"
        })

        return course.to_dict(orient='records')[0]
