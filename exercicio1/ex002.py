peso = int(input("Digite o peso: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("Peso Total: ", peso)
    print("Excesso: ", excesso)
    print("Multa: R$", multa)
else:
    print("Não há excesso de peso!")
