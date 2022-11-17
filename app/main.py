from flask import Flask, json
from flask_pydantic_spec import FlaskPydanticSpec
from flask_cors import CORS
from tinydb import TinyDB

app = Flask(__name__)

CORS(app)

spec = FlaskPydanticSpec('flask', title= 'Endpoints')
spec.register(app)

database = TinyDB('database.json')

from routes.alunos import *