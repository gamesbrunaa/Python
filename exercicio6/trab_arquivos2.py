from turtle import pensize

#abrindo o arquivo
a = input("Digite o nome do arquivo: ")
arquivo = open(a, 'r')

alunos_notas = []
medias = []
indices = []
maiores = []

#função para calcular media
def media(n1, n2, n3):
    media = ((n1 + n2 + n3) / 3)
    return media

#função para achar as maiores médias
def maior_media(medias):
    maior = 0
    cont = 0
    for x in range(len(medias)):
        if (medias[x] > maior) & (x not in indices):
            maior = medias[x]
            cont = x
    maiores.append(maior)
    indices.append(cont)

#transformando o arquivo em uma lista de listas
for linha in arquivo:
    linha = linha.strip()
    alunos_notas.append(linha.split(" "))
print(alunos_notas)

#separando o nome dos alunos das notas
alunos = []
for x in range(len(alunos_notas)):
    alunos.append(alunos_notas[x][0])
print(alunos)

#transformando a lista de listas em apenas uma lista
l_alunos_notas = []
for x in alunos_notas:
    l_alunos_notas.extend(x)
print(l_alunos_notas)

#seperando as notas
notas = []
for x in l_alunos_notas:
    if x not in alunos:
        notas.append(x)
print(notas)

#transformando cada valor do array em float
notas = [float (x.strip("[]").replace(",", ".")) for x in notas]

#calculando as medias dos alunos
for x in range(0, len(notas), 3):
    n1 = (notas[x])
    n2 = (notas[x + 1])
    n3 = (notas[x + 2])
    medias.append(media(n1, n2, n3))
print(medias)

#encontrando os três maiores
maior_media(medias)
maior_media(medias)
maior_media(medias)
print(maiores)

#escrevendo no arquivo
arquivo3 = open('arquivo3.txt', 'w')
cont = 0
while (cont < 3):
    arquivo3.write(alunos[indices[cont]])
    arquivo3.write(' - ')
    arquivo3.write(str(maiores[cont]))
    arquivo3.write('\n')
    cont += 1

arquivo.close()
arquivo3.close()