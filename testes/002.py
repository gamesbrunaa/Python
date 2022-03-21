import os

arquivo = input("Digite o nome do arquivo: ")
a = open(arquivo, 'r')
x = 1
for linha in a:
    print(x, linha)
    x += 1
