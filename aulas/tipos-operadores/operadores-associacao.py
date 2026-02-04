""" -- Com listas -- """
frutas = ["maçã", "laranja", "morango"]

print("morango" in frutas)
print("Morango" in frutas) # False - O uso de letras maiúsculas importa (case sensitive)
print("limão" in frutas)
print("limão" not in frutas)
print("\n")

""" -- Com strings (sequências de caracteres) -- """
curso = "Curso de Python"

print("Curso" in curso)
print("python" in curso)
print("de" not in curso)
print("P" in curso)