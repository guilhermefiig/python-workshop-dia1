class ContaBancaria():
    def __init__(self, titular, saldo, metodo_deposito, metodo_saque):
        self.titular = titular
        self.saldo = saldo
        self.deposito = metodo_deposito
        self.saque = metodo_saque

    def menssagem(self):
        print(f'Seu nome é {self.titular}, seu saldo é {self.saldo}, seu metodo de deposito é {self.deposito} e o metodo de saque é {self.saque}')
    
titular = input('Seu nome: ')
saldo = input('Seu saldo: ')
metodo_deposito = input('Seu metodo de deposito: ')
metodo_saque = input('Seu metodo de saque: ')

banco = ContaBancaria(titular, saldo, metodo_deposito, metodo_saque)
banco.menssagem()