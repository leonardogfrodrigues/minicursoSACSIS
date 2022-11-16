from flask import Flask, json
from flask_pydantic_spec import FlaskPydanticSpec
from flask_cors import CORS
from tinydb import TinyDB

app = Flask(__name__)

CORS(app)

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://127.0.0.1:5000/',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE'
        },
        'body': json.dumps('Hello from Lambda!')
    }

spec = FlaskPydanticSpec('flask', title= 'Endpoints')
spec.register(app)

database = TinyDB('database.json')

from routes.alunos import *