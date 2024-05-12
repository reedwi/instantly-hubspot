from typing import Annotated, Any, Literal, Optional

from pydantic import (
    AnyUrl,
    BeforeValidator,
    HttpUrl,
    PostgresDsn,
    computed_field,
)
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    API_V1_STR: str = "/api"
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    @computed_field  # type: ignore[misc]
    @property
    def server_host(self) -> str:
        # Use HTTPS for anything other than local development
        if self.ENVIRONMENT == "local":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    PROJECT_NAME: str
    SENTRY_DSN: HttpUrl | None = None
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    
    HS_APP_ID: int
    HS_CLIENT_ID: str
    HS_CLIENT_SECRET: str

    @computed_field
    @property
    def HS_REDIRECT_URI(self) -> str:
        return f'{self.server_host}{self.API_V1_STR}/install'
    
    @computed_field
    @property
    def WEBHOOK_URL(self) -> str:
        return f'{self.server_host}{self.API_V1_STR}/webhooks'

    STRIPE_PROD_PUBLISHABLE_KEY: Optional[str]
    STRIPE_PROD_SECRET_KEY: Optional[str]
    STRIPE_TEST_PUBLISHABLE_KEY: Optional[str]
    STRIPE_TEST_SECRET_KEY: Optional[str]

    @computed_field
    @property
    def STRIPE_PUBLISHABLE_KEY(self) -> str:
        if self.ENVIRONMENT in ["local", "staging"]:
            return self.STRIPE_TEST_PUBLISHABLE_KEY
        return self.STRIPE_PROD_PUBLISHABLE_KEY
    
    @computed_field
    @property
    def STRIPE_SECRET_KEY(self) -> str:
        if self.ENVIRONMENT in ["local", "staging"]:
            return self.STRIPE_TEST_SECRET_KEY
        return self.STRIPE_PROD_SECRET_KEY

settings = Settings()