import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TOKEN: str
    ADMINS: str
    BASE_URL: str
    WEBHOOK_PATH: str
    HOST: str
    PORT: int

    model_config = SettingsConfigDict(
        env_file=os.path.join(".env")
    )

settings = Settings()