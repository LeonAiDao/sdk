import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Leon AI"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "True") == "True"
