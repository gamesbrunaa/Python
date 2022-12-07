s1 = input("Digite uma string: ")
cont1 = 0
cont2 = 0
for x in s1:
    if x == ' ':
        cont1 += 1
    elif x == 'a':
        cont2 += 1
    elif x == 'e':
        cont2 += 1
    elif x == 'i':
        cont2 += 1
    elif x == 'o':
        cont2 += 1
    elif x == 'u':
        cont2 += 1
print("Apareceu ", cont1, "espaços em branco!")
print("Apareceu ", cont2, "vogais!")
