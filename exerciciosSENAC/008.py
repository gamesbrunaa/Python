s1 = input("Digite uma string: ")
s2 = s1[::-1]
if s1 == s2:
    print(s1)
    print("É um palindromo!")
else: 
    print(s1)
    print("Não é um palindromo!")