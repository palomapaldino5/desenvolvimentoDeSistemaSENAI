"""
4)Crie um programa que simule um caixa eletrônico. 
Peça ao usuário um valor a ser sacado e deduza de um saldo inicial. 
Caso o usuário tente sacar mais do que o saldo ou insira um valor inválido, trate o erro de forma apropriada. 
Garanta que o saldo atualizado seja sempre exibido no finally.
"""

saldo = 50

while True:
    try:
        opcao = int(input('1 - SACAR \n 2 - SALDO \n 0 - Sair \n '))

        match opcao:
            case 1:
                try:
                    valorSaque = float(input('Digite o valor a ser sacado'))

                    if valorSaque > saldo:
                        raise Exception
                    elif valorSaque < 0:
                        raise Exception
                    else:
                        print(f'O valor R$ {valorSaque} foi sacado!')
                        saldo -= valorSaque
                except Exception:
                    print('OPERAÇÃO INVÁLIDA')

            case 2:
                print(f'O SALDO DISPONIVEL É DE R$ {saldo}')
            
            case 0:

                confirma =input('Confirma? s/n').lower()

                if confirma == 's':
                    break
                else:
                    continue
    except ValueError:
            print(f'OPÇÃO INVÁLIDA! TENTE NOVAMENTE! Código do erro {erro}')
    except Exception as erro:
            print(f'ERRO DESCONHECIDO TENTE NOVAMENTE! Código do erro {erro}')    
    finally:
            print(f'Usuário, saldo disponível é de R${saldo}')                
