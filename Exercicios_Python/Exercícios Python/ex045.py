from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
opc = randint(0,2)
print(''' Escolha entre uma das opções abaixo:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
opj = int(input('Sua opção é: '))
if opj != 0 and opj != 1 and opj != 2:
    print('\033[0;31mJogada inválida!!!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('-=' * 11)
    print('O computador jogou {}.'.format(itens[opc]))# format = dentro dos itens, a posição opc
    print('Jogador jogou {}.'.format(itens[opj]))# format = dentro dos itens, a posição opj
    print('-='*11) # -=-=-=-=-=-=-=-=-=-=-=
if opc == 0: # pedra
    if opj == 0: # pedra
        print(' EMPATE')
    elif opj == 1: # papel
        print('JOGADOR VENCE')
    elif opj == 2: # tesoura
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida!!!')
elif opc == 1: # papel
    if opj == 0: # pedra
        print('COMPUTADOR VENCE')
    elif opj == 1: # papel
        print('EMPATE')
    elif opj == 2: # tesoura
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida!!!')
elif opc == 2: # tesoura
    if opj == 0: # pedra
            print('JOGADOR VENCE')
    elif opj == 1: # papel
            print('COMPUTADOR VENCE')
    elif opj == 2: # tesoura
            print('EMPATE')
    else:
            print('Jogada inválida!!!')




