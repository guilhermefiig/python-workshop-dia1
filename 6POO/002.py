class ContaBancaria:
    def __init__(self, titular, saldo, metodo_deposito, metodo_saque):
        self.titular = titular
        self.saldo = saldo
        self.metodo_deposito = metodo_deposito
        self.metodo_saque = metodo_saque

    def mensagem(self):
        print(f'Seu nome é {self.titular}, seu saldo é {self.saldo}, seu método de depósito é {self.metodo_deposito} e o método de saque é {self.metodo_saque}')

titular = input('Seu nome: ')
saldo = float(input('Seu saldo: '))
metodo_deposito = input('Seu método de depósito: ')
metodo_saque = input('Seu método de saque: ')

banco = ContaBancaria(titular, saldo, metodo_deposito, metodo_saque)
banco.mensagem()