# Conjuntos

Anotações

### Data:  12 de janeiro de 2026

### Tópico: Conjuntos

### Lembretes

### Anotações

- Set é uma coleção de elementos únicos, que não se repetem. Representam conjuntos matemáticos e eliminam duplicações de elementos de um objeto iterável.

```python
# Eliminar duplicações
set([1, 2, 5, 2, 6]) # {1, 2, 5, 6}

set("abacaxi") # {"b", "a", "c", "x", "i"} 
set(("palio", "gol", "celta", "palio")) # {}
```

- O conjunto (set) não garante a ordem dos elementos (muda a cada execução). Não é uma estrutura de dados para ordenar elementos.

- Um set pode ser declarado de duas formas: utilizando a função set() ou colocando os elementos entre duas chaves.

```python
# Entre duas chaves
linguagens = {"python", "java", "c#", "java"}
print(linguagens)
>>> {'python', 'java', 'c#'} # Muda a cada execução
```

- OBS: Colocar os elementos entre chaves, é uma forma possível de criar um set. Porém, é mais comum a utilização de um iterável dentro da função set. 
Pois, se você sabe os elementos que serão adicionados ao conjunto, não é comum colocar elementos repetidos, mas é uma opção aceita.

### Acessandos dados

- Por conta de conjuntos não garantirem a ordem dos elementos dentro dele, OS SETS NÃO SUPORTAM INDEXAÇÃO DOS ELEMENTOS E NEM FATIAMENTO.
- Para acessar os valores de um conjunto, é necessário convertê-lo para uma lista.

```python
naturais = {1, 2, 3, 4}
print(naturais[3]) # Antes de tranformá-lo em lista
>>> TypeError: 'set' object is not subscriptable
# Um objeto 'set' não é indexável

naturais = list(naturais)
print(naturais[2])
>>> 3
```

### Iterar conjuntos

- Mesma sintaxe e forma das outras estruturas.
- Se usa o método for.

```python
naturais = {1, 2, 3, 4, 6, 8, 1}

for natural in naturais: 
	print(natural)
```

### Função enumerate

- Mesma sintaxe e forma das outras estruturas.
- O índice indicado nos elementos NÃO é fixo para eles. Não é possível acessar o elemento X pelo índice numerado pela função.

```python
naturais = {1, 2, 3, 4}

for indice, natural in enumerate(naturais):
	print(f"{indice}: {natural}")
```

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  12 de janeiro de 2026

### Tópico: Métodos da classe set

### Lembretes

### Anotações

- Os métodos da classe set são, em sua maioria, ligados a conjuntos matemáticos.

### {}.union()

- Utilizado para unir dois conjuntos existentes.
- Cria um novo conjunto da união dos dois, sem modificar os originais (não é in place).

*conjunto1*.union(*conjunto2*)

conjunto1: primeiro conjunto que vai ser unido:
conjunto2: segundo conjunto que vai ser unido.

```python
a = {1,2,3}
b = {4,5,6}

c = a.union(b)
print(c)
>>> {1, 2, 3, 4, 5, 6} # -> não garante a ordem dos      elementos
```

### {}.intersection()

- Retorna os elementos iguais de dois conjuntos.
- Retorna um novo conjunto dos elementos da intersecção. Não modificam os originais.

*conjunto1.*intersection(*conjunto2*)

conjunto e conjunto2: conjuntos existentes de onde a intersecção vai ser feita.

```python
a = {1, 2, 3}
b = {2, 3, 4}

inter = a.intersection(b)
print(inter)
>>> {2, 3}
```

### {}.difference()

- Retorna a diferença dos dois conjuntos. Tudo o que existe dentro do primeiro, que não existe dentro do segundo.
- Aqui, a ordem dos conjuntos (conjunto1 e conjunto2) faz diferença.  O método difference() é  **não comutativo.**
- Retorna um novo conjunto com os elementos distintos dos dois. Não modifica os originais.

*conjunto1.*difference(*conjunto2*)

conjunto1: conjunto de onde vai ser subtraído os elementos iguais. É a base da subtração.
conjunto2: conjunto que vai subtrair os elementos iguais. Todos os elementos que existem aqui vão ser subtraídos do primeiro.

“Tudo o que está em 1 que não está em 2.”

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b)) # O único elemento de 'a', que    não existe em 'b' é 1 
>>> {1}

print(b.difference(a)) # O único elemento de 'b', que    não existe em 'a' é 4
>>> {4}
```

### {}.symmetric_difference()

- Retorna a diferença simétrica entre os conjuntos. Ou seja, tudo o que não é igual nos dois.
- Retorna elementos que estão em um OU outro, mas não em ambos.
- Contrário da intersecção, e união das diferenças.
- Cria um novo conjunto com os elementos, sem modificar os originais.

*conjunto1*.symmetric_difference(*conjunto2*)

conjunto e conjunto2: conjuntos existentes de onde a diferença vai ser feita.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.symmetric_difference(b))
>>> {1, 4} # União das duas diferenças
```

### {}.issubset()

- Verifica se um conjunto A é um subconjunto de B. Ou seja, se todos os elementos de A estão presentes em B.
- Retorna um booleano.
- É um método **não comutativo**. Ou seja, a ordem dos conjuntos importa.

*conjunto1*.issubstet(*conjunto2*)

conjunto1: Conjunto que vai ser verificado como subconjunto. Os elemento vão ser verificados. 
conjunto2:  Conjunto de onde sai (ou não) o subconjunto. De onde a comparação vai ser feita.
”Conjunto1 é um subconjunto de Conjunto2?”
”Todos os elementos de Conjunto2 estão em Conjunto1?”

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}

print(a.issubset(b)) 
>>> True

print(b.issubset(a))
>>> False

```

### {}.issuperset()

- O contrário do subconjunto. Verifica um conjunto A é o superconjunto de B.
- Ou seja, se todos os elementos de B existem em A.
- Retorna um booleano.
- É um método **não comutativo.** A ordem dos conjuntos importa.

*conjunto1.*issuperset(*conjunto2*)
conjunto1:  Conjunto de onde sai (ou não) o subconjunto. De onde a comparação vai ser feita.
conjunto2: Conjunto que vai ser verificado como subconjunto. Os elemento vão ser verificados. 

“Todos os elementos de Conjunto1 estão dentro de Conjunto2?”
”Conjunto2 é um subconjunto de Conjunto1? Conjunto1 é o superconjunto de Conjunto2?”

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}

print(a.issuperset(b)) # Os elementos de B não existem emA
>>> False

print(b.issubset(a)) # Os elementos de A existem todos   em B
>>> True

```

### {}.isdisjoint()

- Verifica se os dois conjuntos são totalmente distintos um do outro. Se não possuem elementos em comum.
- Retorna um booleano.
- É um método comutativo. ‘A ordem dos fatores não altera o produto’.

*conjunto1*.isdisjoint(*conjunto2*)

conjunto e conjunto2: conjuntos existentes de onde a verificação da distinção vai ser feita.

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}
c = {0, -1}

print(a.isdisjoint(b))
>>> False # Possuem elementos em comum, não são distintos

print(a.isdisjoint(c))
>>> True # Não possuem elementos em comum, são distintos
```

### {}.add()

- Adiciona qualquer elemento dentro do conjunto, não necessariamente no final.

*conjunto*.add(*objeto*)

conjunto: conjunto onde o elemento vai ser adicionado.
objeto: objeto a ser adicionado no conjunto. Se o elemento já existir no conjunto, o objeto não é adicionado novamente (mas não retorna um erro nem nada).

### {}.clear()

- Limpa todos os elementos do conjunto.
- Modifica o conjunto original.

*conjunto*.clear()

conjunto: conjunto que vai ter os elementos apagados.

### {}.copy()

- Cria uma cópia do conjunto.
- Todas as mudanças feitas na cópia não são realizadas no conjunto original.

*copia_conjunto = conjunto.*copy()

copia_conjunto = novo conjunto onde vai ser armazenada a cópia.
conjunto:  conjunto que vai ser copiado.

### {}.discard()

- Remove um elemento idêntico ao indicado do conjunto.
- Diferentemente do remove() (também utilizado nos conjuntos), se o objeto indicado não for encontrado dentro do conjunto não retorna um erro (ValueError).
- Como os elementos não se repetem, não existe a situação de excluir apenas a primeira ocorrência do elemento indicado, como em outras estruturas de dados.
- Apenas para sets e frozensets

*conjunto.*discard(*objeto*)

conjunto: conjunto de onde o objeto vai ser removido.
objeto: objeto a ser removido do conjunto.

```python
a = {1,2,3,4,5,6}

a.discard(3)
a.discard(10)
print(a)
>>> {1, 2, 4, 5, 6} # Remove o 3 e não da erro pelo 10   não existir no conjunto
```

### {}.pop()

- Remove o elemento da frente do conjunto, ao invés do último como em outras estruturas.
- A remoção de um elemento é considerada aleatória, mesmo que o pop remova os primeiros elementos do conjunto, por que o conjunto não garante a ordem dos elementos.
- Remove e retorna o elemento removido.

*conjunto*.pop()

conjunto: conjunto de onde o elemento vai ser removido.

```python
a = {1, 2, 4, 5, 6}

print(a.pop())
>>> 1 
print(a.pop())
>>> 2

print(a)
>>> {3, 4, 5, 6}
```

 

### {}.remove()

- Remove o elemento do conjunto idêntico ao indicado.
- Se o elemento não existir dentro do conjunto, o remove() retorna um erro (ValueError).

*conjunto.*remove(*objeto*)

conjunto: conjunto de onde o elemento vai ser removido.
objeto: objeto que vai ser removido do conjunto (se não existir, a função retorna um erro).

### len()

- Retorna o tamanho (quantidade de elementos) do conjunto.
- Apenas dos elementos não repetidos (ignora os que se repetem).

len(*objeto*)

objeto: iterável, sequência ou coleção.

```python
a = {1, 2, 4, 5, 6, 1, 8, 7, 5, 2, 4, 9} # 12

print(len(a))
>>> 8
```

### in

- Verifica se um objeto está dentro de um conjunto.
- O objeto precisa ser idêntico (case sensitive e tipo do objeto).
- Retorna um booleano

*objeto* in *conjunto*

objeto: objeto a ser procurado no conjunto.
conjunto: conjunto onde o objeto vai ser procurado.

```python
naturais = {1, 2, 4, 5, 6, 7, 8, 9}

print(1 in naturais)
>>> True

print(10 in naturais)
>>> False
```

<aside>
📌 **RESUMO:**

</aside>