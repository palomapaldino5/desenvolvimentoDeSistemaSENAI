"""
1) faça uma calculadora com as 4 operações configuradas ( +,-,*,/)
"""
def calculadora_adicao():
    print("Bem-vindo à calculadora de adição!")

    while True:
        try:
            # Solicitar entrada do usuário
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
            # Verificar se o usuário quer finalizar
            finalizar = input("Você digitou algo inválido. Digite 'finalizar' para encerrar ou pressione Enter para continuar: ").strip().lower()
            if finalizar == "finalizar":
                print("Encerrando a calculadora. Até logo!")
                break
# Executar a calculadora
calculadora_adicao()

