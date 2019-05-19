"""operadores para trabajar con la función
anónima lambda"""
from functools import reduce

def doble(x):
    return x+x

def esPar(x):
    return 

lista = [1,3,-1,15,9]

#el operador map actúa sobre cada uno de los
#valores que utiliza la función
listaDobles = map(lambda x: x*2,lista)
listaDobles1 = map(doble,lista)

def esPar(x):
    return x%2==0
#operador filter aplica filtro a valores de
#lista que cumplan la condición
#lambda x: (condición,lista de valores)
#devuelve return si es true o none si es false
listaPares = filter(lambda x: x%2 == 0, lista)
listaPares1 = filter(esPar,lista)
#la línea superior es equivalente a:
#def f(x):
    #if x%2 == 0:
        #return x
    #else
        #return None

#operador reduce actúa según la operación que
#apliquemos en condición sobre los valores de
#lista
sumatorio = reduce(lambda x,y: x+y, lista)
sumatorioDobles = reduce(lambda x,y: x+y*2, lista)
suma100 = reduce(lambda x,y: x+y, range(101))

print(list(listaPares))
print(list(listaPares1))
print(sumatorio)
print(sumatorioDobles)
print(suma100)
