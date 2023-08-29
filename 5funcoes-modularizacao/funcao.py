def maior_numero ():

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o terceiro número: '))
    num3 = float(input('Digite o segundo número: '))
    
    if num1 > num2 and num1 > num3:
        print(f'O número {num1} é maior do que {num2} e {num3}')

    elif num2 > num1 and num2 > num3:
        print(f'O número {num2} é maior do que {num1} e {num3}')

    elif num3 > num1 and num3 > num2:
        print(f'O número {num3} é maior do que {num2} e {num1}')

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o terceiro número: '))
    num3 = float(input('Digite o segundo número: '))

maior_numero()
