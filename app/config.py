import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI')
    PROD_ORIGIN = os.getenv('PROD_ORIGIN')
    DEV_ORIGIN = os.getenv('DEV_ORIGIN')

