class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        print(f'Oi, meu nome é {self.nome}, minha idade é {self.idade} e mina profissão {self.profissao}')
    
nome = input('Seu nome: ')
idade = input('Seu idade: ')
profissao = input('Seu profissao: ')

pessoa = Pessoa (nome, idade, profissao)
pessoa.saudacao()


# pessoa = Pessoa('ze', 35, 'carteiro')
# pessoa.saudacao()

# guilherme = Pessoa('Gui', 18, 'Estudante')
# guilherme.saudacao()

# rayza = Pessoa('Rayza', 18, 'Dentista')
# rayza.saudacao()