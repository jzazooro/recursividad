import unicodedata

frase = input("Por favor escribe una oracion: ") 
filtro = frase.split()
filtro = ''.join(filtro)

def palindromo(N,M):
    if N < M:
        if filtro[N] == filtro[M]:
            palindromo(N+1,M-1)
        else:
            print("No se trata de un palindromo")
    elif N > M:
        palindromo(N,M+1)
    else:
        if filtro[N] == filtro[M]:
            print("Se trata de un palindromo")
        else:
            print("No se trata de un palindromo")

a = len(filtro)
b = 0
palindromo(b,a-1)