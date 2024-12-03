import json

nome = input('Nome: ')
senha = input('Senha: ')

cadastro = {
    'nome' : nome,
    'senha' : senha,


}

with open('cadastro.json', 'w', encoding='utf8') as leitura:
    json.dump(
        cadastro,
        leitura,
        indent=2
    )