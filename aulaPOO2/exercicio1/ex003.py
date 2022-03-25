ganha = float(input("Digite quanto você ganha por hora: "))
horas = float(input("Digite quantas horas você trabalha ao mês: "))
salarioB = ganha * horas
IR = 0.11 * salarioB
INSS = 0.08 * salarioB
S = 0.05 * salarioB
salario = salarioB - IR - INSS - S
print(" + Salario Bruto: R$", salarioB)
print(" - IR (11%): R$", IR)
print(" - INSS (8%): R$", INSS)
print(" - Sindicato (5%): R$", S)
print(" = Salário Líquido: R$", salario)
