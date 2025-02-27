nombres_de_gatos=[]
def pedir_nombres_gatos():
    nombres=[]
    while True:
        nombre = input('Ingresa el nombre del gato ' + str(
        len(nombres) + 1) + ' (o solo da enter para parar y ver la lista) \n')
        # si el nombre del gato ya existe decir 'ese nombre para gato ya existe ingresa uno diferente'
        if nombre in nombres:
            print('Ese nombre para gato ya existe ingresa uno diferente')
            continue
        # hasta que el usuario ingrese un string vacio
        if nombre == '':
            break
        # agregar nombre a la lista va despues del break si no crearia una entrada EMPTY
        nombres = nombres + [nombre]
    return nombres

def imprimir_nombres_gatos(nombres_de_gatos):
    print('Los nombres de los gatos son:')
    for nombre_de_gato in nombres_de_gatos:
        print(nombre_de_gato)

def michi_en_lista(nombres_de_gatos):
    print()
    if 'Michi' not in nombres_de_gatos:
        print('Que curioso que no tienes un gato llamado Michi')
    elif 'Michi' in nombres_de_gatos:
        print('Si te acordaste de Michi! Nice!')


nombres_de_gatos=pedir_nombres_gatos()
imprimir_nombres_gatos(nombres_de_gatos)
michi_en_lista(nombres_de_gatos)