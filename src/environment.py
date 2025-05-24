from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv()

class Environment:
    DB_NAME = os.getenv('DB_NAME')

    def __init__(self):
        self.db_name = self.DB_NAME
        logger.info("Loaded Database Name as {self.db_name}")


app_environment = Environment()