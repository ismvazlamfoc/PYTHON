# Autor: Ismael Vázquez Lamaiz
# Ejercicio 10: Capturar múltiples excepciones

# Primera parte: abrir un archivo que no existe
try:
    archivo = open("no_existe.txt", "r")
    print(archivo.read())
    archivo.close()
except FileNotFoundError:
    print("Error: el archivo no existe")

# Segunda parte: dividir entre un número introducido por el usuario
try:
    divisor = int(input("Introduce un divisor: "))
    print("Resultado:", 10 / divisor)
except ValueError:
    print("Error: debes introducir un número")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")
