# DICIONARIO
# CHAVE E VALOR 

usuario = {
    #chave : valor
    'nome'  : 'Victor',
    'email' : 'emailtop@gmail.com',
    'senha' : '!123456',
    'cpf' : 4564646465464,
    'vip' : True,
    'saldo' : 10,
    'endereco' : [
        {
            'rua' : '13',
            'cidade' : 'Ceilandia',
            'estado' : 'DF'

        }
    ]
}


print(usuario['nome'])

print(usuario, type(usuario))

#arquitetura de dic facilita o gerenciamento de dados
#e a busca por eles (Obs: Até mesmo o crud)

#pesquisa = input('Digite o que quer achar:')
#print(usuario[pesquisa])

#metodos para dicionario
#len - quantas chaves existe no dicionario
#keys - retorna as chaves
#values - retorna os valores
#items - retorna chaces e valores
#setdefault - Adiciona valoor se a chave não existe
#get = busca chave
#pop - apaga uma especifica (del)
#popitem - apaga a ultima chave
#update - atualiza um dicionario
print(len(usuario))
print(list(usuario.keys()))
print(list(usuario.values()))
print(list(usuario.items()))

usuario.setdefault('saldo', 0)
print(usuario)

print(usuario.get('nome'))
usuario.pop('nome')
print(usuario)

usuario.popitem()
print(usuario)

usuario.update({
    'nome' : 'Victor',
    'email' : 'victor.rohod@docente.senai.br'
})
print(usuario)