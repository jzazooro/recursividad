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
