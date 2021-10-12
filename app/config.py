import logging
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    database_dev_url: AnyUrl
    database_prod_url: AnyUrl
    testing: int = 0
    ENVIROMENT: str
    WEB_APP_TITLE: str
    WEB_APP_DESCRIPTION: str
    WEB_APP_VERSION: str
    DEFAULT_EXPIRE_TIME: int = 3600
    API_AUTH: str


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
