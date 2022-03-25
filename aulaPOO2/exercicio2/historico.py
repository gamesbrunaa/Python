import datetime
from re import T

class Historico:
    def __init__(self):
        self.data_abre = datetime.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print("data abertura da conta: {}".format(self.data_abre))
        print("Transações realizadas: ")
        if (self.transacoes != []):
            for x in self.transacoes:
                print("-", x)
        else:
            print("Não foram realizados transações ainda!")