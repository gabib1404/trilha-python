# Eliminar duplicações
print(set([1, 2, 5, 2, 6])) # {1, 2, 5, 6}

print(set("abacaxi")) # {"b", "a", "c", "x", "i"} 

print(set(("palio", "gol", "celta", "palio"))) # {}

linguagens = {"python", "java", "c#", "python", "java"}
print(linguagens)

naturais = {1,6,5,8,2,2}
naturais = list(naturais) # Transforma o conjunto em uma lista para acessar os elementos
print(naturais[2])

# Métodos da classe set
a = {1,2,3,4,5,6}
b = {5,6,7,8,9,10}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

a.add(5)
print(a)

a.discard(3)
a.discard(10)
print(a)

a = {1, 2, 4, 5, 6, 1, 8, 7, 5, 2, 4, 9}

print(len(a))