import json

def cadastrarUsuario():
    nome = input('Digite o nome:')
    login = input('Digite o login (email):')
    cpf = int(input('Digite seu cpf (888888):'))
    
    while True:    
        senha = input('Digite a sua senha:')
        c_senha = input('Digite a sua senha novamente:')

        if senha == c_senha:
            break
        else:
            print('Senha não bate na confirmação tente novamente!')

        dados ={
            'nome': nome,
            'login' : login,
            'cpf' : cpf,
            'senha' : senha,
        }

        with open('dados.json', 'w',encoding='utf8') as leitura:
            json.dump(
                dados,
                leitura,
                indent=2
            )