import re

def validar_dinheiro(valor):
    padrao = re.compile(r'^\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?$')

    return True if padrao.match(valor) else [False, valor]
