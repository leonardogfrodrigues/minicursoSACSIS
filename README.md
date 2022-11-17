# Minicurso de Flask para a SACSIS 2022

Leonardo G. F. Rodrigues 

leonardogfrodrigues@gmail.com

### :memo: Descrição
A aplicação consiste numa API REST simples utilizando Flask. Os dados persistidos nessa API são de um banco de dados de alunos descrito pelo TinyDB 
__________________

### :computer: Configurações necessárias 
Antes de executar os comandos deste e do próximo tópico é preciso ter o python3 e o gerenciador de pacotes pip instalados em sua máquina.

- Ambiente de execução
```
python3 -m venv venv
```
- Instalação do Flask
```
pip install flask
```
- Instalação do TinyDB
```
pip install tinydb
```
- Instalação do Flask_Pydantic_Spec para especificação da API
```
pip install flask-pydantic-spec
```
- Instalação do Flask-Cors para permissão de execução no navegador
```
pip install flask-cors
```

__________________
### :gear: Execução
Posteriormente, na pasta "app", basta executar os comandos abaixo:

```
export FLASK_APP='main.py'
```

```
export FLASK_DEBUG=1
```

```
flask run
```

__________________
### :eyes: Visualização

Por fim, entre com o endereço abaixo em seu navegador para visualizar a aplicação com a documentação swagger.

```
http://localhost:5000/apidoc/swagger
```
