from conta import Conta

conta_silvio = Conta(1001, "Silvio", 100.00, 200.00);

conta_silvio.deposita(-200);

print("Seu saldo atual: ", conta_silvio.saldo);