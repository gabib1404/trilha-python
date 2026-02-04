
""" -- int para float -- """

preco = 10 # variável inteira
print(preco) # 10

preco = float(preco) # transforma 'preco' em float
print(preco) #10.0

preco = preco/2 # divisão também transforma em float
print(preco) # 5.0

""" -- float para int -- """

preco = 10.30
print(preco) # 10.3

preco = int(preco) # transforma a variavel em inteira
print(preco) # 10 (arredondado para baixo)

""" -- conversão por divisão -- """
preco = (preco/2) # transforma em float
print(preco) # 5.0

preco = (preco//2) # preserva o tipo int
print(preco) # 2 (arredondado para baixo)

""" -- numérico para string -- """
preco = 10.50
idade = 18

print(str(preco)) # transforma em tipo string (cadeia de caracteres)
print(str(idade)) 

texto = f"idade: {idade} preço {preco}" # concatena as variáves (agora string) dentro do texto
print(texto) # "idade 18 preço 10.50"

""" -- string para numérico -- """
preco = "10.50" # variavel string
print(float(preco)) # 10.50

idade = "18"
print(int(idade)) #18

""" --  erro de conversão -- """
nome = "python"
#print(float(nome)) 
# ValueError: valor inválido para ser transformado em float

""" -- observações -- """

print(type(str(10.56))) # função type(): imprime qual o tipo da variavel/valor que está dentro dele
# <class 'str'> 
print(type(10))
# <class 'int'>
print(type(10/2))
# <class 'float'>
print(type(50//5))
# <class 'int'>