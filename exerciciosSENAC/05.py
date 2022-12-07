nome = input("Digite o nome do técnico: ")
qtdAtendimento = int(input("Quantos atendimentos foram realizados? "))
qtdProdutos = float(input("Quanto ele vendeu em produtos? "))
salario = 2500
comissao = 50
atendimento = (qtdProdutos * 0.05)
salarioF = salario + (qtdAtendimento * comissao) + atendimento

print("O salário final é ", salarioF)