# Autor: Ismael Vázquez Lamaiz
# Ejercicio 15: Usar isnumeric()

cadena = input("Introduce una cadena: ")

# isnumeric() devuelve True si todos los caracteres son dígitos
if cadena.isnumeric():
    print("La cadena es un número")
else:
    print("La cadena no es un número")
