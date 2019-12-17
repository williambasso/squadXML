class Bd:
    def __init__(self, bd, id=None):
        self.__bd = bd
        self.__id = id

    @property
    def bd(self):
        return self.__bd

    @property
    def id(self):
        return self.__id
