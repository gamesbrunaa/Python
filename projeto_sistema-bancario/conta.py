from historico import Historico

class Conta:
    __slots__ = ['_numero', '_titular', '_saldo', '_limite']

    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

    @property
    def numero(self):
        return self._numero

    @property
    def titutar(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("deposito de {}".format(valor))

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True
    
    def extrato(self):
        print("numero: {} \nsaldo:{}".format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True