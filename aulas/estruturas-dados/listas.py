

carros = ["gol", "palio", "celta"]

for indice, carro in enumerate(carros): 
	print(f"{indice + 1}: {carro}")


linguagens = ["python", "Java", "C#", "javascript", "PHP"]
"""
entrada = input("Digite uma linguagem: ")
while True: 
	try:
		print(f"Índice encontrado: {linguagens.index(entrada)}")
		break
	except ValueError:
		print("Objeto não encontrado na lista!")
		break"""

linguagens.sort(reverse = True)
print(linguagens)

linguagens.sort(key = lambda x : len(x))
print(linguagens)

linguagens.sort(key = str.lower)
print(linguagens)

linguagens.sort(key = len, reverse = True)
print(linguagens)

print(sorted("python"))
print(sorted(linguagens))
print(sorted("python", reverse = True))