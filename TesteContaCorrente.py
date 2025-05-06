from ContaCorrente import ContaCorrente

novaConta = ContaCorrente("Paulo", 1000)
print(novaConta.cliente, novaConta.saldo)

novaConta.sacar(500)
print("Saldo após saque:", novaConta.saldo)

novaConta.depositar(200)
print("Saldo após depósito:", novaConta.saldo)
