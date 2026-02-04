# Listas

Anotações

### Data:  7 de janeiro de 2026

### Tópico:

### Lembretes

**Introdução**

**Formas de acesso**

🔴 o for do python se assemelha ao do Java! revisar/ dar uma olhada!

### Anotações

- Listas podem armazenar de maneira sequencial qualquer tipo de objeto.
- São objetos **mutáveis,** podendo ter seus dados alterados após a sua criação.
- Formas de criação:

```python
# Objetos dentro de colchetes separados por vírgulas
frutas = ["laranja", "maçã"]

# Lista vazia
frutas = []

# Método list

# Separa o elemento em "pedaços"
letras = list("python") # Cada letra é um elemento, não é uma lista com o objeto "pyhton"
>>> letras = ["p", "y", "t", "h", "o", "n"]

# Com a função range
numeros = list(range(10))

# Listas com objetos de diferentes tipos
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
```

### Acesso direto

- Utiliza os índices da lista para acessar os objetos.
- A sequência do índice é iniciada a partir de 0.

```python
letras = ["p", "y", "t", "h", "o", "n"]

letras[0] # p
letras[5] # n
letras[3] # h
```

<aside>
🎯

### Índices negativos

É possível acessar os últimos elementos de uma lista sem saber o índice deles (ou a quantidade de elementos que existem na lista).

Para isso, é utilizado o índice negativo (iniciado em -1).

```python
letras = ["p", "y", "t", "h", "o", "n"]

letras[-1] # n
letras[-2] # o
letras[-3] # h
```

Também pode-se criar uma cópia da lista ao contrário pelo uso dos índices negativos.

</aside>

### Listas aninhadas

- Como as listas são objetos que podem armazenar qualquer tipo de objeto, listas também podem conter listas como objetos dentro delas. Esses casos são chamados de listas aninhadas.
- Criam estruturas bidimensionais (tabelas). Com acesso de informação com índices de linhas e colunas → matrizes

```python
matriz = [
	[1, "a", 2],
	["b", 3, 4],
	[6, 5, "c"]
]

# [linha][coluna]
matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-2] # 5
```

### Fatiamento

- Acesso de um conjunto de objetos da lista através de um intervalo de índices (final, inicial, passo).
- Cria uma nova lista (sublista) que contenha os objetos presentes no intervalo indicado.

lista[start : stop : step] → Todos os elementos são “opcionais”, e o parâmetro stop é exclusive (stop - 1).

```python
letras = ["p", "y", "t", "h", "o", "n"]

letras[2:] # ["t", "h", "o", "n"]
letras[:2] # ["p", "y"] (exclusive)
letras[1:3] # ["y", "t"] (exclusive)
letras[0:3:2] # ["p", "t"] (exclusive)
letras[::] # ["p", "y", "t", "h", "o", "n"] sem argumentos, a lista roda inteira
letras[::-1] # ["n", "o", "h", "t", "y", "p"] imprime a lista ao contrário (passo -1)
```

### Iterar listas

- Para percorrer uma lista, é (majoritariamente) utilizado o método **for.**

```python
carros = ["gol", "celta", "palio"]

for carro in carros:
	print(carro)
	
>>> gol
>>> celta
>>> palio
```

<aside>
❗

### Comando for

python: 

```python
for i in range(10):
	# bloco de código
```

C: 

```c
for(int i = 0; i < 10; i++):
	// bloco de código
```

i (variável de iteração): variável que irá percorrer o objeto no for. Indica o índice do objeto que está sendo percorrido.

range(10) ou i<10 (objeto a ser percorrido): indica a quantidade de iterações que o for irá executar. Em ambas as situações, a quantidade e forma dos índices será a mesma [0, 1, … , 9].

</aside>

### Função enumerate:

- Utilizada quando é necessário saber qual o ínidice de um objeto dentro do for. (*”Onde está o objeto X da lista Y? Qual o índice que indica sua posição?”*)

```python
for indice, carro in enumerate(carros): 
	print(f"{indice}: {carro}")
	
>>> 0: gol
>>> 1: celta
>>> 2: palio
```

A função funciona da mesma forma que: 

```python
for i in range(len(carros)): 
	print(f"{i}: {carros[i]}")
```

<aside>
❗

### Função enumerate()

- A função enumerate é utilizada para enumerar itens de um objeto iterável (capaz de ser “rodado”).
- A função gera uma tupla (lista imutável) com 2 parâmetros (indice e objeto).
- Retorna um objeto enumerado.

```python
cidades = ["Londres", "São Paulo", "Nova York"]

list(enumerate(cidades))
>>> ([0, "Londres"], [1, "São Paulo"], [2, "Nova York"])
```

Sintaxe: 

enumerate(*iterable*,  *start = x*)

- *iterable:* objeto iterável (deve ser uma sequência).
- *start = x (opcional):* define com qual índice a sequência vai ser iniciada. Se x = 1, o índice do primeiro objeto é 1.
Se não for indicado, o valor padrão é 0.
</aside>

### Compreensão de listas

- Oferece uma sintaxe mais curta para criar uma nova lista com base em uma já criada ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

### Filtros

```python
numeros = []
pares = []

for numero in numeros: 
	if numero % 2 == 0: # Verifica se o número é par
		pares.append(numero) # Adiciona o item ao final da lista
```

- append: Adiciona um item ao final da lista.

```python
numeros = []
pares = [numero for numero in numeros if numero % 2 == 0]
```

- pares  = [*verdadeiro* for *variavel* in *objeto iteravel* if *condição falso*] → diminui o código para uma linha.
- Se a condição do if (numero % 2 == 0) for verdadeira, numero é adicionado a lista pares, se for falsa não acontece nada. O objeto (lista numeros) é iterado novamente, e a mesma verificação de condição acontece.

### Modificando valores

```python
numeros = []
quadrado = []

for numero in numeros: 
	quadrado.append(numero**2) #  Eleva os valores de 'numeros' ao quadrado e adiciona no fim da lista 'quadrado'
```

```python
numeros = []
quadrado = [numero** 2 for numero in numeros]
```

- A cada nova iteração do for da lista ‘numeros’ o quadrado do número da lista é adicionado na lista ‘quadrado’.

<aside>
📌  **RESUMO:**

</aside>
		

Anotações

### Data:  8 de janeiro de 2026

### Tópico: Métodos da classe list

### Lembretes

🔴 Anotar sobre os parâmetros de fatiamento da lista no index!!!!

### Anotações

### [].append()

- Adiciona um elemento ao fim da lista.
- Qualquer tipo de objeto pode ser adicionado a lista com esse método.

*lista*.append(*objeto*)

lista: lista onde os objetos serão adicionados

objeto: qualquer tipo de objeto a ser adicionado na lista.

```python
lista = []

lista.append(2)
lista.append("cinco")
lista.append(2.75)
lista.append([1, 5, 9])

print(lista)
>>> [2, "cinco", 2.75, [1, 5, 9]]
```

### [].clear()

- Deleta todos os itens da lista.
- Deixa a lista desejada vazia.

*lista.*clear()

```python
lista = [2, "cinco", 2.75, [1, 5, 9]]

lista.clear()

print(lista)
>>> []
```

### [].copy()

- Copia todos os itens de uma lista.
- Pode guardar os itens dentro de outra lista → cria uma cópia.
- Cria um novo objeto idêntico ao antigo, porém as mudanças feitas em uma lista não vão ser refletidas na outra (ids diferentes = objetos diferentes)

*lista.*copy()

*lista:* lista a ser copiada.

```python
lista = [2, "cinco", 2.75, [1, 5, 9]]

copia_lista = lista.copy()

print(copia_lista)
>>> [2, "cinco", 2.75, [1, 5, 9]]

# Alterações

copia_lista[2] = "vinte e dois"

print(lista)
print(copia_lista)

>>> [2, "cinco", 2.75, [1, 5, 9]]
>>> [2, "vinte e dois", 2.75, [1, 5, 9]]
```

### [].count()

- Utilizado para verificar quantas vezes um objeto aparece dentro da lista.
- Retorna uma contagem → número de cada objeto indicado.
- Retorna apenas a contagem dos objetos IDÊNTICOS ao indicado (case sensitive e diferentes tipos)

*lista.*count(*objeto*)

*objeto*: objeto a ser contado .

```python
cores_favoritas = ["vermelho", "verde", "azul", "azul", "vermelho", "azul", "roxo"]

# Case sensitive
cores_favoritas.count("vermelho") # 3
cores_favoritas.count("azul") # 2
cores_favoritas.count("Roxo") # 0
cores_favoritas.count("verMelho") # 0

numeros = [2, 2, 2, '2', 2]

# Diferentes tipos
numeros.count(2) # 4
numeros.count('2') # 1
```

### [].extend()

- Junta duas listas existentes em uma indicada.
- Concatena um objeto iterável em uma lista. Funciona como um +=.

*lista*.extend(*objeto_iteravel*)

lista: lista onde o objeto vai ser adicionado.

objeto_iteravel: objeto/lista a ser adicionada a lista indicada.

```python
linguagens = ["python", "java", "c#"]

linguagens.extend(["javascript", "php"])
# linguagens += ["javascript", "php"]

print(linguagens)
>>> ["python", "java", "c#", "javascript", "php"]
```

### [].index()

- Retorna o índice  da primeira ocorrência de um objeto especificado.
- Se o objeto estiver presente mais de uma vez na lista, **apenas o índice da primeira aparição é retornado,** ou seja, a primeira vez que ele aparece na lista.
- Retorna apenas o índice do objeto IDÊNTICO ao especificado (case sensitive e tipo de objeto).

*lista.*index*(objeto)*

lista: lista onde o objeto vai ser procurado.
objeto: objeto a ser procurado na lista. 

```python
linguagens = ["python", "java", "c#", "javascript", "java", "php"]

linguagens.index("php") # 5
linguagem.index("java") # 1 -> apenas a primeira aparição
linguagem.index("Java") # ValueError -> objeto não existe na lista
```

### [].pop()

- Pelo comportamento padrão da lista ser de “pilha” (O último elemento adicionado é o último elemento da lista, e o primeiro a ser retirado se é preciso acesso aos demais), a função .pop() retira o último elemento adicionado.
- Pode ser utilizado de duas formas: se o índice não for indicado, o último elemento à ser adicionado na lista é apagado. Se indicar o índice, o objeto daquele referido índice é apagado da lista.

*lista.*pop(*indice*)

lista: lista de onde o objeto será retirado.
indice (opcional): indice do objeto a ser retirado da lista. Se não for indicado o índice padrão é o do último objeto da lista (lista.pop(len(lista)))

```python
linguagens = ["python", "java", "c#", "javascript", "php"]

linguagens.pop() # php
# ["python", "java", "c#", "javascript"]

linguagens.pop() # javascript
# ["python", "java", "c#"]

linguagens.pop(1) # java
# ["python", "c#"]
```

### [].remove()

- Remove da lista o objeto indicado. Difere-se do .pop() por que o ELEMENTO é indicado, não o ÍNDICE.
- Remove apenas a primeira aparição do objeto indicado. Se ele estiver presente mais vezes na lista, apenas uma ocorrência é removida.
- Remove apenas objetos IDÊNTICOS ao indicado (case sensitive e tipo do objeto).

*lista*.remove(*objeto*)

lista: lista onde o objeto será removido.
objeto: objeto a ser removido da lista.

```python
linguagens = ["python", "java", "c#", "javascript", "php"]

linguagens.remove("python")
# ["java", "c#", "javascript", "php"]

linguagens.remove("Java") # ValueError -> objeto não existe na lista
```

### [].reverse() → in-place

- Utilizado para fazer a inversão da lista.
- Inverte a lista sem precisar criar uma cópia (in-place).

*lista*.reverse()

lista: lista que será invertida.

```python
linguagens = ["python", "java", "c#", "javascript", "php"]

linguagens.reverse()
print(linguagens)
>>> ["php", "javascript", "c#", "java", "python"]

# Assim como:
nova_lista = linguagens[::-1]
print(nova_lista)

```

- A diferença entre o .reverse() e o step do fatiamento ser -1, é que o reverse inverte a própria lista (o próprio elemento ‘linguagens’ é modificado) e o fatiamento cria uma cópia da lista (que deve ser armazenada em outro objeto).

### [].sort() → in-place

- Ordena a lista de acordo com alguns parâmetros informados, mantendo as mudanças no objeto original (in-place)

*lista.*sort(**, key = None, reverse = False*)

*: ‘*keyword-only parameters separator*’, indica que todos os parâmetros escritos após o * DEVEM ser indicados explicitamente utilizando o seu nome (*nome_parametro = valor).*
key =: Critério de ordenação personalizado. Se não for indicado, seu padrão é None.
reverse =: Define se a ordenação será crescente ou decrescente. Se não for indicado, seu padrão é False, ordem crescente para números e ordem alfabética para strings. Se for True, a ordem é decrescente para ambos os casos.

```python
linguagens = ["python", "java", "c#", "javascript", "php"]

# Uso padrão
linguagens.sort()
print(linguagens)
>>> ["c#", "java", "javascript", "php", "python"] # Ordem alfabética

# Indicando reverse
linguagens.sort(reverse = True)
print(linguagens)
>>> ['python', 'php', 'javascript', 'java', 'c#']

# Utilizando key
# Ordena a lista por tamanho das strings (qntd de caracteres)
linguagens.sort(key = lambda x : len(x)) # ou key = len
print(linguagens)
>>> ['c#', 'php', 'java', 'python', 'javascript']

# Ordem decrescente
linguagens.sort(key = len, reverse = True)
print(linguagens)
>>> ['javascript', 'python', 'Java', 'PHP', 'C#']

# Para ignorar letras maíusculas (se houvesse) -> são    colocadas primeiro
linguagens.sort(key = str.lower)
print(linguagens)
>>> ['C#', 'Java', 'javascript', 'PHP', 'python']
```

<aside>
❗

### função *lambda*

- A função lambda é uma função pequena e anônima.
- A função pode receber um número infinito de argumentos, mas possui apenas uma expressão.

```python
lambda argumentos: expressao
```

- Exemplos:

```python
x = lambda a : a * 5

print(x(10))
>>> 50
```

</aside>

### len()

- Utilizado para verificar o tamanho de algum objeto.
- Número de caracteres de uma string, número de elementos de uma lista, etc.
- Retorna um número inteiro.

len(*objeto*)

objeto: sequencia ou coleção.

```python
linguagens = ['python', 'php', 'javascript', 'java', 'c#']

print(len(linguagens))
>>> 5

print(len("php"))
>>> 3
```

### sorted()

- Função built-in que funciona da mesma forma que o .sort().
- A principal diferença é que o sorted cria uma cópia do objeto, e o .sort() retorna o mesmo objeto modificado.
- sorted funciona para diversos tipos de objetos (como o len).

sorted(*objeto_iteravel*, **, key = None, reverse  = False*)

Os parâmetros são os mesmos que o .sort()

objeto_iteravel: sequência ou coleção.
*: ‘*keyword-only parameters separator*’, indica que todos os parâmetros escritos após o * DEVEM ser indicados explicitamente utilizando o seu nome (*nome_parametro = valor).*
key =: Critério de ordenação personalizado. Se não for indicado, seu padrão é None.
reverse =: Define se a ordenação será crescente ou decrescente. Se não for indicado, seu padrão é False, ordem crescente para números e ordem alfabética para strings. Se for True, a ordem é decrescente para ambos os casos.

```python
linguagens = ['python', 'php', 'javascript', 'java', 'c#']

print(sorted(linguagens))
>>> ['C#', 'Java', 'PHP', 'javascript', 'python']

print(sorted("python"))
>>> ['h', 'n', 'o', 'p', 't', 'y']

print(sorted("python", reverse = True))
>>> ['y', 't', 'p', 'o', 'n', 'h']
```

<aside>
📌 **RESUMO:**

</aside>