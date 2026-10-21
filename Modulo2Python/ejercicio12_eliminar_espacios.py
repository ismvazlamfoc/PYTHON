# Autor: Ismael Vázquez Lamaiz
# Ejercicio 12: Eliminar espacios en blanco

cadena = input("Introduce una cadena con espacios al inicio y al final: ")

# strip() elimina los espacios del principio y del final
limpia = cadena.strip()

print("Antes: [" + cadena + "]")
print("Después: [" + limpia + "]")
