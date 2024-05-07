import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI')
    ORIGINS = [os.getenv('PROD_ORIGIN'), os.getenv('DEV_ORIGIN')]

