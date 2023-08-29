comando = int(input('Digite 1 para ADICIONAR UMA TAREFA.\nDigite 2 para EXECUTAR A FILA.\nDigite 3 para SAIR.\n'))
fila = []

while comando != 3:
    match comando:
        case 1:
            atv = str(input('Digite a atividade que desejas adicionar: '))
            fila.append(atv)
            print(f'{atv.upper()} adicionado à fila.')
            comando = int(input('Digite 1 para ADICIONAR UMA TAREFA.\nDigite 2 para EXECUTAR A FILA.\nDigite 3 para SAIR.\n'))
        case 2:
            print('{} removido da fila.'.format(fila[0].upper()))
            fila.pop(0)
            comando = int(input('Digite 1 para ADICIONAR UMA TAREFA.\nDigite 2 para EXECUTAR A FILA.\nDigite 3 para SAIR.\n'))
