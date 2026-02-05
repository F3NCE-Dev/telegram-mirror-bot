from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str = "Bot_token"
    DATABASE_URL: str = "sqlite:///bot.db"

    class Config:
        env_file = ".env"

settings = Settings()
