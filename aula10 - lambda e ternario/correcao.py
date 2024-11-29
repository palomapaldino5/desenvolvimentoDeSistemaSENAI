def ex1():
    # metodo com lambda
    # for i
    #  tabuada = lambda n : print(n * i)
    #  tabuada(8)

    # metodo com list compreentions
    tabuada = [i * 8 for i in range(1,11)]
    print(tabuada)

def ex2():
    usuario_cadastrado = 'ADM'
    senha_cadastrada = 'ADM'

    usuario = input('Qual é o usuário: ')
    senha = input('Qual é a senha: ')

    v_usuario = usuario == usuario_cadastrado
    v_senha = senha == senha_cadastrada
    verificar = v_usuario and v_senha

    msgSucesso = 'CONTA LOGADA'
    msgErro = 'USUARIO OU SENHA INCORRETOS'

    # metodo 1
    print(msgSucesso) if verificar else print(msgErro)

    # metodo 2
    print('USUARIO CORRETO!') if v_usuario else print('USUARIO INCORRETO')

    print('SENHA CORRETA!') if v_senha else print('SENHA INCORRETA')

ex2()