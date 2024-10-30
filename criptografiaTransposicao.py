alfabetoNum = {chr(i): i - 65 for i in range(65, 91)}
numLetra = {v: k for k, v in alfabetoNum.items()}
def criptografa(mensagem, chave):
    qtdColunas = len(chave)
    for char in mensagem:
        if char.upper() in alfabetoNum.keys():
            pass