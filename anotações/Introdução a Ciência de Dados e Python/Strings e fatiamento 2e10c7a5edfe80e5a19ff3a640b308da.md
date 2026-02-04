# Strings e fatiamento

Anotações

### Data:  7 de janeiro de 2026

### Tópico: Métodos úteis da classe string

### Lembretes

**Métodos úteis**

### Anotações

### Maiúscula, minúscula e título

```python
curso = "python"

print(curso.upper()) # Transforma todas as letras em MAIÚSCULAS
>>> PYTHON

print(curso.lower()) # Transforma todas as letras em minúsculas
>>> python

print(curso.title()) # Transforma na formatação de Título (apenas a primeira maiúscula)
>>> Python
```

### Eliminando espaços em branco

```python
curso = "    Python "

print(curso.strip()) # Elimina todos os espaços em branco de ambos os lados da string
>>> "Python"

print(curso.lstrip()) # Elimina apenas os espaços brancos a ESQUERDA da string (left strip)
>>> "Python "

print(curso.rstrip()) # Elimina apenas os espaços brancos a DIREITA da string (rigth strip)
>>> "    Python" 
```

### Junção e centralização

```python
curso = "PYTHON"

print(curso.center(10, "a")) # A função centraliza a sua string de acordo com o tamanho dado na função
>>> "aaPYTHONaa"

print(" ".join(curso)) # Adiciona o caractere desejado entre as letras da string indicada
>>> "P Y T H O N"
```

<aside>
🎯

### Função .center()

Sintaxe:

string.center(largura, preenchimento)
- largura (obrigatório): indica o tamanho total desejado para a nova string. (largura = string + preenchimento)
- preenchimento (opcional): deve ser preenchido com o caractere que será preenchido nos novos espaços adicionados. Se não for indicado, apenas o espaço em branco “ “ é adicionado.

### Função .join()

A função .join() é muito utilizada para juntar elementos (concatenar) de uma lista e transformá-los em uma única string, utilizando um separador definido.

Sintaxe: 

separador.join(string)

- seprarador (obrigatório): caractere indicado para ser o separador dos objetos da lista na string. Sempre deve ser indicado.
- string (obrigatório): lista, tupla, string, ou qualquer objeto que será transformado na string.
Os objetos da sequência DEVEM ser do tipo string.
</aside>

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  7 de janeiro de 2026

### Tópico: Interpolação de variáveis

### Lembretes

### Anotações

- a

### %

- O uso não é recomendado.
- Parecido com o uso da linguagem C.

```python
nome = "Guilherme"
idade = 20
profissao = "Professor"
disciplina = "Matemática"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s."
	, %(nome, idade, profissao, disciplina))
```

### Método format

```python
nome = "Guilherme"
idade = 20
profissao = "Professor"
disciplina = "Matemática"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}."
.format(nome, idade, profissao, disciplina))
# Utiliza o mesmo formato do anterior, porém as variáveis
# são indicadas por chaves, e mantém o princípio da ordem

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {0} e estou matriculado no curso de {1}."
.format(profissao, idade, disciplina, nome))
# Também podem ser indicados os índices das variáveis no format,
# começando em 0.

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {curso}."
.format(nome=nome, idade=idade, profissao=profissao, curso = disciplina))
# Podem ser colocados nomes distintos no texto, e indicar
# quais são as variáveis correspondentes no format. Não utiliza ordem.

pessoa = {'nome' = "Guilherme", 'idade' = 20, 'profissao' = "Professor", 'disciplina' = "Matemática"}
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {disciplina}."
.format(**pessoa))
# Todas as variáveis indicadas são chaves do dicionário 'pessoa',
# por isso, é possível indicar apenas as chaves e o nome do dicionário.
```

### f-string

- Semelhante ao format

```python
nome = "Guilherme"
idade = 20
profissao = "Professor"
disciplina = "Matemática"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {disciplina}.")

PI = 3.14159 # Constante
print(f"Valor de PI: {PI}")
>>> Valor de PI: 3.14159

print(f"Valor de PI: {PI:.2f}") # Número de casas decimais após a vírgula
>>> Valor de PI: 3.14

print(f"Valor de PI: {PI:10.2f}") # Número de espaços antes da variável: casas decimais após a vírgula
>>> Valor de PI:           3.14
```

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  7 de janeiro de 2026

### Tópico: Fatiamento de strings

### Lembretes

### Anotações

- Método utilizado para retornar partes da string original (substring), informando start, stop e step.
[start : stop[ , step]]
- Nenhum dos parâmetros é obrigatório.
O ‘stop’ é exclusive, ou seja, não aparece na contagem de índices (stop-1).

```python
nome_completo = "Ana da Silva Carvalho"

print(nome_completo[0]) # [start]
>>> "A"

print(nome_completo[2:5]) #[start : stop(exclusive)]
>>> "a da "

print(nome_completo[:9]) #[ : stop(exclusive)]
>>> "Ana da Si"

print(nome_completo[7:]) # [start: ] (até o fim da string)
>>> "Silva Carvalho"

print(nome_completo[7:12:2]) # [start : stop(exclusive): step]
>>> "Sva"

print(nome_completo[::-1]) # [:: step]
>>> "ohlavraC avliS ad anA" # Cria uma cópia da string ao contrário
```

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  7 de janeiro de 2026

### Tópico: String de múltiplas linhas/strings triplas

### Lembretes

### Anotações

- São definidas por 3 aspas simples ou duplas na atribuição da mesma.
- Mantém todos os espaços e recuos.

```python
nome = "Gabi"

mensagem = f"""
	Olá, me chamo {nome}!
"""
```

<aside>
📌 **RESUMO:**

</aside>