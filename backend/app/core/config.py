from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Smart Profile"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A smart personal profile generator"
    
    # API 配置
    KIMI_API_KEY: str = ""  # 从环境变量获取
    KIMI_API_BASE: str = "https://api.moonshot.cn/v1"
    
    # 数据库配置
    DATABASE_URL: str = "sqlite:///./smart_profile.db"
    
    # Redis settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    # JWT settings
    SECRET_KEY: str = "sk-h8Gv3GmkEEXblUcJn3qowM6TtgNGDKnmYq4R0ki2qGSMGmP6"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()
