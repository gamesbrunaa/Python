from conta import Conta
from cliente import Cliente

conta1 = Conta('00001', 'Bruna', 100, 10000)
conta2 = Conta('00002', 'Weslley', 200, 1000)
conta3 = Conta('00003', 'Isabel', 0, 1000)

print(conta1.saldo)
print(conta2.saldo)
print(conta3.saldo)

conta2.transfere(conta1, 100)
print(conta1.saldo)
print(conta2.saldo)

x = conta3.transfere(conta2, 100)
if(x == False):
    print("Não é possivel fazer transferência!")
else:
    print(conta2.saldo)
    print(conta3.saldo)

cliente1 = Cliente('Bruna', 'Heloisa', 000000000)
conta4 = Conta('00004', cliente1, 120, 1000)
cliente2 = Cliente('Weslley', 'Renzel', 12345678910)
conta5 = Conta('00005', cliente2, 1000, 10000)
cliente3 = Cliente('Eu', 'Myself', 12345678911)
conta6 = Conta('00006', cliente3, 100, 1000)

conta4.saca(20)
conta5.saca(100)
conta6.deposita(100)

conta1.historico.imprimir()
print("\n")
conta2.historico.imprimir()
print("\n")
conta3.historico.imprimir()
print("\n")
conta4.historico.imprimir()
print("\n")
conta5.historico.imprimir()
print("\n")
conta6.historico.imprimir()
print("\n")
