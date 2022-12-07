s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")
cont1 = 0
cont2 = 0
for i in s1:
    cont1 += 1
for j in s2:
    cont2 = cont2 + 1

print('Tamanho de ', s1, ":", cont1, 'caracteres')
print('Tamanho de ', s2, ":", cont2, 'caracteres')

if (s1 == s2):
    print('As duas strings possuem tamanhos iguais!')
else:
    print('As duas strings são de tamanhos diferentes!')