base = int(input("Digite o primeiro número: "))
expoente = int(input("Digite o segundo número: "))
x = 0
potencia = 1
while x != expoente:
    potencia = potencia * base
    x = x + 1
print("Potencia = ", potencia)