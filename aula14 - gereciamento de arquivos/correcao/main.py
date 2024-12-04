from login import loginUsuario as l_Usuario
from cadastro import cadastrarUsuario as c_usuario

while True:
    try:
        print(f'1 - cadastrar\n 2 - login\n')
        opcao = int(input('O que deseja fazer?'))

        match opcao:
            case (1):
                c_usuario()
            case (2):
                l_Usuario()
    except ValueError:
        print('Digite um valor válido!')
    except Exception:
        print('Aconteceu um erro! tente novamente!')