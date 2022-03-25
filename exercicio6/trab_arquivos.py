import collections
from collections import Counter

#abrindo o arquivo
a = input("Digite o nome do arquivo: ")
arquivo = open(a, 'r')
palavras = []
mais_repetidas = []

#função que encontra as três palavras mais repetidas
def repetir(palavras):
    repetidas = []
    repetidas = (Counter(palavras).most_common(3))
    return repetidas

#transformando o arquivo em uma lista de palavras
for linha in arquivo:
    linha = linha.strip()
    linha = linha.lower()
    palavras = linha.split(" ") 

#chamando a função
mais_repetidas = repetir(palavras)

#escrevendo no arquivo
cont = 0 
arquivo2 = open('arquivo2.txt', 'w')
while (cont < 3):
    x, y = mais_repetidas[cont]
    arquivo2.write(x)
    arquivo2.write(':')
    arquivo2.write(str(y))
    arquivo2.write('\n')
    cont += 1

#fechando os arquivos
arquivo.close()
arquivo2.close()