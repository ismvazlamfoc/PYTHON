# Autor: Ismael Vázquez Lamaiz
# Ejercicio 9: Verificar si un input es un número

try:
    # Si el texto no es un número, int() lanza ValueError
    numero = int(input("Introduce un número: "))
    print("El número introducido es", numero)
except ValueError:
    print("Error: debes introducir un número válido")
