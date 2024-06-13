class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_codigo(self):
        return self.__codigo

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def definir_quantidade(self, quantidade):
        self.__quantidade = quantidade

class Eletronico(Produto):
    def __init__(self, nome, codigo, preco, quantidade, marca):
        super().__init__(nome, codigo, preco, quantidade)
        self.__marca = marca

    def get_marca(self):
        return self.__marca

class Roupa(Produto):
    def __init__(self, nome, codigo, preco, quantidade, tamanho):
        super().__init__(nome, codigo, preco, quantidade)
        self.__tamanho = tamanho

    def get_tamanho(self):
        return self.__tamanho

class Alimento(Produto):
    def __init__(self, nome, codigo, preco, quantidade, data_validade):
        super().__init__(nome, codigo, preco, quantidade)
        self.__data_validade = data_validade

    def get_data_validade(self):
        return self.__data_validade
