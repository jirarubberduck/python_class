#Desarrollar un juego en el cual se juega piedra, papel o tijeras contra la computadora.
#El output debe verse asi:
#"PIEDRA, PAPEL, TIJERAS
#0 Victorias, 0 Derrotas, 0 Empates
#Ingresa tu jugada: (p)iedra (a)papel (t)tijeras (s)alir
# a
# PAPEL contra...
# PAPEL
# ¡Es un empate!
# 0 Victorias, 0 Derrotas, 1 Empate
#
# Ingresa tu jugada: (p)iedra (a)papel (t)tijeras o (s)alir
# t
# TIJERAS contra...
# PAPEL
# ¡Ganaste!
# 1 Victoria, 0 Derrotas, 1 Empate
#
# Ingresa tu jugada: (p)iedra (a)papel (t)tijeras o (s)alir
# s"

import random

#Ingresa tu jugada: (p)iedra (a)papel (t)tijeras (s)alir
def main():
    print('PIEDRA, PAPEL, TIJERAS')

    opciones_validas=['p','a','t','s']
    resultados = {'Victorias': 0, 'Derrotas': 0, 'Empates': 0}
    print(resultados)

    while True:
        opcion = input('Ingresa tu jugada: (p)iedra (a)papel (t)tijeras o (s)alir \n')

        if opcion == '':
            print('Debes ingresar una jugada.')
            continue

        if opcion not in opciones_validas:
            print('Esa opcion no es valida.')
            continue

        if opcion == 's':
            break

        resultado=determinar_resultado_de_juego(opcion)
        contar_resultados(resultado, resultados)
        print(resultados)

def determinar_resultado_de_juego(jugada_humano):
    resultado=''
    jugada_valida = ['p', 'a', 't']
    jugada_cpu = random.choice(jugada_valida)
    print('DEBUG: jugada_cpu=' + jugada_cpu)

    if jugada_humano == 'p':
        print('PIEDRA contra ...')
        if jugada_cpu == 'p':
            print('PIEDRA')
            print('¡Es un empate!')
            resultado='empate'

        elif jugada_cpu == 'a':
            print('PAPEL')
            print('¡Perdiste!')
            resultado='perdida'

        elif jugada_cpu == 't':
            print('TIJERAS')
            print('¡Ganaste!')
            resultado='victoria'

    if jugada_humano == 'a':
        print('PAPEL contra ...')
        if jugada_cpu == 'p':
            print('PIEDRA')
            print('¡Ganaste!')
            resultado = 'victoria'

        elif jugada_cpu == 'a':
            print('PAPEL')
            print('¡Es un empate!')
            resultado='empate'

        elif jugada_cpu == 't':
            print('TIJERAS')
            print('¡Perdiste!')
            resultado='perdida'

    if jugada_humano == 't':
        print('TIJERAS contra ...')
        if jugada_cpu == 'p':
            print('PIEDRA')
            print('¡Perdiste!')
            resultado='perdida'

        elif jugada_cpu == 'a':
            print('PAPEL')
            print('¡Ganaste!')
            resultado = 'victoria'

        elif jugada_cpu == 't':
            print('TIJERAS')
            print('¡Es un empate!')
            resultado='empate'

    return resultado

def contar_resultados(resultado, resultados:dict):

    if resultado == 'empate':
        resultados=resultados.update('Empates',resultados.get('Empates')+1)

    elif resultado == 'perdida':
        resultados=resultados.update('Derrotas',resultados.get('Derrotas')+1)

    elif resultado == 'victoria':
        resultados=resultados.update('Victorias',resultados.get('Victorias')+1)

    return resultados

main()
