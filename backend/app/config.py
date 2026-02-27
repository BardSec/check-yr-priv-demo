from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_base_url: str = "http://localhost"
    secret_key: str = "demo-secret-key-not-for-production-use-abc123xyz"
    redis_url: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"


settings = Settings()
