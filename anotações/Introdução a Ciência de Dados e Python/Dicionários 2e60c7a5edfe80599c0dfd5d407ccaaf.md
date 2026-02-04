# Dicionários

Anotações

### Data:  12 de janeiro de 2026

### Tópico: Dicionários

### Lembretes

### Anotações

- Um dicionário é um conjunto não ordenado de pares ‘chave: valor’.
- As chaves são valores únicos e imutáveis (não se repetem e não podem ser alteradas uma vez depois de instanciadas/tuplas ou strings).
- Os valores relacionados às chaves podem ser de qualquer tipo.
- São delimitados por chaves, com os pares ‘chave: valor’ separados por vírgulas.

```python
dicionário = {'chave1': 'valor1', 'chave2': 'valor2'} 
```

- Uma chave só pode ter um único valor associado diretamente a ela. Mas é possível usar listas para guardar mais de um valor em uma chave (de forma indireta), porque conta como apenas um objeto do tipo list.

Criação: 

```python
# Entre chaves

pessoa = {"nome": "Gabriela", "idade":18}

# Método dict
pessoa = dict(nome = "Gabriela", idade = 18) # Chave sem aspas, mesmo se for string simples

# Para adicionar uma nova chave
pessoa["telefone"] = 40028922

print(pessoa)
>>> {'nome': 'Gabriela', 'idade': 18, 'telefone': 40028922}
```

### Acesso aos dados

- Assim como em outras estruturas, onde para o acesso direto dos dados era utilizado o índice, a lógica segue a mesma.
- Utiliza-se a chave do objeto para acessá-lo.
- O acesso funciona dessa forma por conta que a chave é única e elas possuem apenas um objeto associado a ela.

```python
dados = {'nome': 'Gabriela', 'idade': 18, 'telefone': 40028922}

print(dados["nome"])
>>> Gabriela

print(dados["idade"], dados["idade"])
>>> 18 40028922
```

- Se houver um sinal de igual ao lado do acesso das chaves que já existem, o valor delas é sobrescrito.

```python
dados["nome"] = Maria
dados["idade"] = 21

print(dados)
>>> {'nome': 'Maria', 'idade': 21, 'telefone': 40028922}
```

### Dicionários aninhados

- Como os valores dos dicionários podem ser de qualquer tipo, um dicionário pode conter outro dicionário como um de seus valores, desde que a chave associada a ela seja um objeto imutável.
- Estruturas desse tipo são chamados de dicionários aninhados.
- Possuem uma estrutura semelhante a um banco de dados.

```python
contatos = {
	"Gabriela": {"email": "gabibrumf@yahoo.com", "telefone": 40028922},
	"João": {"email": "joao@gmail.com", "telefone": 40028922} 
	}

# Acesso
print(contatos["Gabriela"])
>>> {"email": "gabibrumf@yahoo.com", "telefone": 40028922}

print(contatos["Gabriela"]["telefone"])
>>> 40028922
```

### Iterar dicionários

- Também se utiliza o método for para iteração dos dicionários.
- Possui pequenas mudanças na apresentação dos dados.

```python
for chave in contatos: 
	print(chave, contatos[chave])

for chave, valor in contatos.items():
	print(chave, valor)
	
>>> Gabriela {'email': 'gabibrumf@yahoo.com', 'telefone': 40028922}
>>> João {'email': 'joao@gmail.com', 'telefone': 40028922}
```

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  12 de janeiro de 2026

### Tópico: Métodos da classe dict

### Lembretes

### Anotações

### {:}.clear()

- Apaga todos os valores e chaves do dicionário.

### {:}.copy()

- Cria uma cópia do dicionário, que é armazenada em outro objeto.
- É possível fazer alterações na cópia, sem que o original seja alterado.

```python
contatos = {"Gabriela": {"email": "gabi@gmail.com", "telefone": 40028922}
}

copia = contatos.copy()

copia["Gabriela"]= {"email": "gabib@gmail.com"}

print(contatos["Gabriela"]["email"])
>>> gabi@gmail.com

print(copia["Gabriela"]["email"])
>>> gabib@gmail.com
```

### {:}.fromkeys()

- Cria um novo dicionário a partir de uma sequência de chaves, atribuindo o mesmo valor para todas elas.
- As chaves podem ser criadas sem valor associado a elas, ou com um valor já atribuído.

*dicionário =* dict*.*fromkeys(*iterável, valor*)

dicionário: dicionário (novo) onde as chaves vão ser adicionadas.
iterável: objeto iterável (sequência, cadeia ou coleção) que serão as chaves do dicionário.
valor: valor que será atribuído a todas as chaves. Se não for indicado, o valor padrão é “None”.

```python
# Sem valor
contatos = dict.fromkeys(["nome", "telefone"])
print(contatos)
>>> {"nome": None, "telefone": None}

# Com valor
contatos = dict.fromkeys(["nome", "telefone"], "vazio")
print(contatos)
>>> {"nome": "vazio", "telefone": "vazio"} # Todas as    chaves recebem o mesmo valor
```

- OBS: Se o dicionário atribuído ao fromkeys() já existir, o conteúdo dele vai ser reescrito com as novas informações. Não é possível atualizar dicionários (adicionar mais chaves ou valores) utilizando esse método.

```python
**dicionario = dict.fromkeys(["a", "b"], "vazio")
print(dicionario)
>>> {"a": "vazio", "b": "vazio"}

dicionario = dicionario.fromkeys(["c", "d"], "vazio")
print(dicionario)
>>> {"c": "vazio", "d": "vazio"}**
```

### {:}.get()

- Retorna um valor de alguma chave contida no dicionário.
- Funciona da mesma forma do fatiamento (dicionario[chave]). Porém, se a chave não existir no dicionário, não retorna um erro (KeyError).
- Retorna o valor relacionado a chave, e se não existir retorna uma mensagem indicada no método.

*dicionario.*get(*chave, mensagem*)

dicionario: dicionário onde a chave vai ser buscada.
chave: chave a ser procurada no dicionário. Se não existir, não retorna um erro.
mensagem (opcional): mensagem a ser retornada se a chave não for encontrada no dicionário. Por padrão, a mensagem é “None”.

```python
contatos = {
	"Gabriela": {"email": "gabi@gmail.com", "telefone": 40028922}
}

print(contatos["nome"]) #Fatiamento
>>> KeyError # Retorna um erro, e o programa para

print(contatos.get("nome"))
>>> None # Chave não existe no dicionário
fulano = contatos.get("João", "Não existe")
print(fulano)
>>> Não existe

ciclano = contatos
```

### {:}.items()

- Retorna uma lista de tuplas contendo todos os elementos pares-chave presentes no dicionário.
- Retorna um objeto do tipo ‘dict_items’.
- Muito utilizado para iterar o dicionário utilizando o for.

*dicionario*.items()

```python
dicionarioA = {"a": "valorA", "b": "valorB", "c": "valorC"}

print(dicionarioA.items())
>>> dict_items[("a", "valorA"), ("b", "valorB"), ("c", "valorC")]
```

### {:}.keys()

- Retorna uma lista apenas das chaves do dicionário.
- Retorna um objeto do tipo ‘dict_keys’.

```python
dicionarioA = {"a": "valorA", "b": "valorB", "c": "valorC"}

chaves = dicionarioA.keys()
print(chaves)
>>> dict_keys(["a", "b", "c"])
```

### {:}.pop()

- Remove uma chave, e os valores atríbuidos a ela do dicionário, se for idêntica a indicada.
- Além de remover o par chave-valor, ele retorna o valor que foi removido.
- Pode retornar um erro (KeyError) se a chave não for encontrada. Mas esse comportamento pode ser alterado no próprio método.

*dicionario*.pop(*chave, mensagem*)

dicionario: coleção onde a chave indicada vai ser apagada.
chave: chave a ser buscada no dicionário para ser apagada.
mensagem (opcional, mas pode retornar erro): Objeto retornado se a chave não for encontrada no dicionário. Se o objeto ‘mensagem’ não for indicado, o método retorna um erro (KeyError) e o programa para se a chave não for encontrada.

```python
contatos = {
	"Gabriela": {"email": "gabibrumf@yahoo.com", "telefone": 40028922},
	"João": {"email": "joao@gmail.com", "telefone": 40028922},
	"Isabela": {"email": "isabela@gmail.com", "telefone": 40028922}, 
}

contatos.pop("Lara")
>>> KeyError: 'Lara' # Retorna um erro porque a chave não existe, e nenhuma mensagem foi indicada

contatos.pop("Lara", "Não existe")
>>> Não existe # Retorna a mensagem indicada porque a chave não existe

contatos.pop("Isabela", "Não existe")
>>> {'email': 'isabela@gmail.com', 'telefone': 40028922} # Retorna os valores apagados (relacionados a chave indicada)

print(contatos)
>>> {'Gabriela': {'email': 'gabibrumf@yahoo.com', 'telefone': 40028922}, 'João': {'email': 'joao@gmail.com', 'telefone': 40028922}}
```

### {:}.popitem()

- Apaga os itens (par chave-valor) do dicionário na ordem da pilha (LIFO - Last-In, First-Out, O último a ser adicionado é o primeiro a ser apagado).
- Se não existirem mais chaves no dicionário,e o popitem() for chamado, ele retorna um erro (KeyError).
- Se uma chave  for apagada do dicionário, o seu valor é retornado.

*dicionario*.popitem()

```python
contatos = {
	'Gabriela': {'email': 'gabibrumf@yahoo.com', 'telefone': 40028922}, 
	'João': {'email': 'joao@gmail.com', 'telefone': 40028922}
}
	
contatos.popitem()
>>> {"email": "joao@gmail.com", "telefone": 40028922} # Item apagado

contatos.popitem()
>>> {'email': 'gabibrumf@yahoo.com', 'telefone': 40028922} # Item apagado

contatos.popitem()
>>> KeyError: 'popitem(): dictionary is empty'
```

### {:}.setdefault()

- Retorna o valor de uma chave indicada, e se ela não for encontrada a chave é adicionada ao dicionário com um valor indicado.
- Se a chave existir no dicionário, e o valor for indicado, o valor não é atualizado.

*dicionario*.setdefault(*chave, valor*)

dicionario: dicionário onde a chave vai ser buscada/adicionada.
chave: chave a ser buscada. Se não for encontrada ela é adicionada ao dicionário.
valor(opcional): se a chave não for encontrada no dicionário, o método adiciona a chave e relaciona o valor indicado a ela. O valor padrão é None.

```python
usuario = {"nome": "Gabi", "email": "gabi@gmail.com"}

usuario.setdefault("nome", "Isa")
>>> {"nome": "Gabi", "email": "gabi@gmail.com"}# A chave foi encontrada, o valor retornado

usuario.setdefault("telefone", {})
>>> {} # A chave não foi encontrada, foi adicionada com o valor {} relacionado a ela

usuario.setdefault("CPF") # Valor None é adicionado

print(usuario)
>>> {"nome": "Gabi", "email": "gabi@gmail.com",         "telefone": {}, "CPF": None}
```

### {:}.update()

- Serve para atualizar os valores do dicionário.
- Se a chave for encontrada o valor dela é atualizado. Se não existir no dicionário, a chave e o valor são adicionados.

*dicionario*.update({*chave: valor}*)

dicionario: dicionário que vai ser atualizado.
chave: chave relacionada ao valor que vai ser atualizado.
valor: novo valor que a chave vai assumir.

```python
usuario = {"nome": "Gabi", "email": "gabi@gmail.com",  
	"telefone": {}, "CPF": None}
	
usuario.update({"nome": "Gabriela"}) # Atualiza o valor  da chave já existente
usuario.update({"admin": True}) # Adiciona o par ao      dicionário (chave não existia)

print(usuario)
>>> {'nome': 'Gabriela', 'email': 'gabi@gmail.com', 'telefone': {}, 'CPF': None, 'admin': True}
```

### {:}.values()

- Como na função keys(), retorna uma lista de valores do dicionário.
- Retorna um objeto do tipo ‘dict_values’.

*dicionario*.values()

dicionario: dicionário de onde os valores vão ser retirados.

```python
usuario = {'nome': 'Gabriela', 'email': 'gabi@gmail.com', 'telefone': {}, 'CPF': None, 'admin': True}

print(usuario.values())
>>> dict_values(['Gabriela', 'gabi@gmail.com', {}, None, True])
```

### in

- Utilizado para verificar se uma chave existe dentro de um dicionário.
- Retorna um booleano.

*chave* in *dicionario*

```python
contatos = {
	'Gabriela': {'email': 'gabibrumf@yahoo.com', 'telefone': 40028922}, 
	'João': {'email': 'joao@gmail.com', 'telefone': 40028922}
}

'Gabriela' in contatos # True
'Isabela' in contatos # False
'joão' in contatos # False

'email' in contatos['Gabriela'] # True
'idade' in contatos['Gabriela'] # False
```

### del

- Remove chaves (e o valor relacionado a ela) do dicionário.
- Pode remover chaves de dicionários que são valores de outra chave (dicionários aninhados).
- Retorna um erro (KeyError) se a chave não existir no dicionário.

del *dicionario*[*chave]*

```python
contatos = {
	'Gabriela': {'email': 'gabibrumf@yahoo.com', 'telefone': 40028922}, 
	'João': {'email': 'joao@gmail.com', 'telefone': 40028922}
}

del contatos['Gabriela']
del contatos['João']['telefone']

print(contatos)
>>> {'João': {'email': 'joao@gmail.com'}}
```

<aside>
📌 **RESUMO:**

</aside>