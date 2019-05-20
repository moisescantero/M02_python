"""función recursiva es aquella que se llama a
sí misma y que debe tener un parámetro de
salida para que no se ejecute hasta infinito"""

#hacer def factorial(n):


def retroContador(e):

    print("{},".format(e),end="")
    
    if e > 0:
        retroContador(e-1)

retroContador(10)

def sumatorio(n):
    if n != 0:
        return n + sumatorio(n-1)
    else:
        return 0
sumatorio(4)