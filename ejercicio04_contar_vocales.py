# Autor: Ismael Vázquez Lamaiz
# Ejercicio 4: Contar vocales

palabra = input("Introduce una palabra: ")

# Pasamos a minúsculas para contar mayúsculas y minúsculas por igual
palabra = palabra.lower()
vocales = "aeiou"
contador = 0

# Recorremos cada letra y sumamos si es una vocal
for letra in palabra:
    if letra in vocales:
        contador += 1

print("Número de vocales:", contador)
