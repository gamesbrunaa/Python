cpf = input("CPF(xxx.xxx.xxx-xx) :")
tam = len(cpf)
for letra in cpf:
    if(cpf[3] != '.') or (cpf[7] != '.') or (cpf[11] != '-') or tam != 13:
        verificador = 0
    else:
        verificador = 1

if verificador == 0:
    print("CPF inválido!")
elif verificador == 1:
    print("CPF válido!")
