import numpy as np
import itertools as it
import math
from queue import Queue
from spellchecker import SpellChecker
spell = SpellChecker(language='pt')
def criptografa(mensagem, chave):
    qtdLinhas = (len(mensagem)//len(chave)) if len(mensagem)%len(chave) == 0 else (len(mensagem)//len(chave))+1
    matriz = np.full((qtdLinhas, len(chave)), " ")
    
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
            stringCriptografada.append(st)

    return ''.join(stringCriptografada)
def ordenar_colunas(chave):
    # Retorna a ordem dos índices das colunas com base na chave
    return sorted(range(len(chave)), key=lambda k: chave[k])
def descriptografa(mensagem, chave):
    qtdLinhas = math.ceil(len(mensagem)/len(chave))
    matriz = np.full((qtdLinhas, len(chave)), " ")
    ordemColunas = sorted(chave)
    for i in range(len(chave)):
        coluna =list(mensagem[:qtdLinhas])
        if len(coluna)!=qtdLinhas and len(mensagem)<qtdLinhas:
            coluna = arrumaColuna(coluna, qtdLinhas)
        matriz[:, chave.find(ordemColunas[i])] =  coluna
        mensagem = mensagem[qtdLinhas:]
    listDesc = []
    for linha in matriz:
        for char in linha:
            listDesc.append(char)
    return "".join(listDesc)
def arrumaColuna(coluna, qtd):
    while len(coluna)!=qtd:
        coluna.append(" ")
    return coluna
def bruteForce(mensagem):
    for i in range(len(mensagem)):
        p = it.permutations(criaChave(i+1))
        p = [''.join(p) for p in set(p)]
        for j in p:
            palavras = descriptografa(mensagem, j).split()
            palavrasEmPT = [item in spell for item in palavras]
            if all(item for item in palavrasEmPT):
                return (descriptografa(mensagem, j), j)
def analise():
    pass

def criaChave(int):
    return ''.join(chr(ord('a') + j) for j in range(int))
print(criptografa("eu amo chocolate", "amor"))
print(descriptografa("EMHLUOOA  CTACOE", "amor"))
print(bruteForce("EMHLUOOA  CTACOE"))

print(sorted("MENTIRA"))