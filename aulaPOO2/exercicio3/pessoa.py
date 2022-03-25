import datetime

class Pessoa:

    _total_pessoas = 0
    __slots__ = ['_nome', '_cpf', '_end', '_tel']

    def __init__(self, nome, cpf, end, tel):
        self._nome = nome 
        self._cpf = cpf
        self._end = end
        self._tel = tel

    @staticmethod
    def get_total_pessoas():
        return Pessoa._total_pessoas

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def end(self):
        return self._end
    
    @property
    def tel(self):
        return self._tel

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @end.setter
    def end(self, end):
        self._end = end

    @tel.setter
    def tel(self, tel):
        self._tel = tel


class Fotografo(Pessoa):

    def __init__(self, nome, cpf, end, tel):
        Pessoa.__init__(self, nome, cpf, end, tel)

class Proprietario(Pessoa):

    def __init__(self, nome, cpf, end, tel):
        Pessoa.__init__(self, nome, cpf, end, tel)

class Data:

    def __init__(self):
        self.data_foto = datetime.datetime.today()