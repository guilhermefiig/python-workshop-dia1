velocidade_carro = int(input('Quaal a velocidade do carro? '))

if velocidade_carro > 80:
    print('Você foi multado')
    print(f'Sua multa é no valor de R${(velocidade_carro - 80) * 7}')

else:
    print('Você não foi multado')