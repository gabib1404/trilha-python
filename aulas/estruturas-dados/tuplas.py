carros = ("gol", "celta", "palio",)

for indice, carro in enumerate(carros):
	print(f"{indice}: {carro}")

for indice, carro in enumerate(carros, 1):
	print(f"{indice}: {carro}")