import numpy as np
import math

def descriptografa(mensagem, chave):
    # Calcular número de linhas necessárias
    qtdLinhas = math.ceil(len(mensagem) / len(chave))
    
    # Criar a matriz com espaços vazios
    matriz = np.full((qtdLinhas, len(chave)), " ")
    
    # Ordenar as colunas de acordo com a chave
    ordemColunas = sorted(range(len(chave)), key=lambda x: chave[x])
    
    # Preencher a matriz com os caracteres da mensagem
    idx = 0
    for i in range(len(chave)):
        col = ordemColunas[i]  # índice da coluna de acordo com a ordem da chave
        for j in range(qtdLinhas):
            if idx < len(mensagem):  # Certificar-se de que o índice não ultrapassa o tamanho da mensagem
                matriz[j, col] = mensagem[idx]
                idx += 1
    print(matriz)
    # Recuperar a mensagem original ao ler a matriz linha por linha
    listaDesc = []
    for linha in matriz:
        listaDesc.extend(linha)
    
    # Juntar os caracteres em uma string e retornar
    return "".join(listaDesc).strip()

# Exemplo de uso
mensagem_cifrada = "E IPR CMTRA EAOOC UOU F ARN SOQ GE S"
chave = "eadcbgf"

# Descriptografar a mensagem
mensagem_original = descriptografa(mensagem_cifrada, chave)
print(f"Mensagem original: {mensagem_original}")
