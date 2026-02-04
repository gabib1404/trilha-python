# Tipos de operadores com Python

Anotações

### Data:  11 de dezembro de 2025

### Tópico: Operadores Aritméticos

### Lembretes

O que são operadores aritméticos?

Exemplos:

### Anotações

- Executam operações matemáticas com operandos

```python
# Adição 
print(1 + 2)
>>> 3

# Subtração
print(8 - 5)
>>> 3

# Multiplicação
print(5 * 4)
>>> 20

# Divisão
print(12 / 3) -> Sempre retorna um tipo 'float'
>>> 4.0

# Divisão inteira
print(12 // 5) -> Retorna um valor do tipo 'int' SEMPRE arrendondando para baixo.
>>> 2

# Módulo (resto da divisão)
print(10 % 3)
>>> 1

# Exponenciação
print(2 ** 3)
>>> 8
```

### Precedência dos operadores

1. Parêntesis
2. Expoentes
3. Multiplicações e divisões (esquerda para a direita)
4. Adições e subtrações (esquerda para a direita)

```python
print(10 - 5 * 2)
>>> 0

print((10 - 5)* 2)
>>> 10

print(10 ** 2 * 3) -> exponenciação, depois multiplicação
>>> 300

print((10 * 3) ** 2)
>>> 900

print(10 / 2 * 4)
>>> 20.0
```

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  16 de dezembro de 2025

### Tópico: Operadores de Comparação

### Lembretes

### Anotações

- São operadores utilizados para comparar dois valores.

```python
# Igualdade
saldo = 450
saque = 200

print(saldo == saque)
>>> False

# Diferença

print(saldo != saque)
>>> True

# Maior que/Maior ou igual
saldo = 450
saque = 450

print(saldo > saque)
>>> False

print(saldo >= saque)
>>> True

# Menor que/Menor ou igual
saldo = 450
saque = 200

print(saldo < saque)
>>> False

print(saldo <= saque)
>>> False
```

- A variável que retorna uma comparação entre dois valores é *booleana.*

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  16 de dezembro de 2025

### Tópico: Operadores de atribuição

### Lembretes

### Anotações

- São usados para definir o valor inicial, ou sobrescrever o valor de uma variável

### Atribuição Simples

- Mais utilizado dos operadores.
- Representado por ‘=’.
- *variável = valor;*

```python
saldo = 500

print(saldo)
>>> 500
```

### Atribuição com adição

- No momento de atribuição do valor, ele já é modificado pela operação de soma.
- Representado por ‘+=’.

```python
saldo = 500
saldo += 200 # saldo = saldo + 200

print(saldo)
>>> 700
```

- valor inicial: 500
500 += 200
500 + 200 = 700

### Atribuição com outras operações

```python
# Com subtração
saldo -= 100 # saldo = saldo - 100

print(saldo)
>>> 400

# Com multiplicação
saldo *= 2 # saldo = saldo * 2

print(saldo) 
>>> 800

# Com divisão
saldo /= 4 # saldo = saldo / 4

print(saldo)
>>> 200.0

# Com divisão inteira
saldo //= 100 # saldo = saldo // 100

print(saldo)
>>> 2

# Com módulo 
saldo %= 3 # saldo = saldo % 3

print(saldo)
>>> 2

# Com exponenciação
saldo **= 3 # saldo = saldo**3

print(saldo)
>>> 8
```

<aside>
❗

A divisão inteira ( // ) só serve se você divide números inteiros. Pelo contrário, a variável que é retornada é do tipo *float*, porém truncada.

Exemplo: 

```python
print(10.5 // 2)
>>> 5.0 # Resultado deveria ser 5.25

print(11 // 2.5)
>>> 4.0 # Resultado deveria ser 4.4
```

</aside>

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  18 de dezembro de 2025

### Tópico: Operadores Lógicos

### Lembretes

### Anotações

- São operadores utilizados em conjunto com operadores de comparação, para montar uma expressão lógica.
- O valor retornado é um *booleano.*

### Operador *E (and)*

```python
saldo = 1000
saque = 200
limite = 100 # Atribuição simples

saldo >= saque and saque <= limite
>>> False
```

- O operador E funciona assim:

|  |  |  |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |
- APENAS se todas as condições forem verdadeiras (1), o resultado retornado é um *True.*

### Operador *OU (or)*

```python
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
>>> True
```

- Para o resultado da expressão ser verdadeiro, apenas uma das condições precisa ser verdadeira.

| 0 | 0 | 0 |
| --- | --- | --- |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |
- Contrário do E.

### Operador de negação (*not*)

- Ele inverte o sinal de qualquer expressão.

```python
contatos_emergencia = [] # Lista

not 1000 > 1500
>>> True 
# 1000 não é maior que 1500, mas o *not* inverte o valor

not contatos_emergencia
>>>  True
# Lista vazia em Python é falso, o valor booleano é *False*

not "saque 1500;"
>>> False
# String preenchida retorna um valor booleano *True*

not ""
>>> True
# String vazia retorna um valor booleano *False*
```

### Parênteses

- Assim como nas expressões matemáticas, os parênteses nas expressões lógicas também têm a função de alterar a precedência das operações.

```python
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
>>> True
# Não existe precedência maior, a expressão é resolvida da esquerda para a direita

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
>>> True

```

- Ambas as expressões representam a mesma situação, porém a segunda se torna mais legível e de melhor entendimento.

<aside>
💡

diquinhas: 

- Não é recomendado fazer expressões loógicas muito grandes, por isso, é possível quebrar as expressões em partes e atribuí-las a variáveis.
    
    ```python
    conta_normal = saldo >= saque and saque <= limite
    conta_especial_saldo = conta_especial and saldo >= saque
    
    expressao = conta_normal or conta_especial_saldo
    print(expressao) 
    >>> True
    ```
    
- Assim, o código vai se tornando cada vez mais legível!

</aside>

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  18 de dezembro de 2025

### Tópico: Operadores de identidade

### Lembretes

### Anotações

- Operadores utilizados para comparar se dois objetos testados ocupam a mesma posição na memória
- Para essa situações, é utilizado o operador *is.*
- Existe também o operador *is not*, que compara se dois objetos NÃO ocupam o mesmo espaço de memória.

```python
curso = "Curso de Python"
nome_curso = curso
# Uma variável recebe a outra

saldo, limite = 200, 200
# Ambas as variáveis recebem o mesmo valor

curso is nome_curso
>>> True
	# Pois o objeto 'nome_curso' referencia o objeto 'curso',
	# ou seja, 'nome_curso' e 'curso' possuem a mesma localidade na memória.
	
nome_curso is not curso
>>> False
	# O retorno é falso pois (como visto acima), ambos os 
	# objetos possuem o mesmo espaço na memória
	
saldo is limite
>>> True
#
```

<aside>
💡

Interning (Reutilização de objetos comuns): 

É uma otimização utilizada pelo Python que cria apenas um objeto na memória, mas que pode ser acessado por diferentes variáveis.

- **Geralmente** é utilizada para objetos pequenos (números de -5 a 256, strings pequenas sem espaços e booleanos).
- É possível verificar se isso acontece com dois objetos observando os IDs de ambos - se forem iguais, ocupam o mesmo espaço na memória.

```python
saldo = 200
limite = 200

print(id(saldo))
print(id(limite))
>>> 140727839788168
>>> 140727839788168
```

</aside>

- O operador *is* é igual uma comparação de IDs de variáveis.
- Ambas as funções são as mesmas.

```python
if id(a) == id(b) 
a is b
```

<aside>
❗

O operador de identidade *is* e o operador de comparação ‘==’ NÃO têm a mesma função!

==: Compara se os valores das variáveis são os mesmos.
Os objetos podem não ocupar o mesmo lugar na memória, mas se os valores são iguais, o valor retornado da expressão é *True.*

is: Compara se os objetos compartilham o mesmo lugar na memória. Os valores dos objetos têm que ser iguais, assim como o ID.
Se o objeto é o mesmo (ID e valor), o valor retornado é *True.*

</aside>

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  19 de dezembro de 2025

### Tópico: Operadores de Associação

### Lembretes

🔴 O operador *in* é o utilizado no *for!*

### Anotações

- São operadores utilizados para verificar se um objeto está presente em uma sequência ou não.
- Os operadores são: *in* e *not in.*
- in: verifica se o objeto ESTÁ na sequência.
not in:  verifica se o objeto NÃO ESTÁ presente na sequência.

```python
curso = "Curso de Python" # Sequência de caracteres
frutas = ["laranja", "uva", "morango"] # Lista
numeros = (1500, 1000, 2000) # Tupla

"Python" in curso:
>>> True

"maçã" not in frutas:
>>> True

1000 not in saques:
>>> False
```

<aside>
📌 **RESUMO:**

</aside>