"""
2)Programe um algoritmo onde podemos colocar um valor em reais e logo a pós perguntar 
qual moeda deseja converter ( Dólares, Ienes ou euro) e logo após isso fazermos a conversão
"""
def conversor_moedas():
    # Taxas de câmbio (valores fictícios, atualize conforme necessário)
    taxas = {
        "1": {"nome": "Dólar", "simbolo": "$", "taxa": 5.85},
        "2": {"nome": "Euro", "simbolo": "€", "taxa": 6.20},
        "3": {"nome": "Iene", "simbolo": "¥", "taxa": 0.043}
    }

    try:
        # Entrada do valor em reais
        valor_reais = float(input("Digite o valor em reais (R$): "))
        
        # Escolha da moeda
        print("\nEm qual moeda deseja converter:")
        for key, moeda in taxas.items():
            print(f"{key} - {moeda['nome']} ({moeda['simbolo']})")
        
        opcao = input("\nDigite o número correspondente à moeda desejada: ")

        # Verificação da opção e cálculo
        if opcao in taxas:
            moeda_selecionada = taxas[opcao]
            valor_convertido = valor_reais / moeda_selecionada["taxa"]
            print(f"\nR$ {valor_reais:.2f} equivalem a {moeda_selecionada['simbolo']} {valor_convertido:.2f} ({moeda_selecionada['nome']}).")
        else:
            print("\nOpção inválida! Por favor, escolha uma moeda válida.")
    except ValueError:
        print("\nErro: Por favor, insira um valor numérico válido para o valor em reais.")

# Executa o programa
conversor_moedas()
