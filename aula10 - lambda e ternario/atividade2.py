"""
2)Faça um algoritmo que avalie se o usuario e senha cadastrados e 
se não tiver, printe uma falha
senao printe que deu tudo certo
(considerar que usuario e senha sejam ''ADM')
"""

usuario_cadastrado = "paloma"
senha_cadastrada = "123"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Tudo certo! Login realizado com sucesso.")
else:
    print("Falha: usuário ou senha incorretos.")
if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print('error')
else:
    print('senha correto')

print('usuario') if usuario_cadastrado else print('sucesso')