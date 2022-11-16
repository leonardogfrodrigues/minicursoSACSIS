from flask import Flask
from pydantic import BaseModel

from main import database

class Aluno(BaseModel):
    nome: str
    email: str
    telefone: int
   
class Alunos(BaseModel):
    alunos: list[Aluno]
    count: int