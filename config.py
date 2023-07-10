import logging
import os

"""
Example config project class, use to load env and others configuration.
"""


class Config:
    logger = logging.getLogger()

    def __init__(self):
        self.load_env_variables()

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
