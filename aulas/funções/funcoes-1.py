
# Criar a função
def exibir_mensagem():
    print("Hello World!")

exibir_mensagem()

    # Funções com parâmetros
def boas_vindas(nome):
    print(f"Seja bem-vindo {nome}!")

boas_vindas(nome = 'gabi')

def boas_vindas2(nome = "Anônimo"):
    print(f"Seja bem-vindo {nome}")

boas_vindas2()
boas_vindas(nome = 'isa')

""" Retorno de funções """

def calcular_total(numeros): 
	return sum(numeros) # Retorna apenas um valor
	
def retorna_antecessor_sucessor(numero): 
	antecessor = numero - 1
	sucessor = numero + 1
	
	return antecessor, sucessor
	

calcular_total([10, 20, 30, 40]) # 100

retorna_antecessor_sucessor(10) # (9, 11) -> Retorna uma tupla

def func_3():
    print("Olá!")
    # return None

func_3() # "Olá!" -> não retorna nada, pois é o valor padrão
print(func_3()) # "Olá!" e None -> imprime o valor padrão de retorno


""" Argumentos nomeados """

def salvar_carro(marca, modelo, ano, placa): 
    # Salva um carro no banco de dados
    print(f"Carro salvo no inventário! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("fiat", "palio", 2011, "nnao-5311") # Argumentos posicionados
salvar_carro(marca="fiat", modelo="palio", ano=2011, placa="nnao-5311") # Argumentos nomeados
salvar_carro(**{"marca":"fiat", "modelo":"palio", "ano": 2011, "placa":"nnao-5311"}) # Por dicionários

""" Args e kwargs """

def exibir_poema(data_extenso, *args, **kwargs): 
    texto = "\n".join(args)
    meta_dados = "\n".join(f"{chave.title()}: {valor}" for chave, valor in kwargs.items())
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("terça-feira, 03 de fevereiro de 2026", "to be or not to be", "that is the question", autor = "shakespeare", ano = 1999)