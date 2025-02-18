# for uses i como item
# necesita a range como inicializador y estos son los args (start,stop,step)
# for i in range(1,10,2):
#     print(str(i))
# el stop no es inclusivo y se debe poner el numero anterior
# acepta negativos, asi como el step para conteos regresivos
# for i in range (5,-1,-1):
#     print (str(i))

import random

# for i in range((random.randint(1,10))):
#     print('Hello')

# Juego de adivinar el numero
# Un programa que me 3 intentos para adivinar un numero secreto entre el 1 y el 10
numero=random.randint(1,10)
intentos=3

for intento in range (intentos):
    print('Que numero crees que estoy pensando')
    print('Tienes '+ str(intentos) + ' intentos')
    intentos -=1
    # entrada=int(input())
    try:
        entrada=int(input())
    except ValueError:
        print('El valor ingresado no es un numero, perdiste un intento te quedan '+str(intentos) +' intentos')
        #al usar continue en cualquier loop, se para y reinicia
        continue

    if numero == entrada:
        print('Felicidades es correcto! El numero es: '+ str(numero))
        print('Adivinaste usando '+ str(intento+1) + ' intentos')
        break
    elif intentos == 0:
        print('Fallaste miserablemente!')
        print('El numero que estaba pensando es ' + str(numero))

    elif numero < entrada:
        print('Intenta de nuevo, estas arriba')

    elif numero > entrada:
        print('Intenta de nuevo, estas abajo')

