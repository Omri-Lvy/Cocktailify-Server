import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGO_URI = os.getenv('MONGO_URI') or ''
    PROD_ORIGIN = os.getenv('PROD_ORIGIN') or ''
    DEV_ORIGIN = os.getenv('DEV_ORIGIN') or 'http://localhost:3000, http://localhost:3001'
