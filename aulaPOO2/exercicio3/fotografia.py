from pessoa import *
import os
from skimage import io, data
from matplotlib import imshow

class Fotografia:

    _total_fotos = 0
    __slots__ = ['_foto', '_fotografo', 'data', '_proprietario']

    def __init__(self, foto, fotografo, proprietario):
        self._foto = foto
        self._fotografo = fotografo
        self._proprietario = proprietario
        self.data = Data()

    @staticmethod
    def get_total_fotos():
        return Fotografia._total_fotos

    @property
    def foto(self):
        return self._foto

    @property
    def fotografo(self):
        return self._fotografo
    
    @property
    def proprietario(self):
        return self._proprietario

    @foto.setter
    def foto(self, foto):
        self._foto = foto

    @fotografo.setter
    def fotografo(self, fotografo):
        self._fotografo = fotografo

    @proprietario.setter
    def proprietario(self, proprietario):
        self._proprietario = proprietario

    def mostrar(self, foto):
        file = os.path.join(skimage.data_dit, foto)
        f = imread(file)
        io.imshow(f)
        io.show()

    def propriedades(self, foto):
        print("Tamanho da fotografia em pixels: ")
        foto = data.foto()
        print(foto.shape)
        print("Fotógrafo: ", foto.fotografo.nome)
        print(foto.data)
