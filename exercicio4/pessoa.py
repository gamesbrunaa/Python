class Pessoa:

    __slots__ = ['_nome', '_end', '_cpf', '_dataNasc']

    def __init__(self, nome, end, cpf, dataNasc):
        self._nome = nome
        self._end = end
        self._cpf = cpf
        self._dataNasc = dataNasc

    @property
    def nome(self):
        return self._nome

    @property
    def end(self):
        return self._end

    @property
    def cpf(self):
        return self._cpf

    @property
    def dataNasc(self):
        return self._dataNasc

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @end.setter
    def end(self, end):
        self._end = end




