""" -- etapa 1 (função input) -- """

"""_função input_

- lê dados de entrada padrão (teclado)
- recebe um argumento do tipo string
- lê a entrada, transforma em string, e retorna o valor
"""

nome = input("Informe o seu nome: ")
# >>> Informe o seu nome: |

""" -- etapa 2 (função print) -- """

"""_função print_ 

- exibir dados na tela (saída padrão)
- recebe um argumento varargs (número variável de argumentos) e 4 opcionais (sep, end, file, flush)
- todos os objetos são convertidos para string (separados por sep, e terminados por end).

"""

sobrenome = "brum"

print(nome, sobrenome) # Gabriela Brum
print(nome, sobrenome, end="...\n") # Gabriela Brum...
# end = argumento final, adiciona ao final da string

print(nome, sobrenome, sep="*") # Gabriela*Brum
# sep =  separador, adiciona o argumento sempre que a string for "separada"

""" -- treino -- """
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="!!!! \n") # por padrão, end=\n
print(nome, idade, sep=":    ")