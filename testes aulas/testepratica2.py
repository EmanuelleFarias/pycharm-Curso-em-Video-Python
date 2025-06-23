print('\n{:^50}\n'.format('⋱⁂⋰ ¡Hola! ⋱⁂⋰'))
while True:
    try:
        print('※ Para iniciar ingrese un número entero.\n※ Para finalizar ingrese 0.')
        num = int(input('\n▸▸ Tu elección es: '))
    except ValueError:
        print('\n✕ Opción inválida. ✕ Elige un número entero, por favor.\n')
        continue
    if num < 0:
        print('\n✕ Opción inválida. ✕ Elige un número entero positivo, por favor.\n')
        continue
    elif num > 0:
        print('\n▸ El número elegido fue {}.\n \n⁑∗¡Arranquemos!⁑∗'.format(num))
        frase = str(input('\n▸▸▸ Ingrese una palabra o frase: '))
        carac = len(frase)#-frase.count(' ') sin espacios
        print(f'\n▸ "{frase}" tiene {carac} caracteres.')
    else:
        print('\n ▲ Programa finalizado ▲\n\n{:⊹^50}\n'.format(' ⊹⋒ ¡Hasta pronto! ⋒⊹ '))
        break
    n = carac
    f = 1
    print('\n▸ Calculando el fatorial...\n{}! = '.format(n), end = ' ')
    while n > 0:
        print('{}'.format(n), end = '')
        print(' x ' if n > 1 else ' = ', end = '')
        f *= n
        n -= 1
    print('{}'.format(f))
    print('\n▸ El número {} es par.\n'.format(f)if f % 2 == 0 else '\n▸ El número {} es ímpar.\n.'.format(f))
