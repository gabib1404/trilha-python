# Tuplas

Anotações

### Data:  9 de janeiro de 2026

### Tópico: Tuplas

### Lembretes

### Anotações

- Tuplas são estruturas de dados semelhantes a listas, também podem armazenar quaisquer tipos de dados sequencialmente.
- Tuplas são **imutáveis**, ou seja, uma vez criadas não podem ter seus dados alterados.
- São estruturas de dados estáticas, utilizadas para armazenar dados relacionados que não devem mudar.
- Formas de criação:

```python
# Com os dados armazenados entre parênteses e separados   por vírgulas
frutas = ("laranja", "uva", "morango",)
pais = ("Brasil",) # Sempre possui uma virgula ao final (boa prática)

# Utilizando a função tuple
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
```

### Acesso direto

- Da mesma forma que é acessada uma lista.
- Utiliza-se o **índice** do elemento que vai ser acessado.

```python
frutas = ("laranja", "uva", "morango",)

print(frutas[0])
>>> laranja

print(frutas[2])
>>> morango

# Índices negativos
print(frutas[-1])
>>> morango

print(frutas[-2])
>>> uva
```

### Tuplas aninhadas

- Assim como nas listas, também podem ser criadas tuplas de tuplas (já que armezenam qualquer tipo de objetos).
- São criadas estruturas bidimensionais, que são acessadas informando os índices de linha e coluna (linha, coluna) → matriz
- Utilizadas para matrizes que não podem ter seus dados alterados.

```python
matriz = (
	(1, "a", 2),
	("b", 3, 4),
	(6, 5, "c"),
]

# [linha][coluna]
matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-2] # 5
```

### Fatiamento

- Utilizado para retornar um intervalo de elementos de uma tupla.
- Retorna uma sublista com os elementos indicados pelo intervalo.
- Usa-se os índices inicial, final(não incluso) e o passo do intervalo (quantas posições são puladas)

*tupla*[*start, stop[, step]]*

start: índice do primeiro elemento a ser selecionado do intervalo. Se não for indicado, o padrão é 0.
stop (não incluso): índice do último elemento do intervalo. O último elemento é sempre o com índice stop-1. Se não for indicado, o padrão é len(tupla).
step: passo do intervalo, quantas posições são puladas no intervalo. Se não for indicado, o padrão é 1.

```python
letras = ("p", "y", "t", "h", "o", "n",)

letras[2:] # ("t", "h", "o", "n")
letras[:2] # ("p", "y") (exclusive)
letras[1:3] # ("y", "t") (exclusive)
letras[0:3:2] # ("p", "t") (exclusive)
letras[::] # ("p", "y", "t", "h", "o", "n") sem argumentos, a lista roda inteira
letras[::-1] # ("n", "o", "h", "t", "y", "p") imprime a lista ao contrário (passo -1)
```

### Iterar tuplas

- Utilizando o método for, e do mesmo jeito que acontece com uma lista.

```python
carros = ("gol", "celta", "palio",)

for carro in carros: 
	print(carro)
	
>>> gol
>>> celta
>>> palio
```

### Função enumerate()

- Utilizada para enumerar os índices dos elementos da tupla.

enumerate(*objeto, start = 0*)
objeto: qualquer objeto iterável (sequência ou coleção).
start: valor de ínicio da enumeração dos elementos. Se não for indicado, o valor padrão é 0.

```python
carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
	print(f"{indice}: {carro}")

>>> 0: gol
>>> 1: celta
>>> 2: palio

for indice, carro in enumerate(carros, 1):
	print(f"{indice}: {carro}")
```

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  @hoje

### Tópico: Métodos da classe tuple

### Lembretes

### Anotações

### (,).count()

- Retorna a contagem de vezes que um objeto existe dentro de uma tupla.
- Apenas a contagem dos objetos IDÊNTICOS ao indicado (case sensitive e tipo de objeto.

*tupla.*count(*objeto*)

tupla: estrutura de dados da onde o item vai ser contado.
objeto: objeto que será contado.

### (,).index()

- Retorna o índice da primeira aparição de um objeto dentro da tupla.
- Se o objeto estiver presente mais de uma vez na tupla, **apenas o índice da primeira aparição é retornado,** ou seja, a primeira vez que ele aparece na tupla.
- Retorna apenas o índice do objeto IDÊNTICO ao especificado (case sensitive e tipo de objeto).

*tupla*.index(*objeto*)

objeto: objeto que será encontrado na tupla.

### len()

- Função built-in.
- Retorna o tamanho (quantidade de objetos) da tupla.

len(*objeto/tupla*)

objeto: qualquer sequência ou coleção.

<aside>
📌 **RESUMO:**

</aside>