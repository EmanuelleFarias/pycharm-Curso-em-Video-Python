print('\n{:^50}\n'.format('⋱⁂⋰ ¡Hola! ⋱⁂⋰'))
while True:
    try:
        print('※ Para iniciar ingrese un número entero.\n※ Para finalizar ingrese 0.')
        num = int(input('\n▸▸ Tu elección es: '))
    except ValueError:
        print('\n✕ Opção inválida. ✕ Elige un número entero, por favor.\n')
        continue
    if num < 0:
        print('\n✕ Opção inválida. ✕ Elige un número entero positivo, por favor.\n')
        continue
    if num == 0:
        print('\n ▲ Programa finalizado ▲\n\n{:⊹^50}\n'.format(' ⊹⋒ ¡Hasta pronto! ⋒⊹ '))
        break

    print('\n▸ El número elegido fue {}.\n \n⁑∗¡Arranquemos!⁑∗'.format(num))
    frase = str(input('\n▸▸▸ Ingrese una palabra o frase: '))
    carac = len(frase)  # -frase.count(' ') sin espacio
    print(f'\n▸ "{frase}" tiene {carac} caracteres.')

    fat = 1
    for f in range(1, carac + 1):
        fat *= f
    print('\n▸ El fatorial de {}! = {}'.format(carac, fat))
    print('\n▸ El número {} es par.\n'.format(fat) if fat % 2 == 0 else '\n▸ El número {} es ímpar.\n'.format(fat))

