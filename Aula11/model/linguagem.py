class Linguagem:
    def __init__(self, linguagem, id=None):
        self.__linguagem = linguagem
        self.__id = id

    @property
    def linguagem(self):
        return self.__linguagem

    @property
    def id(self):
        return self.__id
