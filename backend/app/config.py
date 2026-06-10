from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Classtify API"
    app_version: str = "0.1.0"
    debug: bool = False

    database_url: str = "postgresql+asyncpg://classtify:classtify@localhost:5432/classtify"
    jwt_secret: str = "change-me-in-production"
    jwt_lifetime_seconds: int = 3600

    cors_origins: list[str] = ["http://localhost:1420"]

    openrouter_api_key: str | None = None
    openrouter_default_model: str = "anthropic/claude-sonnet-4"
    openrouter_base_url: str = "https://openrouter.ai/api/v1"


settings = Settings()
