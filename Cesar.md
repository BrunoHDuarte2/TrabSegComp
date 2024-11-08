# Criptografia de Cesar
Para cifrar e descifrar usando a cifra de César é relativamente fácil. O código feito utiliza de um dicionário para mapear as letras do alfabeto de 0 a 26, também foi criado um dicionário para fazer o contrário. 
### Criptografa()
A função de cifragem ou criptografia recebe a mensagem a ser criptografada e um número, que será o deslocamento. A partir disso se inicializa uma string vazia, chamemos ela aqui de 'str'. Para cada caracter na mensagem se verifica se ele é um caracter que não pertence ao alfabeto, ou seja, um espaço em branco, 'ç' ou qualquer tipo de caracter especial, pois nesse caso ele não será cifrado, caso ele não seja um char especial se seleciona o número equivalente a aquele caracter usando do dicionário e então se adiciona a 'str' a letra que é calculada como:

$ numeroDaLetra = (numChar + key) mod 26 $

Onde numChar é o número que equivale ao char que se está cifrando, dessa forma se pega o resto na divisão inteira por 26 pois dessa forma caso estejamos tentando cifrar um char 'z' com chave não nula isso resultará em um número que não tem correspondência em nosso alfabeto, dessa forma pega-se o resto que será a 'volta' dele ao nosso alfabeto. Exemplo:

$ numeroDaLetra =  (numChar(z)+3)mod26 $
Onde, numChar(z) = 25, então numeroDaLetra = 2, ou seja z será criptografado como B com chave igual a 3.

### Descriptografa()

De forma análoga a volta dessa critografia é feita utilizando ao invés de somar a chave, se subtraindo. 

### BruteForte()
A força bruta nessa criptografia é feita com base todas as chaves possíveis, tendo em vista a caracteristica cíclica dessa cifra é necessário somente 26 tentativas para quebra essa cifra, pois pela forma cíclica cifrar usando chave 3 ou $26+3$ ou $ (n*26+3),\forall n\in \mathbb{N} $. Dito isso para quebrar essa cifra basta testar toda chave que segue:
$ (chave \geq 0)\land(chave\leq25) $ 
Dessa forma, ao fazer um loop por todas essas possibilidades a mensagem é quebrada em algum momento. No código para identificar quando a mensagem foi quebrada foi utilizada uma biblioteca para servir como um dicionário de lingua portuguesa, assim para cada tentativa de descriptografar é gerado uma lista de palavras, uma frase, que para estar descriptografada necessariamente deve estar em português. Então é validado se alguma palavra na frase pertence ao português se pertencer então está descriptografado.

### AnaliseFrequencia()
Utilizando algumas caracteristicas da lingua portuguesa pode-se melhorar a efetividade de uma brute force. Utilizando a distribuição de frequência dada, se extraiu a letra mais comum numa mensagem cifrada e então pode-se tentar os casos mais comuns na nossa língua, foi separado 10 casos mais comuns: a, e, o, i, r, s, n, d.
E então, em ordem se calcula a diferença entre a letra mais frequente na mensagem e os casos mais comuns, para então descifrar a mensagem com essa diferença, se caso alguma tentativa dessas gerar uma frase que contém palavras em português se retorna a mensagem descriptografada e a chave utilizada.
Dessa forma, esse método se mostra uma alternativa ao BruteForce mas que funciona de forma parecida, apenas tentando se diminuir o espaço de tentativas. 
