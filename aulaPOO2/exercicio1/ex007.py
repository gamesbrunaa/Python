num = int(input("Digite o número: "))
total = 1
x = 1
while x <= num:
    total = total * x
    x = x + 1
print("O fatorial de %i é %i" % (num, total))
