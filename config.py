import logging
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

# Initialize logger for this module
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """
    Configuration settings for the application.

    Loaded from environment variables and/or a .env file.
    Pydantic's BaseSettings handles loading and validation.
    """
    APP_NAME: str = "MyServerlessApp"
    LOG_LEVEL: str = "INFO"
    # Default changed to match previous handler logic
    DUMMY_API_URL: str = "https://jsonplaceholder.typicode.com/users" 

    EXAMPLE_URL: Optional[str] = None
    EXAMPLE_QUEUE_USERS: Optional[str] = None
    EXAMPLE_ERROR: Optional[str] = None

    # Pydantic V2 settings configuration
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8', 
        extra='ignore'
    )

# To use the settings in your application:
# from config import Settings
settings = Settings()
