litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite A para alcool e G para gasolina: ")
if tipo == 'A':
    total = litros * 3.45
    if litros <= 20:
        desconto = total * 0.03
        valorfinal = total - desconto
        print("VALOR TOTAL: R$", valorfinal)
    elif litros > 20:
        desconto = total * 0.05
        valorfinal = total - desconto
        print("VALOR TOTAL: R$", valorfinal)
elif tipo == 'G':
    total = litros * 4.53
    if litros <= 20:
        desconto = total * 0.04
        valorfinal = total - desconto
        print("VALOR TOTAL: R$", valorfinal)
    elif litros > 20:
        desconto = total * 0.06
        valorfinal = total - desconto
        print("VALOR TOTAL: R$", valorfinal)
