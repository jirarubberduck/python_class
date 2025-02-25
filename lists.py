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
existo='Jesus' in ['Bruno','Angel','Diana','Jesus']
seguro_nohay_adalberto='Adalberto' not in ['Bruno','Angel','Diana','Jesus']
print('Existo? :'+str(existo))
print('Seguro que no existe Adalberto? :'+str(seguro_nohay_adalberto))

#nombra la lista que va a guardar los datos
nombres_de_gatos=[]

# def nombrar_gatos():
#     nombre_de_gato=input('Ingresa el nombre de un gato')
#     return nombre_de_gato

#pedir nombres de gatos en loop
while True:
    nombre_de_gato = input('Ingresa el nombre del gato '+str(len(nombres_de_gatos)+1)+' (o solo da enter para parar y ver la lista) \n')
    #si el nombre del gato ya existe decir 'ese nombre para gato ya existe ingresa uno diferente'
    if nombre_de_gato in nombres_de_gatos:
        print('Ese nombre para gato ya existe ingresa uno diferente')
        continue
    #hasta que el usuario ingrese un string vacio
    if nombre_de_gato=='':
        break
    #agregar nombre_de_gato a la lista va despues del break si no crearia una entrada EMPTY
    nombres_de_gatos=nombres_de_gatos+[nombre_de_gato]

#al final debe imprimir los nombres con un header de 'Los nombres de los gatos son:' y terminar el programa
print('Los nombres de los gatos son:')
for nombre_de_gato in nombres_de_gatos:
    print(nombre_de_gato)
#checar si Michi esta en la lista, si no mencionarlo
print()
if 'Michi' not in nombres_de_gatos:
    print('Que curioso que no tienes un gato llamado Michi')
elif 'Michi' in nombres_de_gatos:
    print('Si te acordaste de Michi! Nice!')