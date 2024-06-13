class Cliente:
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id
        self.__historico_compras = []

    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id

    def get_historico_compras(self):
        return self.__historico_compras

    def add_compra(self, venda):
        self.__historico_compras.append(venda)
