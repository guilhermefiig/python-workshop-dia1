sexo = input('Qual o seu sexo [M/F]?').lower()

cont_masc = 0
cont_fem = 0

while sexo != 'sair':

    if sexo == 'm':
        cont_masc += 1

    elif sexo == 'f':
        cont_fem += 1

    sexo = input('Qual o seu sexo [M/F]?')

print(f'A quantidade de pessoas do sexo masculino é {cont_masc} e de pessoas do sexo feminino é {cont_fem}.')
    

