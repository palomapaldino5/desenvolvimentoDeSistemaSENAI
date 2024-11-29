"""
1)Peça ao usuário dois números e uma operação matemática (+, -, *, /). 
Execute a operação e trate erros como divisão por zero e operação inválida.
"""
try:
    num1 = int(input('Digite primeiro número'))
    operador = input('Digite o operador')
    num2 = int(input('Digite segundo número'))

    match operador :
        case '+':
            resultado = num1 + num2
        case '-':
            resultado = num1 - num2
        case '*':
            resultado = num1 * num2
        case '/':
            resultado = num1 / num2    
except ValueError:
    print('VALOR INVÁLIDO!')
except ZeroDivisionError:
    print('NÃO POSSO DIVIDIR UM NÚMERO POR 0')
except Exception:
    print('OPERAÇÃO INVÁLIDA!')
finally:
    print(f'Resultado final é de {resultado} ')