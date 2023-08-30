class Animal:
    def __init__(self, animal, som, qtd_pata, habitat):
        self.animal = animal
        self.som = som
        self.qtd_pata = qtd_pata
        self.habitat = habitat
        

    def descricao(self):
        print(f'\nO {self.animal} {self.som}, tem {self.qtd_pata} patas e o seu habitat é {self.habitat}.\n')

class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

class Cobra(Animal):
    def descricao(self):
        print(f'\nA {self.animal} {self.som}, tem {self.qtd_pata} e o seu habitat é {self.habitat}.\n')

gato = Gato('gato', 'mia', 4, 'casa')
cachorro = Cachorro('cachorro', 'late', 4, 'casa')

gato.descricao()
cachorro.descricao()

cobra = Cobra('cobra', 'não faz som', 0, 'selva')
cobra.descricao()