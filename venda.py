class Venda:
    def __init__(self, data, itens_vendidos, valor_total):
        self.__data = data
        self.__itens_vendidos = itens_vendidos
        self.__valor_total = valor_total

    def get_data(self):
        return self.__data

    def get_itens_vendidos(self):
        return self.__itens_vendidos

    def get_valor_total(self):
        return self.__valor_total
