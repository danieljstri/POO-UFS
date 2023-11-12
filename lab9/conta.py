class Conta:
    def __init__(self, nome_correntista, numero_conta):
        self.__nome_correntista = nome_correntista
        self.__numero_conta = numero_conta
        self.__saldo_disponivel = 0
        self.__conta_ativa = True

    def get_nome_correntista(self):
        return self.__nome_correntista

    def set_nome_correntista(self, nome):
        self.__nome_correntista = nome

    def get_numero_conta(self):
        return self.__numero_conta

    def get_saldo_disponivel(self):
        return self.__saldo_disponivel

    def get_conta_ativa(self):
        return self.__conta_ativa

    def deposito(self):
        if self.__conta_ativa:
            while True:
                try:
                    valor = float(input("Insira a quantidade do depósito: "))
                    if valor > 0:
                        self.__saldo_disponivel += valor
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Quantidade de depósito inválida. Certifique-se do valor ser positivo.")
        else:
            print("A conta está desativada. Depósitos não podem serem feitos.")
    

    def saque(self):
        if self.__conta_ativa:
            while True:
                try:
                    valor = float(input("Insira a quantidade do saque: "))
                    if valor > 0 and self.__saldo_disponivel >= valor:
                        self.__saldo_disponivel -= valor
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Quantidade de saque inválida. Certifique-se do valor ser positivo e menor ou igual ao saldo disponível.")
        else:
            print("A conta está desativada. Saques não podem serem feitos.")

    def desativar_conta(self):
        self.__conta_ativa = False

    def ativar_conta(self):
        self.__conta_ativa = True
