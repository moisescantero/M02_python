"""funcion anónima lambda para agregar funciones sin
tener que crearlas en el módulo importado"""

from main_funciones_1nivel02 import sumaTodos

doble= lambda x: x*2#asignar función a variable y después imprimir
triple= lambda x: x*3
print(sumaTodos(3, doble))
print(sumaTodos(100, triple))

#print(sumaTodos(3, lambda x: x*2))#usar funcion directamente en print
