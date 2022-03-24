import collections
from collections import Counter

a = input("Digite o nome do arquivo: ")
arquivo = open(a, 'r')
palavras = []
mais_repetidas = []

def repetir(palavras):
    repetidas = []
    repetidas = (Counter(palavras).most_common(3))
    return repetidas

for linha in arquivo:
    linha = linha.strip()
    linha = linha.lower()
    palavras = linha.split(" ") 

mais_repetidas = repetir(palavras)
cont = 0 
while (cont < 3):
    x, y = mais_repetidas[cont]
    print(x, ':', y)
    cont += 1
    
arquivo.close()