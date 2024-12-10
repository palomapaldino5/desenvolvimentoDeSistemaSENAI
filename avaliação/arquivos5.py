"""
5)Implemente uma função chamada calculadora que:Receba dois números e uma operação (adição, subtração, multiplicação ou divisão).
Retorne o resultado da operação.Trate divisões por zero e exiba uma mensagem apropriada.Salve o histórico dela em um json
"""
import json

def calculadora_adicao():
    print("Bem-vindo à calculadora de adição!")

    while True:
        try:
            num1 = float(input("Digite o primeiro número (ou 'finalizar' para encerrar): "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input('Qual é a operação desejada? (+, - , * ou /)')

            if operacao == '+':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}\n")
            elif operacao == '-':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}\n")
            elif operacao == '*':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}\n")
            elif operacao == '/':
                print(f"Resultado: {num1} / {num2} = {num1 / num2}\n")
            else:
                print('Coloque um operador válido!')

            

        except ValueError:
            with open('cadastro.json', 'w', encoding='utf8') as num2:
                json.dump(
                num1,
                num2,
                indent=2
            )
            finalizar = input("Você digitou algo inválido. Digite 'finalizar' para encerrar ou pressione Enter para continuar: ").strip().lower()
            if finalizar == "finalizar":
                print("Encerrando a calculadora. Até logo!")
                break
calculadora_adicao()