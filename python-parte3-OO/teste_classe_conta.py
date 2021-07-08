#sintax para importar a classe
from conta import Conta

#criando um objeto do tipo Conta, é necessário passar os parametros
#contidos dentro do método contrutor __init__ sem o self
conta_silvio = Conta(1234, "Silvio Sales", 100, 1000)
print(conta_silvio.titular)
print("Saldo inicial:", conta_silvio.saldo)
conta_silvio.deposita(400)
print("Saldo atual:", conta_silvio.saldo, "\n")

#criando outro objeto do tipo conta
conta_giovana = Conta(4321, "Giovana Victoria", 200, 2000)
print(conta_giovana.titular)
print("Saldo inicial:", conta_giovana.saldo)

#fazendo uma transferencia
conta_silvio.transfere(500, conta_giovana)
print("\n{} transferiu 500 para {}\n".format(conta_silvio.titular, conta_giovana.titular))

print(conta_silvio.titular)
print("Saldo final:", conta_silvio.saldo, "\n")

print(conta_giovana.titular)
print("Saldo final:", conta_giovana.saldo)