from model.front import Front
from model.linguagem import Linguagem
from model.bd import Bd
class Squad:
    def __init__(self, nome, linguagem:Linguagem, bd:Bd,front:Front,id=None):
        self.nome = nome
        self.linguagem = linguagem
        self.bd = bd
        self.front = front
        self.id = id


  
        # def __init__(self, nome, linguagem:Linguagem, bd:Bd,front:Front, linguagem_id = None, front_id = None, bd_id = None, id=None):
        # self.linguagem_id = linguagem_id
        # self.bd_id = bd_id
        # self.front_id = front_id