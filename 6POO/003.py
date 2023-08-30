class Carro:
    def __init__(self, modelo, marca, ano, cor, velocidade):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade

    def aceleracao(self, aumento):
        self.velocidade += aumento
        print(f'O {self.marca} {self.modelo} {self.cor}, ano {self.ano} acelerou {self.velocidade}km/h')

meu_carro = Carro('VW', 'Jetta', 2020, 'Chumbo', 0)

meu_carro.aceleracao(int(input('Quanto acelerou? ')))