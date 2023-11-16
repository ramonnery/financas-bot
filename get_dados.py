from json_in_dict import json_in_dict


def get_dados():
    dados = json_in_dict('dados.json')

    gastos = dados['gastos']
    resultado = []

    for gasto in gastos:
        desc, val = gasto.items()

        resultado.append(f'{desc[1]}: R$ {val[1]:.2f}')

    return resultado

