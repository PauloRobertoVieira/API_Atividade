import openai
from app.config.settings import settings
from app.utils.logger import logger

client = openai.OpenAI(api_key=settings.openai_api_key)

class AIService:
    def classify_course(self, course_description):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Você é um assistente que conhece censo da educação no Brasil, especificamente Censo da UFG planilha 2022_2023."},
                    {"role": "user", "content": f"Classifique o curso: {course_description}"}
                ],
                max_tokens=50
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f'Erro ao classificar o curso: {e}')
            raise
