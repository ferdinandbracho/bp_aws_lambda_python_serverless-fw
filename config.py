import logging
import os
import pathlib

from dotenv import load_dotenv

"""
Example config project class, use to load env and others configuration.
"""


class Config:
    logger = logging.getLogger()

    def __init__(self):
        self.load_env_file()
        self.load_env_variables()

    def load_env_file(self) -> None:
        try:
            load_dotenv()
            env_path = pathlib.Path('.') / '.env'
            load_dotenv(dotenv_path=env_path)
        except Exception as e:
            logging.warning(f"Failed to load .env file: {e}")

    def load_env_variables(self) -> None:
        self.example_url = os.getenv("EXAMPLE_URL")
        self.example_users = os.getenv("EXAMPLE_QUEUE_USERS")
        self.example_errors = os.getenv("EXAMPLE_ERROR")

        if not all([
            self.example_url,
            self.example_users,
            self.example_errors
        ]):
            self.logger.warning("Incomplete example configuration."
                                "Please check environment variables.")


config = Config()
