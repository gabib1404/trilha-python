curso = "Curso de Python"
nome_curso = curso

saldo = 200
limite = 200

print(curso is nome_curso)
print(nome_curso is not curso)

print(limite is saldo)

a = 1000
b = 1000
print(a is b)

print(id(saldo))
print(id(limite))