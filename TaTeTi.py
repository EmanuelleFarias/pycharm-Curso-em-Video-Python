def mostrar_tablero_amplio(tablero):
    print()
    print(("+" + "-----")*3 + "+")
    for fila in tablero:
        print(("|" + "     ")*3 + "|")
        print("|  {}  |  {}  |  {}  |".format(*fila))
        print(("|" + "     ")*3 + "|")
        print(("+" + "-----")*3 + "+")

def verificar_victoria(tablero, jugador):

    for i in range(3):
        if all([tablero[i][j] == jugador for j in range(3)]):
            return True
        if all([tablero[j][i] == jugador for j in range(3)]):
            return True

    if all([tablero[i][i] == jugador for i in range(3)]) or \
       all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True
    return False

def jugar_tateti():
    tablero = [[str(i + j * 3) for i in range(3)] for j in range(3)]
    jugador = 'X'
    turnos = 0

    while True:
        mostrar_tablero_amplio(tablero)
        print(f'\nTurno del jugador {jugador}')
        try:
            jugada = int(input('Ingresa tu movimiento: '))
            if jugada < 0 or jugada > 8:
                print('⚠️ Casilla inválida.')
                continue
            fila, col = divmod(jugada, 3)
            if tablero[fila][col] in ['X', 'O']:
                print('⛔ Casilla ocupada.')
                continue
        except ValueError:
            print('❌ Entrada no válida.')
            continue

        tablero[fila][col] = jugador
        turnos += 1

        if verificar_victoria(tablero, jugador):
            mostrar_tablero_amplio(tablero)
            print(f'\n🏆 ¡{jugador} ha ganado!')
            break
        elif turnos == 9:
            mostrar_tablero_amplio(tablero)
            print('\n🤝 ¡Empate!')
            break

        jugador = ('O' if jugador == 'X' else 'X')


jugar_tateti()