#para crear funciones se utiliza def seguido de el short name de la funcion
#se ultilizan cuando la misma rutina de codigo varias veces

def primer_funcion():
    print('Primer Funcion')

def segunda_funcion(nombre):
    print('Hola '+nombre)

def tercera_funcion(nombre):
    welcome='Hola '+nombre
    return welcome

def va_a_fallar():
    mi_valor=0/0
    return mi_valor

#definir: hacer la firma(nombre lo que acepta, parametros y valores de retorno)
#llamar/invocar: cuando se hace uso de una funcion
#argumento: el valor real del parametro ejemplo "Jesus"
#parametro: es lo que esta definido como input en la funcion/lo que pide el template ejemplo "nombre"
#null: None en python, como True y False de los booleanos

nombre=print('cualquier texto, no importa')

print(nombre==None)
print('primer parametro', 'segundo parametro', 'tercer parametro')
print('primer parametro', 'segundo parametro', 'tercer parametro', sep=',', end='.')

#las funciones se apilan en el main thread o main program (no confundir con el archivo main)
#que es el punto de entrada y se llama el callstack
#el callstack define las fucniones disponibles y como se veran en el stack trace (traceback)
# C:\Users\jesus\AppData\Local\Programs\Python\Python313\python.exe C:\Users\jesus\python_class\functions.py
# cualquier texto, no importa
# True
# primer parametro segundo parametro tercer parametro
# primer parametro,segundo parametro,tercer parametro.Traceback (most recent call last):
#   File "C:\Users\jesus\python_class\functions.py", line 33, in <module>
#     va_a_fallar()
#     ~~~~~~~~~~~^^
#   File "C:\Users\jesus\python_class\functions.py", line 15, in va_a_fallar
#     return 0/0
#            ~^~
# ZeroDivisionError: division by zero
#va_a_fallar()

#todas las variables tienen un scope, hay globales (que todo el programa tiene acceso)
#hay variables locales que estan dentro de una funcion (solo pueden usadas en el codigo en ese contexto
# y cuando la funcion acaba los datos de la variable se eliminan del ram)
#variables locales, el bug puede ser contenido en una funcion y no se pueden usar en otras funciones
#variables globales, se pueden usar en cualquier funcion
#variables locales y globales pueden tener el mismo nombre pero hay que evitarlo

def test_global():
    global nombre
    nombre='Jesus'
    print(nombre+'Test 1')

def test_global_4():
    print(nombre+'Test 4')

def test_global_2():
    global nombre
    nombre = 'Luis'
    print(nombre+'Test 2')

def test_global_3():
    print(nombre+'Test 3')

#la variable global en caso de ser redefinida, a pesar de que la funcion haya sido creada en un order especifico
# en main, va a seguir la secuencia en la que las funciones son llamadas
print(nombre)
test_global()
test_global_2()
test_global_3()
test_global_4()

#idealmente las funciones deben verse como cajas negras; esto se logra con encapsulado su comportamiento en la
# funcion y aislandolo del resto del programa: ejemplo:
#error: son causados por funciones rudimentarias y normalmente se ven en programas de terminal, ejemplo:
# dividir 0/0
#execepcion: ocurren ya dentro de la aplicacion, mas complejo. es mas que un error, es un caso exepcional del
# programa, normalmente contiene un mensaje del contexto (donde fallo). ejemplo: meter 1TB de emojis en un
# text field, causa un stack overflow
#el try/catch funciona para operaciones riesgosas que pueden causar un error/excepcion

def manejo_de_excepciones(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print('Bad Request: Cannot divide by Zero')
    except TypeError:
        print('Escriba bien!')

manejo_de_excepciones(1,0)
manejo_de_excepciones(1,'hola')