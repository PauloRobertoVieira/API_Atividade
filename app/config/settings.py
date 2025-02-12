from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str  # Campo obrigatório

    class Config:
        env_file = ".env"  # Carrega variáveis de ambiente de um arquivo .env
        env_file_encoding = "utf-8"  # Codificação do arquivo .env

settings = Settings()  # Instância das configurações

# Teste temporário
print(f"Chave da API: {settings.openai_api_key}")