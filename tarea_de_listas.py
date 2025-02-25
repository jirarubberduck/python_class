#Convertir este while en funcion para solo llamar al archivo y funcione
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