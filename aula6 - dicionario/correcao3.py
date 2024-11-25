"""
3)Crie um programa que permita ao usuário adicionar tarefas a uma lista, marcar como concluídas ou remover tarefas
"""

tarefas = []

while True:
    print('TAREFAS')
    for tarefa in tarefas:
        print(f'- {tarefa}')

    print('*********************')
    print('A - ADICIONAR TAREFA')
    print('B - REMOVER TAREFA')
    print('C - PARAR APLICATIVO')
    escolha = input('Digite o que quer executar')

    match escolha:
        case 'a':
            tarefa = input('Qual tarefa adicionar?')
            tarefas.append(tarefa)
        case 'b':
            tarefa = input('Qual deseja remover')
            tarefas.remove(tarefa)
        case 'c':
            break
        case _:
            print('Opcão invalida')