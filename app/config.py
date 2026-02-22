import os
from dotenv import load_dotenv
import pytz

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
APP_TZ = os.getenv("APP_TIMEZONE")
TIMEZONE = pytz.timezone(APP_TZ)