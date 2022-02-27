# recursividad

Mi direccion de GitHub para este repositorio es la siguiente: [GitHub]()


Hemos reselto tres ejercicios que consisten: el primero en buscar por dicotomia en una tabla; el segundo en detectar si en una lista de lementos hay algun palindromo; y el tercero es el famoso problema de la bandera de Dijkstra.

Ejercicio 1: Busqueda por dicotomia en una tabla ordenada

```
while True:
    tabla = input("Por favor elija los elementos de la tabla con espacios: ")
    tabla = tabla.split()
    try: 
        for i in range(len(tabla)):
            tabla[i] = int(tabla[i])
        print("ahora se ordenaran los elementos como tipo int")
    except: 
        try: 
            for i in range(len(tabla)):
                tabla[i] = float(tabla[i])
            print("ahora se ordenaran los elementos como tipo coma flotante")
        except:
            print("ahora los elementos se ordenaran como tipo sting")
    break

tabla.sort()

elemento = input("Por favor seleccione el elemento que quiere buscar en la tabla: ")

def buscarentabla(tabla, elemento, indice): 
    if elemento == str(tabla[indice]):
        print("el elemento si se enccuentra en la tabla")
    else :
        if indice < (len(tabla)-1):
            indice = indice+1
            buscarentabla(tabla, elemento, indice)
buscarentabla(tabla, elemento, 0)
```

Ejercicio 2: Palindromos

```

```

Ejercicio 3: La bandera de Dijkstra

```
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
```
