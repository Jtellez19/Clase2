diccionario = {}

num_personas = int(input("Cuantas personas son?"))

for turno in range(num_personas):
    nombre = input("Nombre {0}: ".format(turno+1))
    numero = int(input("Numero {0}: ".format(turno+1)))
    diccionario[nombre] = numero

for key, value in diccionario.items():
    print(key," : ",value)

mayor = diccionario[max(diccionario,key = diccionario.get)]
menor = diccionario[min(diccionario,key = diccionario.get)] 
######Actividad Avanzada
import numpy as np

diccionario = {}

num_personas = int(input("Cuantas personas son?"))

for turno in range(num_personas):
    nombre = input("Nombre {0}: ".format(turno+1))
    numero = np.random.randint(100,500)
    diccionario[nombre] = numero

for key, value in diccionario.items():
    print(key," : ",value)

mayor = diccionario[max(diccionario,key = diccionario.get)]
menor = diccionario[min(diccionario,key = diccionario.get)] 
