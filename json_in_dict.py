import json

def json_in_dict(file_path):
    with open(file_path, 'r') as file:
        dados = json.load(file)

    return dados