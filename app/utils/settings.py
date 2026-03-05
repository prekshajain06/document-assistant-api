from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str
    ENV: str
    DB_CONNECTION: str
    SECRET_KEY: str
    ALGORITHM: str
    EXPIRE_TIME_MINUTES: int
    UPLOAD_FOLDER: str

settings = Settings()
