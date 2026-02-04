# Introdução a Ciência de Dados e Python

Data: 11 de dezembro de 2025
Categoria: ciência de dados, python
Criado por: gabriela

[Tipos de operadores com Python](Introdu%C3%A7%C3%A3o%20a%20Ci%C3%AAncia%20de%20Dados%20e%20Python/Tipos%20de%20operadores%20com%20Python%202ce0c7a5edfe80f6966dcfbf2fc5c6a8.md)

[Estruturas Condicionais e de Repetição](Introdu%C3%A7%C3%A3o%20a%20Ci%C3%AAncia%20de%20Dados%20e%20Python/Estruturas%20Condicionais%20e%20de%20Repeti%C3%A7%C3%A3o%202ce0c7a5edfe80748935f9a9790202fb.md)

[Strings e fatiamento](Introdu%C3%A7%C3%A3o%20a%20Ci%C3%AAncia%20de%20Dados%20e%20Python/Strings%20e%20fatiamento%202e10c7a5edfe80e5a19ff3a640b308da.md)

[Listas](Introdu%C3%A7%C3%A3o%20a%20Ci%C3%AAncia%20de%20Dados%20e%20Python/Listas%202e10c7a5edfe80f0893bc7da2e33377f.md)

[Tuplas](Introdu%C3%A7%C3%A3o%20a%20Ci%C3%AAncia%20de%20Dados%20e%20Python/Tuplas%202e30c7a5edfe8064acd6c193fe66cd53.md)

[Conjuntos](Introdu%C3%A7%C3%A3o%20a%20Ci%C3%AAncia%20de%20Dados%20e%20Python/Conjuntos%202e30c7a5edfe8024aa01f73673cf2fff.md)

[Dicionários](Introdu%C3%A7%C3%A3o%20a%20Ci%C3%AAncia%20de%20Dados%20e%20Python/Dicion%C3%A1rios%202e60c7a5edfe80599c0dfd5d407ccaaf.md)

Anotações

### Data:  19 de dezembro de 2025

### Tópico: Funções

### Lembretes

### Anotações

- Funções são blocos de código identificados por um nome, que recebem uma lista de parâmetros (valores que serão recebidos, ou valores padrão) e que podem retornar um valor ou objeto.

Parâmetros:  valores de entrada.
Retorno:  valores de saída.
- Funções são amplamente utilizadas para reaproveitamento de código, e maior legibilidade.
- Programação estruturada.

```python
# Criar a função
def exibir_mensagem(): # Função sem parâmetros
    print("Hello World!")

    # Funções com parâmetros
def boas_vindas(nome): # Parâmtro sem valor padrão
    print(f"Seja bem-vindo {nome}!")

def boas_vindas2(nome = "Anônimo"):
    print(f"Seja bem-vindo {nome}")

exibir_mensagem()
>>> Hello World!

boas_vindas()
>>> TypeError: boas_vindas() missing 1 required positional argument: 'nome'
# A função retorna um erro se o parâmetro não tiver um valor padrão e não for indicado
 
boas_vindas(nome = 'gabi')
>>> Seja bem-vindo gabi!

boas_vindas2()
>>> Seja bem-vindo Anônimo
# Como a função possui um valor padrão, se ela não receber um argumento não é retornado um erro

boas_vindas('isa')
>>> Seja bem-vindo isa!
```

### Como criar funções

- Funções são criadas utilizando a palavra reservada *def.*
- Funções (por padrão) possuem um identificador (nome), parâmetros (valores de entrada) e um retorno (valores de saída).

def *nome_funcao*(*parametro = valor, parametro2 = valor*)

*bloco de código*

return *retorno*

def: palavra reservada para criar uma função.
nome_função:  o nome que vai identificar a função. É por esse nome que a função vai ser chamada quando for preciso utilizá-la no código.
parametro e parametro2: são os objetos que serão utilizados dentro da função. Quando têm seus valores definidos dentro da função são chamados de argumentos.
retorno: qualquer objeto que será retornado ao fim da execução da função.

### Retornando valores

- É possível que as funções em Python retornem mais de um valor, apenas um valor, ou o valor padrão *None.*
- Para retornar um valor em uma função é utilizada a palavra reservada *return.*

```python
def calcular_total(numeros): 
	return sum(numeros) # Retorna apenas um valor
	
def retorna_antecessor_sucessor(numero): 
	antecessor = numero - 1
	sucessor = numero + 1
	
	return antecessor, sucessor
	

calcular_total([10, 20, 30, 40])
>>> 100

retorna_antecessor_sucessor(10)
>>> (9, 11)

# Retorno padrão
def func_3():
    print("Olá!")
    # return None

func_3() # "Olá!" -> não retorna nada, pois é o valor padrão
print(func_3()) # "Olá!" e None -> imprime o valor padrão de retorno
```

### Argumentos nomeados

- Funções também podem receber valores no padrão ‘chave=valor’;

```python

def salvar_carro(marca, modelo, ano, placa): 
    # Salva um carro no banco de dados
    print(f"Carro salvo no inventário! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("fiat", "palio", 2011, "nnao-5311")        # Argumentos posicionados 

salvar_carro(marca="fiat", modelo="palio", ano=2011,     placa="nnao-5311") # Argumentos nomeados

salvar_carro(**{"marca":"fiat", "modelo":"palio",       "ano": 2011, "placa":"nnao-5311"}) # Por dicionários
```

- Argumentos posicionados:  são passados apenas os valores que ocuparão o parâmetro, sem indicar qual será. DEVE seguir a ordem de aparição dos parâmetros na função. 
Pede atenção para a ordem dos argumentos, se forem passados em ordem diferente da apresentada, os valores serão armazenados dessa forma.
- Argumentos nomeados: são passados pelo padrão chave=valor, garantindo que os argumentos passados sejam recebidos pelo parâmetro que estiver relacionado.
- Por dicionários: o ** indica que os argumentos estão sendo passados pelo dicionário indicado.

### Args e kwargs

<aside>
📌 **RESUMO:**

</aside>