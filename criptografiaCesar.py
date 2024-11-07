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
            msgCripto += numLetra.get((numEquivalente+key)%26)
    return msgCripto
def descriptografa(mensagem: str, key: int):
    msgDescripto = ""
    for char in mensagem:
        if char.upper() not in alfabetoNum:
            msgDescripto += char
        else:
            numEquivalente = getNum(char)
            msgDescripto += numLetra.get((abs(numEquivalente-key))%26)  
    return msgDescripto

# BREAKING CESAR
from collections import Counter
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
    # A distribuição de frequência de algumas letras 
    # Letras repetidas juntas serão no geral: rr ou ss
    ch, freq = Counter(mensagem).most_common(1)[0]
    # Casos analisados:
    numEquivalente = alfabetoNum.get(ch)
    # Casos mais comuns (f>=5): a, e, o, i, r, s, n, d 
    contMax = 0
    key = 0 
    if textPortugues(descriptografa(mensagem, (abs(alfabetoNum.get('A')-numEquivalente))).split())>=contMax:
        contMax = textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('A')-numEquivalente)).split())
        key = abs(alfabetoNum.get('A')-numEquivalente)
    if textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('E')-numEquivalente)).split())>=contMax:
        contMax = textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('E')-numEquivalente)).split())
        key = abs(alfabetoNum.get('E')-numEquivalente)
    if textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('O')-numEquivalente)).split())>=contMax:
        contMax = textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('O')-numEquivalente)).split())
        key = abs(alfabetoNum.get('O')-numEquivalente)
    if textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('I')-numEquivalente)).split())>=contMax:
        contMax = textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('I')-numEquivalente)).split())
        key = abs(alfabetoNum.get('I')-numEquivalente)
    if textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('R')-numEquivalente)).split())>=contMax:
        contMax = textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('R')-numEquivalente)).split())
        key = abs(alfabetoNum.get('R')-numEquivalente)
    if textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('S')-numEquivalente)).split())>=contMax:
        contMax = textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('S')-numEquivalente)).split())
        key = abs(alfabetoNum.get('S')-numEquivalente)
    if textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('N')-numEquivalente)).split())>=contMax:
        contMax = textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('N')-numEquivalente)).split())
        key = abs(alfabetoNum.get('N')-numEquivalente)
    if textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('D')-numEquivalente)).split())>=contMax:
        contMax = textPortugues(descriptografa(mensagem, abs(alfabetoNum.get('D')-numEquivalente)).split())
        key = abs(alfabetoNum.get('D')-numEquivalente)
    return descriptografa(mensagem, key), key
    
    
    
    
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
print(descriptografa("FGFHFYJ É GTR IJRFNX", 5))
print(bruteForce("FGFHFYJ É GTR IJRFNX"))
print(analiseFrequencia("FGFHFYJ É GTR IJRFNX"))