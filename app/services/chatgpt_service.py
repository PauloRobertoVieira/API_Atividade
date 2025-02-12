import openai
import pandas as pd
from app.config.settings import settings
from app.utils.logger import logger

client = openai.OpenAI(api_key=settings.openai_api_key)

class ChatGPTService:
    def __init__(self, data_service):
        self.data_service = data_service  # Passando o serviço de dados

    def ask_question(self, question):
        try:
            # Primeiro, tenta obter dados relevantes do arquivo
            data_context = self.process_question(question)

            if data_context:
                context_str = f"Baseado nos dados do censo educacional da UFG (2022-2023), aqui estão algumas informações relevantes: {data_context}"
            else:
                context_str = "Não encontrei informações específicas no arquivo. Responda com base no seu conhecimento geral."

            # Envia ao ChatGPT
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Você agora se chama Guilherme."},
                    {"role": "user", "content": f"{context_str}\nPergunta: {question}"}
                ],
                max_tokens=150
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f'Erro ao responder a pergunta: {e}')
            raise

    def process_question(self, question):
        """
        Processa a pergunta e tenta obter informações do arquivo 2022_2023.xlsx.
        """
        try:
            if "maior quantidade de candidatos novos" in question and "2022" in question:
                df = self.data_service.data
                max_curso = df.loc[df['ANO'] == 2022, ['CURSO', 'CANDIDATOS NOVOS']].nlargest(1, 'CANDIDATOS NOVOS')
                
                if not max_curso.empty:
                    return f"O curso com maior quantidade de candidatos novos em 2022 foi {max_curso.iloc[0]['CURSO']} com {max_curso.iloc[0]['CANDIDATOS NOVOS']} candidatos."
                
            return None  # Caso não encontre correspondência direta
        except Exception as e:
            logger.error(f"Erro ao processar a pergunta: {e}")
            return None
