from json_in_dict import json_in_dict
import json

dados = json_in_dict('dados.json')

def create_dados(descricao, valor):

    novo_gasto = {"descricao": descricao, "valor": valor}
    dados['gastos'].append(novo_gasto)

    json_atualizado = json.dumps(dados, indent=4)

    with open('dados.json' , 'w') as json_file:
        json_file.write(json_atualizado)

    return True


print(create_dados('Danone', 14.0))