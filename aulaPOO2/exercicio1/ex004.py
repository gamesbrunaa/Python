lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))
if (((lado1 + lado2) > lado3) & ((lado1 + lado3) > lado2) & ((lado2 + lado3) > lado1)):
    if ((lado1 == lado2) & (lado2 == lado3)):
        print("É um triângulo Equilátero!")
    elif ((lado1 == lado2) | (lado1 == lado3) | (lado3 == lado2)):
        print("É um triangulo Isosceles!")
    elif ((lado1 != lado2) & (lado2 != lado3)):
        print("É um triangulo Escaleno!")
else:
    print("Não é um trinagulo!")