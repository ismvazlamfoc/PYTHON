# Autor: Ismael Vázquez Lamaiz
# Ejercicio 6: Ordenar una lista

entrada = input("Introduce números separados por comas: ")

# Separamos por comas y convertimos cada valor a número
partes = entrada.split(",")
numeros = []
for parte in partes:
    numeros.append(float(parte))

# Ordenamos de menor a mayor
numeros.sort()

print("Números ordenados:", numeros)
