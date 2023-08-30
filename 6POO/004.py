class FormaGeometrica:
    def calcular_area(self, raio):
        return 3.14 (raio ** 2)

class Circulo(FormaGeometrica):
    pass

class Retangulo(FormaGeometrica):
    def calcular_area(self, base, altura):
        return base * altura

class Quadrado(Retangulo):
    pass

circulo = Circulo()
area = circulo.calcular_area(10)
print(area)

retangulo = Retangulo()
area = retangulo.calcular_area(6,8)
print(area)

quadrado = Quadrado()
area = quadrado.calcular_area(10,12)
print(area)




# class Garrafa:
#     def init(self, tamanho, cor, marca):
#         self.tamanho = tamanho
#         self.cor = cor
#         self.marca = marca

#     def str(self):
#         return f'tamanho: {self.tamanho}, marca:{self.marca}'


# class GarrafaDeVidro(Garrafa):

#     def quebrar(self):
#         print('crack')


# garrafa = Garrafa(150, 'azul', 'indaia')

# garrafa_de_vidro = GarrafaDeVidro(200, 'transparente', 'vidro')


# a = garrafa.str()
# print(a)
# print(garrafa_de_vidro.str())