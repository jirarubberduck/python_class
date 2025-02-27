#lists and tuples son tipos de datos que nos ayudan a trabajar con grandes cantidades de datos
#una lista se define en python con [] se tiene la flexibilidad de tener listas con diferentes tipos de datos
#RETO: crear una lista con 5 tipos de datos distintos
#todas las listas inician en base 0, donde cero es el primer dato
#Traceback (most recent call last):
#   File "C:\Users\jesus\python_class\lists.py", line 12, in <module>
#     print(my_list[99])
#           ~~~~~~~^^^^
# IndexError: list index out of range
#puede contener indices negativos y comienza a contar al reves

mi_lista=[]
my_list=['string',54,5.9,True,None]

for i in my_list:
    print(i)

print(my_list[-5])

#slices, no son inclusivos, se marca el rango separando con :
#sencillo 2 datos
print(my_list[-4:-1])
#mid con solo el final
print(my_list[:3])
#mid solo con el inicio
print(my_list[2:])
#max sin marcaje
print(my_list[:])

#segunda mas importante es trabajar con su longitud
print(len(my_list))
#tercera modificacion de items posicion=nuevo item
my_list[1]=my_list[0]
my_list[-1]=12345

#concatenacion y replicacion de listas

lista_letras=['a','b','c','d','e','f']
lista_numeros=[1,2,3,4,5,6]
lista_juntos=lista_letras+lista_numeros+[None,None,None,None]

print(lista_juntos)

#como borrar un elemento de una lista
#se pueden usar slices
del lista_juntos[-4:]
print(lista_juntos)

#las listas sirven para agrupar elementos similates que tienen algo en comun ademas de el tipo de datos, es mas bien
#el significado

#operadores IN y NOT
# existo='Jesus' in ['Bruno','Angel','Diana','Jesus']
# seguro_nohay_adalberto='Adalberto' not in ['Bruno','Angel','Diana','Jesus']
# print('Existo? :'+str(existo))
# print('Seguro que no existe Adalberto? :'+str(seguro_nohay_adalberto))

#for tradicional en Python
#estos metodos tienen estas cosas en comun:
escritorio = ['pluma', 'teclado', 'monitor']
#Metodo 1-
for i in range(4):
    print(i)

for i in range(len(escritorio)):
    print(str(i+1) + ' ' + escritorio[i])

#Metodo 2- enumerate
for index,item in enumerate(escritorio):
    print(str(index +1) + ' ' + item)

#Multiple assignments (unpacking) desempacar una lista
hijo = ['small', 'cute', 'mischief']
# size = hijo[0]
# appeal = hijo[1]
# behavior = hijo[2]

#pythonic way
size,appeal,behavior=hijo

print(size, appeal, behavior, sep=',')

import random

print(random.choice(hijo))
#shuffle de random
random.shuffle(hijo)
print(hijo)

#Methods vs Functions
#Una funcion se le pasa un valor (es independiente y funciona sola, es luchona vaya)
#Las funciones suelen ser utilerias ejemplo: sacar un promedio o imprime algo
#Un metodo es lo opuesto, corresponde a un objeto es su funcionalidad
#va ligado intrinsecamente a un objeto ejemplo: persona.digerir() persona.respirar()

saludos = ['Hola', 'Buen dia', 'god dag', 'Hello']
saludos.index('Buen dia')

#Agregando valores a una lista
#Metodo 1- con append lo agrega en el ultimo index de la lista
#Metodo 2- con insert lo agrega a un index especifico
saludos.append('Bonjour')

saludos.insert(1,'Hallo')

print(saludos)

#Remover valores de la lista
saludos.remove('Hola')

print(saludos)

#Ordenado de listas alfabeticamente
saludos.sort()
print(saludos)
#al reves
saludos.sort(reverse=True)
print(saludos)
#considerar las minusculas asi no se van al final, jerarquia primer Caps - lower
saludos.sort(key=str.lower)
print(saludos)

#como definir una lista vacia
lista=[]
#como asignar el valor Hello como el 3 valor en una lista con 4 numeros
spam=['uno', 'dos', 'tres', 'cuatro']
spam[2]='Hello'