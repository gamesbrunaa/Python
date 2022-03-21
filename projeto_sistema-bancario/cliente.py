from historico import Historico

class Cliente:

    __slots__ = ['_nome', '_sobrenome', '_cpf', '_usuario', '_senha']

    def __init__(self, nome, sobrenome, cpf, usuario, senha):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._usuario = usuario
        self._senha = senha
        self.historico = Historico()

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def cpf(self):
        return self._cpf

    @property
    def usuario(self):
        return self._senha

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome
    

        