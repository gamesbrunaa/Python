num = int(input("Digite o número para calcular a tabuada: "))
comeca = int(input("Digite onde deve começar: "))
termina = int(input("Digite onde deve terminar: "))
x = comeca
while x <= termina:
    print(" %i X %i = %i" %(num, x, num*x))
    x = x + 1