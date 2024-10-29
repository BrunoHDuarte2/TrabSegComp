alfabetoNum = {chr(i): i - 65 for i in range(65, 91)}
numLetra = {v: k for k, v in alfabetoNum.items()}
def getNum(letra):
    return alfabetoNum.get(letra.upper())

def criptografa(mensagem: str, key: int):
    msgCripto = ""
    for char in mensagem:
        if char.upper() not in alfabetoNum.keys():
            msgCripto += char
        else:
            numEquivalente = getNum(char)
            if numEquivalente+key>26:
                msgCripto += numLetra.get((numEquivalente+key)%26)
            else:
                msgCripto += numLetra.get(numEquivalente+key)
    return msgCripto
def descriptografa(mensagem: str, key: int):
    msgDescripto = ""
    for char in mensagem:
        if char.upper() not in alfabetoNum:
            msgDescripto += char
        else:
            numEquivalente = getNum(char)
            if numEquivalente-key<0:
                msgDescripto += numLetra.get((numEquivalente-key)%26)
            else:
                msgDescripto += numLetra.get(numEquivalente-key)
    return msgDescripto

# BREAKING CESAR

import langid
import string
from spellchecker import SpellChecker
spell = SpellChecker(language='pt')
def bruteForce(mensagem):
    contadorMax = 0
    for i in range(26):
        desc = descriptografa(mensagem, i)
        if (textPortugues(desc.split()))>=contadorMax:
            contadorMax = textPortugues(desc.split())
            descReal, key = desc, i
    return descReal, key

def analiseFrequencia(mensagem):
    ## No português há 3 casos a serem analisados
    # A distribuição de frequência de algumas letras 
    # Letras repetidas juntas serão no geral: rr ou ss
    # toda palavra no geral tem pelo menos
    pass
# Verifica se cada uma das palavras individualmente decifradas por uma chave i é parte da lingua portuguesa :)
def textPortugues(texto: list):
    if texto == []:
        return 0
    palavra = texto.pop(0)
    if palavra in spell:
        return 1 + textPortugues(texto)
    else:
        return textPortugues(texto)

print(criptografa("ABACATE É BOM DEMAIS", 5))
print(descriptografa("DEDFDWH", 3))
print(bruteForce("FGFHFYJ É GTR IJRFNX"))