from flask_restful import Resource
from flask import request

class SquadController(Resource):
    def __init__(self):
        self.dao = SquadDao()
    
    def get(self, id):
        return self.dao.buscar_por_id

    def post(self):
        nome = request.json['nome']
        linguagem = request.json['linguagem']
        front = request.json['front']
        bd =  request.json['bd']
        squad = (nome, linguagem, front, bd)
        return squad

    def put(self, id):
        id = request.json['id']
        nome = request.json['nome']
        linguagem = request.json['linguagem']
        front = request.json['front']
        bd =  request.json['bd']
        squad = (nome, linguagem, front, bd)
        return squad

    def delete(self, id):
        self.dao.deletar(id)
        return  
    


    