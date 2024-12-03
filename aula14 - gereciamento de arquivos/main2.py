arquivo = 'teste.txt'

import json
usuario = {
    'nome' : 'Emilia',
    'idade': 15,
    'cep': '888888-555', 
}

#criar json
#json.dump = joga os dados
with open('dados.json', 'w', encoding='utf8') as leitura:
    json.dump(
        usuario,
        leitura,
        indent=2

    )
    #leitura.write('ATENÇÃO!!!')

    with open('dados.json', 'w', encoding='utf8') as leitura:
        pessoa = json.load(leitura)
        print(pessoa['nome'])