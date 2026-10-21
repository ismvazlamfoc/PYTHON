# Autor: Ismael Vázquez Lamaiz
# Ejercicio 14: Manejo de excepción con finally

archivo = None

try:
    archivo = open("no_existe.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("Error: el archivo no existe")
finally:
    # Este bloque se ejecuta siempre, haya error o no
    if archivo is not None:
        archivo.close()
    print("Fin del programa")
