from conta import Conta

conta1 = Conta("João", "12345")

conta1.deposito()
print(f"Saldo disponível após depósito: {conta1.get_saldo_disponivel()}")

conta1.saque()
print(f"Saldo disponível após saque: {conta1.get_saldo_disponivel()}")

# saque com saldo insuficiente
try:
    conta1.saque()
except ValueError as e:
    print(f"Erro: {e}")

# depósito com valor negativo
try:
    conta1.deposito()
except ValueError as e:
    print(f"Erro: {e}")

# saque com conta inativa
conta1.desativar_conta()
try:
    conta1.saque()
except ValueError as e:
    print(f"Erro: {e}")

# ativando a conta novamente
conta1.ativar_conta()
conta1.deposito()
print(f"Saldo disponível após ativar a conta e fazer um depósito: {conta1.get_saldo_disponivel()}")