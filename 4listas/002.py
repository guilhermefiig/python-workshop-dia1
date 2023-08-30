comando = int(input('Digite 1 para ADICIONAR UMA TAREFA.\nDigite 2 para EXECUTAR A FILA.\nDigite 3 para SAIR.\n'))
pilha = []

while comando != 3:
    match comando:
        case 1:
            atv = str(input('Digite a atividade que desejas adicionar: '))
            pilha.append(atv)
            print(f'{atv.upper()} adicionado à fila.')
            comando = int(input('Digite 1 para ADICIONAR UMA TAREFA.\nDigite 2 para EXECUTAR A FILA.\nDigite 3 para SAIR.\n'))
        case 2:
            print('{} removido da fila.'.format(pilha[0].upper()))
            pilha.pop(-1)
            comando = int(input('Digite 1 para ADICIONAR UMA TAREFA.\nDigite 2 para EXECUTAR A FILA.\nDigite 3 para SAIR.\n'))