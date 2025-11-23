from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str
    DATABASE_URL: str
    SECRET_KEY: str
    
    # Argon2 settings
    ARGON2_TIME_COST: int = 2
    ARGON2_MEMORY_COST: int = 19456
    ARGON2_PARALLELISM: int = 1

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
