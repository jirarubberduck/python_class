#repl - Read Evaluate Print Loop
#expression - calueas and operators (get evaluated to 1 value)

#Operadores
#exponente - potenciacion
2**3
#modulo o remanente - solo imprime la diferencia al siguiente multiplo
22%8
#diferencia entre entero y flotante division de enteros, te da el ultimo divisor entero
22//8
#division /, multiplicacion *, adicion + y substamccion - (se usan parentesis para el orden de la operaciones)
4/(2*(3+5))

#Data types
#Enteros - negativos y positivos - int
#Punto Flotante - de negativo a positivo - Float
#Cadenas - caracteres - string
#Concatenacion de Cadenas - String concat
'Jesus' + 'Oros'
'Jesus' + '7'
'Jesus' + str(7)

#Declaracion de asignamiento
#asignacion de valores en RAM

#inicializacion
nombre='Jesus'
apellido='Oros'
edad=7
#empleo

#asignacion
nombre + apellido + str(edad)

#Buena practica en naming convention
#No numero o signo like 4jesus _jesus ni caracter
#comentar solo lo que no sea obvio o reminders
#usar
#input siempre entrega un string

print('Hola Mundo')
print('Cual es tu nombre:')
nombre=input()
print('Es un gusto conocerte, ' + nombre)
len(nombre)
efectivo=float(input())
efectivo=30.72 + efectivo
print(str(efectivo))

# Diferencia entre un valor y un operador 'valor' 7 5.4
#
# Operadores * + -
#
# Variable nombre='Jesus' String 'Jesus'

#Control de flujo
#syntachtic sugar
#Condicionales - para evaluar expresiones
#Boolean - True y False
#se pueden asignar a una variable o dentro de un condicional - predefernte en una variable

# is_valid=True
# 42==42
# 2!=3

# print('Cual es tu edad:')
# #edad=int(input())
# es_mayor_de_edad=edad>=18
# es_jubilado=edad>=60

# if #edad >=60:
#     print('Jubilado')
# elif es_mayor_de_edad:
#     print('SI es mayor de edad')
# else:
#     print('NO es mayor de edad')

#Ciclos
#while = mientras no se cumpla una condicion (booleana regularmente)
#for = ya esta establecido el numero de repeticiones

# while True:
#   print('Bienvenido al juego')
#   print('Ingresa Q para salir')
#   entrada=input()
#   if entrada=='Q':
#     break
#debug para tarea

#hay dos tipos de valors booleanos: True y False
#cuales son los operadores booleanos: = != < > and y el or y el not
#da un ejemplo de cuando se usaria una condicion

print('De que ciudad nos visitas')
ciudad=input()
if ciudad=='Ensenada':
  print('Bienvenido')
else:
  print('Viaja a Ensenada')