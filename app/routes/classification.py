from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.data_service import DataService
from app.utils.security import verify_token
from app.utils.logger import logger

router = APIRouter(prefix="/v1")
security = HTTPBearer()
data_service = DataService('2022_2023.xlsx')

descricao = "Classifica um curso com IA, considerando a modalidade, grau, ano e quantidade concluintes."

@router.post("/classifica-curso", summary="Classifica um curso com IA", description=descricao)
async def classify_course(course_name: str, credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials)
    df = data_service.data

    filtered = df[df['CURSO'].str.contains(course_name, case=False, na=False)]
    if filtered.empty:
        logger.error(f"Curso {course_name} não encontrado.")
        raise HTTPException(status_code=404, detail="Curso não encontrado.")

    row = filtered.iloc[0]
    curso = row['CURSO']
    modalidade = row['MODALIDADE']
    
    grau = "Licenciatura" if "Licenciatura" in curso else "Bacharelado"

    dados_2022 = filtered[filtered['ANO'] == 2022]
    dados_2023 = filtered[filtered['ANO'] == 2023]

    vagas_2022 = dados_2022['VAGAS NOVAS'].sum() if not dados_2022.empty else 0
    vagas_2023 = dados_2023['VAGAS NOVAS'].sum() if not dados_2023.empty else 0

    concluintes_2022 = dados_2022['CONCLUINTES'].sum() if 'CONCLUINTES' in dados_2022.columns and not dados_2022.empty else 0
    concluintes_2023 = dados_2023['CONCLUINTES'].sum() if 'CONCLUINTES' in dados_2023.columns and not dados_2023.empty else 0

    response_text = (
        f"O curso {curso} é ofertado na modalidade {modalidade} com grau acadêmico {grau}. "
        f"Em 2022, foram ofertadas {vagas_2022} vagas novas e {concluintes_2022} alunos concluíram o curso. "
        f"Em 2023, foram ofertadas {vagas_2023} vagas novas e {concluintes_2023} alunos concluíram o curso."
    )

    logger.info(f"Curso classificado: {response_text}")
    return {"classification": response_text}
