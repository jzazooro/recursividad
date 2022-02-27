from random import randint

fichas = ["Rojo", "Azul", "Verde"]

tabla = []

indice = 0

numerodefichas = int(input("¿Con cuantas fichas desea jugar?: "))

def creartablero(fichas, tabla, indice, numerodefichas):
    indice = indice +1
    if indice <= numerodefichas:
        tabla.append(fichas[randint(0,2)])
        creartablero(fichas, tabla, indice, numerodefichas)

creartablero(fichas, tabla, indice, numerodefichas)

print(tabla)