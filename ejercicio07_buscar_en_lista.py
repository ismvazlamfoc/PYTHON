# Autor: Ismael Vázquez Lamaiz
# Ejercicio 7: Buscar un elemento en una lista

# Lista de videojuegos
videojuegos = ["Zelda", "Mario Kart", "Minecraft", "FIFA", "Fortnite"]

juego = input("¿Qué videojuego quieres buscar? ")

# Comprobamos si el juego está en la lista
if juego in videojuegos:
    posicion = videojuegos.index(juego)
    print(juego, "está en la lista, en la posición", posicion)
else:
    print(juego, "no está en la lista")
