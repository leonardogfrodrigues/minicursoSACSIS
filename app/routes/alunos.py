from flask import request, jsonify
from main import *#app, spec
from flask_pydantic_spec import Response, Request
from database.alunos import *
from tinydb import Query

@app.get("/alunos") #Estabelecendo a rota do servidor com o metodo GET
@spec.validate(resp=Response(HTTP_200=Alunos))
def buscar_Alunos():
    return jsonify(
        Alunos(
            alunos=database.all(),
            count=len(database.all())
            ).dict()
    )
    
@app.post("/inserir-alunos") #Estabelecendo a rota do servidor com o metodo POST
@spec.validate(body=Request(Aluno), resp=Response(HTTP_200=Aluno))
def inserir_Alunos():
  """Cadastrando um aluno"""  
  body = request.context.body.dict() #Dados em json convertidos para um dict em python
  database.insert(body)
  
  return body

@app.put('/alunos/<int:telefone>') #Estabelecendo a rota do servidor com o metodo PUT
@spec.validate(body=Request(Aluno), resp=Response(HTTP_200=Aluno))
def atualizar_Alunos(telefone):
    Aluno = Query()
    body = request.context.body.dict()
    
    database.update(body, Aluno.telefone == telefone)
    return jsonify(body)

@app.delete('/alunos/<int:telefone>') #Estabelecendo a rota do servidor com o metodo DELETE
@spec.validate(resp=Response('HTTP_204'))
def deletar_Alunos(telefone):
    Aluno = Query()
        
    database.remove(Aluno.telefone == telefone)
    return jsonify({})
