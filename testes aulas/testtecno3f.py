from random import randint

print('\nHola, soy tu computadora...🤖🖥️')
print('\nEstoy pensando en un número entre 0 y 10. 🤖💭\nTe reto a adivinar cuál es el número. Tienes 5 intentos.\n')

random_number = randint(0, 10)
maxtent = 5
intentos = 0

while intentos < maxtent:
    try:
        num = int(input('Intenta adivinar el número: '))
    except ValueError:
        print('\n⚠️ Jugada inválida!!! Elige un número entre 0 y 10.\n')
        continue

    if 0 <= num <= 10:
        intentos += 1
        intrest = maxtent - intentos  # Calculamos el número de intentos restantes antes de usarlo

        if num == random_number:
            print('\n🎯 Adivinaste después de {} tentativa(s)!!!🎉\n'.format(intentos))
            break
        elif num < random_number:
            print('\n🔼 El número es mayor... Intenta nuevamente.')
        else:
            print('\n🔽 El número es menor... Intenta nuevamente.')

        print('🍀 Tienes {} tentativas restantes!\n'.format(intrest))

    else:
        print('\n⚠️ Jugada inválida!!! El número debe estar entre 0 y 10.')

if intentos >= maxtent and num != random_number:
    print('\n❌ Tentativas agotadas. El número correcto era {}.'.format(random_number))