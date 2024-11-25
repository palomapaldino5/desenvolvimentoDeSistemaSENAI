"""
3)Crie um programa que permita ao usuário adicionar tarefas a uma lista, marcar como concluídas ou remover tarefas
"""
usuario = ['Victor','Alan', 'Bruna']
teste = ['texto',123, True,[]]
#usuarioAlt = list()
print(type(usuario))
print(teste)

# metodos de uma lista
tarefas = ['marcar', 'desmarcar','encaixe', 'confirmar']

tarefas.pop() # remover no final
print(tarefas)

tarefas.insert(2,'encaixe') # inserir em um indice
print(tarefas)

print(tarefas[1]) # puxar por um indice

tarefas.remove('desmarcar') # deletar pelo valor
print(tarefas)

tarefas.clear() # deletar tudo da lista
print(tarefas)
