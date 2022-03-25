op = int(input("Digite 1 para calcular o fatorial, ou 0 para sair: "))
while op == 1:
    num = int(input("Digite o número: "))
    total = 1
    x = 1
    if (num >= 0 & num < 16):
        while x <= num:
            total = total * x
            x = x + 1
        print("O fatorial de %i é %i" % (num, total))
    else:
        print("Apenas números inteiros e menores que 16!")
    op = int(input("Digite 1 para calcular o fatorial, ou 0 para sair: "))