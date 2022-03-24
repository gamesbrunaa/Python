import os

a = input("Digite o nome do arquivo: ")
arquivo = open(a, 'r')
palavras = []
p = []
vezes = []

for linha in arquivo:
    linha_palavra = linha.lower().replace(',', '').replace('.', '').replace('?', '').replace('-', '').replace(':','')
    for x in linha_palavra:
        palavras.append(x)

for y in range(0, 2):
    for i in range(0, len(palavras)):
        cont = 1
        for j in range(i+1, len(palavras)):
            if(palavras[i] == palavras[j]):
                cont = cont + 1
        if (cont > vezes):
            vezes[y] = cont
            p[y] = palavras[i]
    cont = 0

for y in range(0, 2):
    print(p[y], ': ', vezes[y])

arquivo.close()