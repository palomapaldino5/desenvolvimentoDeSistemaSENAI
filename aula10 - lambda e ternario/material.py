def converterDolar(valor):
    valor *= 5.82
    return valor

print(converterDolar(5))

# def nome (parametro)
# processo
# vs
# lambda parametro : processo

# VANTAGEM DO LAMBDA
# RESUME PROCESSOS SIMPLES
# AJUDA LEGIBILIDADE
# EVITAR CHAMAR UM DEF EM CASO DE UMA LINHA

# DESVATAGENS
# NÃO É EFICAZ EM PROCESSOS MAIORES
# EM FALTA DE ATANÇÃO, DIFICULTA VARAIAVEIS
converterEuro = lambda valor : valor * 6.66
converterIene = lambda valor , taxa : valor / 0.03 - taxa
print(converterEuro(20))
print(converterIene(1000,40))

# TERNARIO
condicao = True
if condicao:
    print('IF')
else:
    print('ELSE')

print('IF') if condicao else print('ELSE')

valor = 0
(valor + 1) if condicao else valor
print(valor)