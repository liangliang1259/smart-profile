from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Smart Profile"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A smart personal profile generator"
    
    # Database settings
    DATABASE_URL: str = "mysql+pymysql://root:password@localhost/smart_profile"
    
    # Redis settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    # JWT settings
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Kimi AI API settings
    KIMI_API_KEY: Optional[str] = None
    KIMI_API_URL: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
