from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str
    api_secret_token: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings() 