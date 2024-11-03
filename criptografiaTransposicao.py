import numpy as np
from queue import Queue
def criptografa(mensagem, chave):
    mensagem = mensagem.replace(" ", "")
    qtdLinhas = (len(mensagem)//len(chave)) if len(mensagem)%len(chave) == 0 else (len(mensagem)//len(chave))+1
    matriz = np.full((qtdLinhas, len(chave)), "  ")
    
    linha = 0
    for i in range(len(mensagem)):
        if (i!=0 and i%len(chave)==0):
            linha +=1
        matriz[linha, i%len(chave)] = (mensagem[i].upper())
    # Ordem das Colunas
    ordemCerta = list(chave)
    ordemCerta.sort()
    fila = Queue()
    for t in ordemCerta:
        fila.put(t)
    stringCriptografada = []
    while not fila.empty():
        test = matriz[:,chave.find(fila.get())]
        for st in test:
            if st != "  ":
                stringCriptografada.append(st)

    return ''.join(stringCriptografada)
def ordenar_colunas(chave):
    # Retorna a ordem dos índices das colunas com base na chave
    return sorted(range(len(chave)), key=lambda k: chave[k])
def descriptografa(mensagem, chave):
    # Saber quantos caracteres terão por coluna
    # Insere a mensagem criptografada na matriz 
    qtdLinhas = (len(mensagem)//len(chave)) if len(mensagem)%len(chave) == 0 else (len(mensagem)//len(chave))+1
    matriz = np.full((qtdLinhas, len(chave)), "  ")
    linha = 0
    for i in range(len(mensagem)):
        if (i!=0 and i%len(chave)==0):
            linha +=1
        matriz[linha, i%len(chave)] = (mensagem[i].upper())
    # Quantidade de carateres que terão por coluna
    sizes = []
    for i in range(len(chave)):
        sizes.append(tamanho(matriz[:,i]))
    listSize = sorted(list(zip(chave, sizes)))
    for letra, tam in listSize:
        coluna = list(mensagem[:tam])
        if len(list(mensagem[:tam])) != matriz.shape[0]:
            coluna.append("  ")
        matriz[:,chave.find(letra)] =  coluna 
        mensagem = mensagem[tam:]    
    listDesc = []
    for linha in matriz:
        for char in linha:
            if char != "  ":
                listDesc.append(char)
    return "".join(listDesc)
def tamanho(arr):
    cont = 0 
    for i in arr:
        if i != "  ":
            cont+=1
    return cont
print(criptografa("aquecer o manguito e pros fracos", "supino"))
print(descriptografa("EAOFCNEREGPAUMTSSARURCQOIOO", "supino"))