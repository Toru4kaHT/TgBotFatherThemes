import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TOKEN: str
    ADMINS: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(".env")
    )

settings = Settings()