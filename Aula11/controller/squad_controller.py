from flask_restful import Resource
from flask import request
from dao.base_dao import BaseDao
from dao.squad_dao import SquadDao
from model.squad import Squad

class SquadController(Resource):
    def __init__(self):
        self.dao = SquadDao()
    
    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()


    def post(self):
        nome_id = request.json['nome']
        linguagem_id = request.json['linguagem_id']
        front_id = request.json['front_id']
        bd_id =  request.json['bd_id']
        squad = Squad(nome_id, linguagem_id, front_id, bd_id )
        if nome_id.lower() == 'nicole' and linguagem_id == 1 and front_id == 1 and bd_id == 1:
            squad_id = self.dao.inserir(squad)
            squad = self.dao.buscar_por_id(squad_id)  
        
        elif nome_id.lower() == 'mateus' and linguagem_id == 2 and front_id == 2 and bd_id == 2:
            squad_id = self.dao.inserir(squad)
            squad = self.dao.buscar_por_id(squad_id)
        
        elif nome_id.lower() == 'tiago' and linguagem_id == 3 and front_id == 3 and bd_id == 3:
            squad_id = self.dao.inserir(squad)
            squad = self.dao.buscar_por_id(squad_id)
        else:
            return 'DEU MERDA'

        return squad


    def delete(self, id):
        self.dao.deletar(id)
        return 'Deletado' 
    


    