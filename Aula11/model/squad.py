from model.front import Front
from model.linguagem import Linguagem
from model.bd import Bd
class Squad:
    def __init__(self, nome, linguagem:Linguagem, bd:Bd,front:Front,id=None):
        self.__nome = nome
        self.__linguagem = linguagem
        self.__bd = bd
        self.__front = front
        self.__id = id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def linguagem(self):
        return self.__linguagem
    
    @property
    def bd(self):
        return self.__bd
    
    @property
    def front(self):
        return self.__front
    
    @property
    def id(self):
        return self.__id



  
        # def __init__(self, nome, linguagem:Linguagem, bd:Bd,front:Front, linguagem_id = None, front_id = None, bd_id = None, id=None):
        # self.linguagem_id = linguagem_id
        # self.bd_id = bd_id
        # self.front_id = front_id