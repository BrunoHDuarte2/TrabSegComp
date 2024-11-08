# Cifra de Transposição
Baseada em permutação dos elementos da mensagem e pode ser feita de várias formas diferentes, nesse caso foi utilizado a forma colunar.
### Criptografa()
A mensagem é inserida numa matriz que possui a quantidade de colunas e linhas baseada em relações com a chave, por exemplo, quantidade de colunas será o tamanho da chave e a de linhas é a divisão inteira do tamanho da mensagem pelo tamanho da chave.
Dessa forma, com a mensagem inteira na matriz simplesmente é escolhido as colunas de forma ordenada de acordo com a chave e então é retornado a string equivalente a junção das colunas em ordem. 
Exemplo:
Mensagem = "Eu amo abacate"
Chave = "Mentira"

| M | E | N | T | I | R | A |
|---|---|---|---|---|---|---|
| E | U |" "| A | M | O |" "|
| A | B | A | C | A | T | E |

Ordenando as colunas se tem:

| A | E | I | M | N | R | T |
|---|---|---|---|---|---|---|
|" "| U | M | E |" "| O | A |
| E | B | A | A | A | T | C |

Onde cada coluna é dada por:
1° " "E
2° UB
3° MA
4° EA
5° " "A
6° OT
7° AC

Dessa forma mensagem criptografada fica: _EUBMAEA AOTAC, considere o underscore no inicio como um espaço vazio, foi deixado assim para melhor visualização.

### Descriptografa()
De forma análoga, é feita a descriptografia quebrando a mensagem em blocos de tamanho igual a quantidade de linhas que será necessária para preencher a matriz com a mensagem. Assim sabendo a ordem das colunas, que é dada pela chave, é simplesmente inserir esses blocos de tamanho igual na coluna equivalente a ele. Por exemplo, o primeiro bloco da mensagem será inserido na coluna que corresponde ao caracter mais próximo ao inicio no nosso alfabeto, e assim para todo o resto da mensagem. Feito toda a inserção da mensagem na matriz, basta ler cada linha, ou no caso do código concatenar todas as linhas e retornar. 

### BruteForce()
Para realizar a bruteforte na cifra de transposição é necessário passar por todos os tamanhos de chave possíveis e por todas as permutações da chave possível. Dessa forma basta um loop com i entre 1 e o tamanho da mensagem que realiza um loop entre todas as permutações possíveis de chave com tamanho i e tentar descriptografa-las.

OBS: Dessa forma não é possível se retornar a chave exata que foi usada na criptografia, mas é possível retornar uma ordem de colunas que satisfaz o problema. 