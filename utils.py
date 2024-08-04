# utils.py

def validar_entrada_int(entrada, default=1):
    try:
        return int(entrada)
    except ValueError:
        return default
