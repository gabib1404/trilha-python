
""" -- Uso de variáveis -- """
age = 18 # Declaração de variáveis - podem mudar de valor ao longo do código (valores mutáveis)
name = "Gabriela"
print(f"Meu nome é {name} e eu tenho {age} anos")

age, name = (56, "Marcia") # Os valores das variáveis podem ser atribuídos separados por virgulas
print(f"Meu nome é {name} e eu tenho {age} anos")

# Declaração de constantes - não mudam de valor uma vez declaradas (valores imutáveis)
# NÃO EXISTE PALAVRA RESERVADA PARA DECLARAÇÃO DE CONTANTES
# Convenção - nome da variável todo em maiúsculas
ABS_PATH = 'C:\Users\gabib\OneDrive\Área de Trabalho\python-data'
DEBUG = True
AMOUNT = 22.6


""" -- Boas Práticas -- """
# 1. snake case - padrao_cobra
# 2. nomes sugestivos - não usar nomes genéricos/abreviados
valor_total = 200
taxa_juros = 0.15
nome_completo = "Juninho 'Pomba' Paçoca"
limite_saque_diario = 560
a = 560 # não recomendado
lim_saq_di = 560 # não recomendado

# 3. nome de constantes todo em maiúsculo
BRAZILIAN_STATES = ['SP', 'MG', 'RJ', 'ES']

print(BRAZILIAN_STATES)

