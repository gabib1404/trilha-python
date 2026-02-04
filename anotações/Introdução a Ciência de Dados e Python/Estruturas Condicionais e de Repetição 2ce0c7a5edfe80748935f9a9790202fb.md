# Estruturas Condicionais e de Repetição

Anotações

### Data:  19 de dezembro de 2025

### Tópico: Indentação e blocos

### Lembretes

### Anotações

- Através da indentação, o interpretador delimita os blocos de comando do código.
- *Indentação:  recuo da linha para a direita*
- Em outras linguagens, blocos de comando são definidos por palavras reservadas ou chaves.

Java: 

```java
void sacar(double valor) { // Início do bloco do método 'sacar'
	if(this.saldo >= valor)  { // Início do bloco do if
		this.saldo -= valor;
	} // Fim do bloco do if
} // Fim do bloco do método
```

- Apesar do código usar a indentação, o que define o escopo do bloco de comando em Java são as chaves. Se um código for escrito inteiramente sem indentação, ele funciona do mesmo jeito.

```java
void sacar(double valor) { // Início do bloco do método
if(this.saldo >= valor) { // Início do bloco do if
this.saldo -= valor;
} // Fim do bloco do if/
} // Fim do bloco do método
```

Python:

```python
def sacar(self, valor:float) -> None: # Início do bloco do método
	if self.saldo >= valor: # Início do bloco do if
		self.saldo -= valor
	# Fim do bloco do if
# Fim do bloco do método
```

- O interpretador Python reconhece como um bloco de código apenas as linhas que estão a 4 espaços em branco para a direita da linha inicial.

<aside>
🎯

Dicas: 

```python
def sacar (self, valor:float) -> None: 
```

self: representa a própria instância do objeto, e permite o acesso a outras variáveis do objeto.
Em métodos de instância (), o *self*  é sempre o primeiro parâmetro, e é obrigatório.
Funciona como o *this* do Java (ambos representam o objeto instanciado atual)

→ None: a seta → é utilizada para *type hints* (anotações de tipo) e server para indicar qual é o tipo de retorno da função.
Não é obrigatório, mas ajuda na leitura e entendimento do código.

</aside>

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  6 de janeiro de 2026

### Tópico: Estruturas Condicionais

### Lembretes

Estrutura simples

Estrutura aninhada

Estrutura ternária

### Anotações

- Permitem o desvio de controle de fluxo **se** uma lógica for atendida.

### IF (Estrutura simples)

- Estrutura condicional simples.

```python
saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
	print("Saque realizado")

if saldo < saque: 
	print("Saldo insuficiente")
```

- Para todo o if que estiver presente no código, a condição é verificada.

### IF/ELSE

- Estrutura condicional com dois desvios.
- Palavras reservadas: *if*  e *else.*

```python
saldo = 1000.00
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
	print("Saque realizado")
else: 
	print("Saldo insuficiente")
```

- Como a estrutura possui dois desvios - um atrelado ao outro -, se a primeira condição (if) for verdadeira a segunda não é executada (a condição não é verificada), se o if for falso, o else é executado.
- Se não entra no primeiro fluxo, o segundo é executado. E se o primeiro fluxo for verdadeiro, o segundo não é executado.

### If/ elif/ else

- Estrutura condicional com mais desvios.
- Utilizado para vários condições.

```python
opcao =  int(input("Informe uma opção:\n {1} Sacar\n {2} Verificar saldo")
)

if opcao == 1:
	saque = float(input("Informe o valor do saque: "))

	if saldo >= saque:
		print("Saque realizado")
	else: 
		print("Saldo insuficiente")

elif opcao == 2:
	# Exibe o extrato

else: 
	sys.exit("Opção inválida")
```

- else if = elif

<aside>
💡

- Estrutura

SE condição:

bloco de código;

SE NÃO, SE condição: 

bloco de código;

SE NÃO condição: 

bloco de código;

</aside>

### If aninhado

- É possível colocar condições dentro de blocos de código de outras condições
- Chamado de **Estrutura de repetição aninhada.**

```python
if conta_normal: 
	if saldo >= saque:
		print("Saldo realizado com sucesso")
	elif saque <= (saldo + cheque_especial):
		print("Saldo realizado com o uso do cheque especial")

elif conta_universitaria: 
	if saldo >= saque: 
		print("Saque realizado com sucesso")
	else: 
		print("Saldo insuficiente")
```

- A lógica continua sendo a mesma.

<aside>
📖

SE conta_normal for True:

(entra no bloco de código identado)

SE saldo for MAIOR OU IGUAL A saque:

(entra no bloco identado)

(saque é realizado)

SE NÃO, SE saque for MENOR OU IGUAL A saldo + cheque especial: 

(entra no bloco identado)

(saque é realizado com o auxílio do cheque especial)

SE conta_normal for False E conta_universitaria for True:

(entra no bloco identado)

SE saldo for MAIOR OU IGUAL A saque: 

(entra no bloco identado)

(saque é realizado)

SE NÃO: 

(entra no bloco identado)

(saque não é realizado)

</aside>

### If ternário

- Estrutura condicional em apenas uma linha.
- Composto por três partes: 
retorno (caso seja verdadeira), expressão lógica e retorno (caso seja falsa)

```python
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")
```

- Se a condição do if for True, “Sucesso” é o retorno utilizado, se for falsa, o retorno do else - “Falha” - é o valor da variável.

<aside>
📌 **RESUMO:**

</aside>
		

Anotações

### Data:  6 de janeiro de 2026

### Tópico: Estruturas de repetição

### Lembretes

### Anotações

- Estruturas utilizadas para repetir um trecho de código um determinado número de vezes, podendo ser determinado através de uma expressão lógica.

- Exemplo sem estrutura de repetição

```python
# Receba um valor pelo teclado e exiba os 10 números seguintes

numero = int(input("Digite um número: "))

print(numero += 1)
print(numero += 1)
print(numero += 1)
print(numero += 1)
.
.
.
```

- As estruturas de repetição servem para facilitar e evitar o uso de trechos repetidos de código, que podem ser repetidos um número definido de vezes.

### Comando for (para)

- Utilizado para percorrer um objeto iterável (listas, tuplas, dicionários, conjuntos, etc).
- Utilizado quando se sabe o número exato de repetições ou em um objeto iterável (pelo número definido de objetos dentro dele).

```python
texto = input("Informe um texto: ")
VOGAIS = "aeiou" #VOGAIS - constante (por isso as letras maiúsculas)

for letra in texto: 
	if letra.upper() in VOGAIS:
		print(letra, end=" ") # Imprime as vogais da palavra em ordem de aparição e separadas por um espaço
print() # quebra de linha, igual um \n

>>> Informe um texto: pneumoultrasilicovulcanoconiotico
>>> e u o u a i i o u a o o i o i o 
```

### Comando for/else

- Serve para adicionar uma linha de código (geralmente um print) depois de um bloco for.
- Funcionamento: 
O bloco do *else* é executado APENAS se o loop foi concluído até o fim.
Caso tenha acontecido algum *break* no meio do loop, o bloco *else* é ignorado.

```python
for i in range(10):
	print(i)
else:
	print("Loop concluído")
	
>>> 0
>>> 1
>>> 2
.
.
.
>>> 9
>>> Loop concluído
```

- Não houve nenhum tipo de interrupção durante o laço de repetição, portanto, o bloco else foi executado.

```python
for i in range(10):
	if i == 7:
		print(i)
		print("Break")
		break
else: 
	print("Loop Concluído")
	
>>> 0
>>> 1 
...
>>> 7
>>> Break
```

- Como a condição do if foi verdadeira - a variável i assumiu o valor de 7 - o loop teve uma interrupção pelo break. Pelo loop não ter sido completo, o bloco else foi ignorado.

<aside>
🎯

**Exemplo mais prático**

```python
numeros = [8,9,6,2,4,8,6,2]
procurado = int(input("Digite o valor a ser procurado na lista: "))

for i in numeros:
	if i == procurado:
		print(f"O número {procurado} foi encontrado na lista!")
		break
else:
	print(f"O número {procurado} não está presente na lista")
```

O usuário digita um valor aleatório que queira buscar na lista.

A cada nova iteração, o laço de repetição (sempre que i passa a valer outro número da lista) verifica se este valor é igual ao valor digitado pelo usuário (if i == procurado).

Se a condição for verdadeira, o bloco de código do if é acessado e ocorre a interrupção do laço pelo break, e o bloco do else (relacionado ao for) não é executado.

Se a condição for falsa, o bloco do if é ignorado, não ocorre a interrupção do break, e o loop se extende até o final da condição. Assim, o bloco do else é executado.

! A interrupção de um loop não acontece apenas com um break, existem outros casos (return ou exceções/erros) que também quebram um loop antes dele ser finalizado.

</aside>

- O comando for/else é muito utilizado para verificar se uma busca dentro de um iterável foi bem sucedida ou não.

### Função range

- Função utilizada para produzir uma sequência de números inteiros que siga os parâmetros indicados.
- Argumentos da função *range*:
**stop (obrigatório):** é o valor que define o fim do intervalo. É o único argumento obrigatório da função. O valor do stop é exclusivo na função, ou seja, o último valor utilizado é o anterior ao indicado no stop.
**start (opcional):** valor de início do intervalo. Com qual valor ela se inicia. Se não for indicado, o valor padrão é 0.
**step (opcional):** define o passo do intervalo. Define o valor que será somado aos valores para montar o intervalo. Se não for indicado, o valor padrão é 1.

range(start, stop [, step]) → objeto range
- range(i,j)
[i, i+1, i+2, i+3, … , j-1] → como o intervalo funciona (star, stop)
- range(i, j, k)
[i+k, i+2k, i+3k, … ,j-1] → intervalo (start, stop, step)

```python
# Apenas valor obrigatório
# range(stop)

list(range(4))
>>> [0,1,2,3] 
""" Valor padrão de início: 0
		Valor do passo padrão: 1
		Valor de fim (indicado não incluso): 3
"""
```

### For com range

- Utilizados juntos quando existe um valor de loops definido.

```python
for i in range(1,10): # start, stop
	print(i, end=" ")

>>> 1 2 3 4 5 6 7 8 9

for i in range(0, 51, 5): #star, stop, step
	print(i, end = " ")

>>> 0 5 10 15 20 25 30 35 40 45 50
```

### Comando while (enquanto)

- Utilizado quando não se sabe o número exato de vezes que o bloco de código deve ser executado.

```python
opcao = -1

while opcao != 0:
	opcao = int(input("Digite a opção desejada: \n{1} opcao 1\n{2} opcao 2\n{3} opcao 3...{0} sair"))
	
	if opcao == 1:
		# bloco 1
	elif opcao == 2:
		# bloco 2
	elif opcao == 3: 
		# bloco 3

print("Bloco finalizado")
```

- O número de vezes que o código vai ser executado é desconhecido, depende da necessidade do usuário.
- O código vai ser executado ATÉ QUE o usuário digite a opção 0, saindo do loop automaticamente e imprimindo “Bloco finalizado”.

### Estrutura while/else.

- Funciona da mesma forma que o for/else.
- O bloco else é executado APENAS se não houver nenhuma interrupção durante o loop.
- Não é muito utilizado.

```python
opcao = -1

while opcao != 0:
	opcao = int(input("Digite a opção desejada: \n{1} opcao 1\n{2} opcao 2\n{3} opcao 3...{0} sair"))
	
	if opcao == 1:
		# bloco 1
	elif opcao == 2:
		# bloco 2
	elif opcao == 3: 
		# bloco 3
else: 
	print("Bloco finalizado")
```

- O bloco else é acessado apenas se o while for finalizado sem interrupções - a opção 0 não é uma interrupção, ela marca o fim do loop da estrutura.

### Comando break

- Utilizado para interromper um trecho de código de ser executado.
- Ele quebra a ordem de execução do código.

```python
for i in range(1,25)
	if i%2 == 0: # Verifica se o valor é par
		print(i, end = " ")
	elif i == 10:
		break
```

- O código acima cria um loop onde apenas os valores pares são impressos, e quando i assume o valor 10 o loop é interrompido e não volta a ser executado.

```python
while True: # Loop infinito
	numero = int(input("Informe um numero: ))
	
	if numero == 10:
		break
	
	print(numero)
```

- O código acima cria um loop infinito, e a cada nova iteração o usuário preenche a variável número com um valor aleatório.
Se o valor que o usuário digitou for 10, a condição do if vira verdadeira e o break quebra o loop.
Se não, os valores indicados pelo usuário são impressos na tela - sempre atenção a ordem das linhas de código.

### Comando continue

- Diferente do break, o continue serve para pular um trecho de código quando uma condição for verdadeira.
- break: quebra
continue: pula para a próxima iteração

```python
for i in range(100): 
	if i == 10:
		continue
	print(i)

>>> 0 1 2 3 4 5 6 7 8 9 11 ...
```

- Se a condição do if for verdadeira (i = 10), todo o trecho de código abaixo do continue não é executado. Pois o continue pula a iteração atual (onde i = 10) e passa para a próxima (i = 11).

<aside>
📌 **RESUMO:**

</aside>