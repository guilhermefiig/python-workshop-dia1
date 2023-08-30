soma = 0

while True:
    numero_digitado = int(input("Digite um número (0 para sair): "))

    if numero_digitado != 0:
        soma += numero_digitado
    
    else:
        break

print(f'A soma dos números digitados é: {soma}')