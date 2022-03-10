from pessoa import Pessoa

class Cadastro:

    __slots__ = ['_listap']

    def __init__(self):
        self._listap = []

    def cadastrar(self, pessoa):
        existir = self.buscar(pessoa.cpf)
        if (existir == None):
            self._listap.append(pessoa)
            return True
        else:
            return False
    
    def buscar(self, cpf):
        for x in self._listap:
            if x.cpf == cpf:
                return x
        return None

