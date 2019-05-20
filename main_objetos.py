"""funciones de 1nivel que pueden invocarse a si mismas y tienen
métodos asignados, iniciación a los objetos"""
"""iniciación a los objetos Oriented Object Programation(OOP)"""

import turtle

tortuguita = turtle.Turtle()#objeto del módulo turtle asignado a varible
otraTortuguita = turtle.Turtle()#otro objeto con las mismas características
lentorra = turtle.Turtle()#otro objeto


lentorra.speed(1)#damos velocidad a lentorra
tortuguita.shape("turtle")#tortuguita tiene forma de tortuga
tortuguita.color("blue")#tortuguita tiene color azul
tortuguita.fd(50)#tortuguita anda 50 pasos
tortuguita.speed(5)


otraTortuguita.color("green")#otraTortuguita tiene color verde
otraTortuguita.left(90)#otraTortuguita gira 90º a la izquierda
otraTortuguita.fd(50)#otraTortuguita anda 50 pasos
otraTortuguita.speed(5)