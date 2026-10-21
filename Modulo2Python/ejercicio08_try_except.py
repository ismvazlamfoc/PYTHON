# Autor: Ismael Vázquez Lamaiz
# Ejercicio 8: Manejo de excepciones (try-except)

numero = 10

try:
    # Esta división provoca un error
    resultado = numero / 0
    print("Resultado:", resultado)
except ZeroDivisionError:
    # Capturamos el error para que el programa no se detenga
    print("Error: no se puede dividir entre cero")

print("El programa continúa")
