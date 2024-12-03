import json

with open('cadastro.json', 'r', encoding='utf8') as leitura:
    pessoa = json.load(leitura)
    nome_cadastrado = pessoa['nome']
    senha_cadastrado = pessoa['senha']

nome = input('Digite o nome')
senha = input('Digite o senha')

if senha == senha_cadastrado and nome == nome_cadastrado:
    print('DEU CERTO')
else:
    print('USUARIO OU SENHA INCORRETOS!')
