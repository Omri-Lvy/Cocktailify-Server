from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from app.config import Config

app = Flask(__name__)
allow_origins =[
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
]
app.config['MONGO_URI'] = Config.MONGO_URI
CORS(app, origins=allow_origins)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

from app import routes
