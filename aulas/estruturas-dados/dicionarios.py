# Entre chaves

pessoa = {"nome": "Gabriela", "idade":18}

# Método dict
pessoa = dict(nome = "Gabriela", idade = 18) # Chave sem aspas, mesmo se for string simples

pessoa["telefone"] = 40028922

print(pessoa)

dados = {'nome': 'Gabriela', 'idade': 18, 'telefone': 40028922}

print(dados["nome"])

print(dados["idade"], dados["telefone"])

# Dicionários aninhados
contatos = {
	"Gabriela": {"email": "gabibrumf@yahoo.com", "telefone": 40028922},
	"João": {"email": "joao@gmail.com", "telefone": 40028922},
	"Isabela": {"email": "isabela@gmail.com", "telefone": 40028922}, 
}

# Fatiamento
print(contatos["Gabriela"])
print(contatos["Gabriela"]["telefone"])

# Iterar dicionários
for chave in contatos: 
	print(chave, contatos[chave])

for chave, valor in contatos.items():
	print(chave, valor)


# fromkeys()
dicionario = dict.fromkeys(["a", "b"], "vazio")

print(dicionario)
dicionario = dicionario.fromkeys(["c", "d"], "vazio")
print(dicionario)

# items()
print(contatos.items())

# keys()
nomes = contatos.keys()
print(nomes)

# pop()
