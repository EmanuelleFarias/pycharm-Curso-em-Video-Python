''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.'''
from random import randint
jpc = randint(0, 10)
pc = jpc
while True:
    n = int(input('Diga um número: '))
    pi = str(input('Par ou Ímpar (P/I): ')).strip().lower()
    s = pc + n
    print(f'Você jogou {n} e o PC jogou {jpc} \nA soma  é {s}')
    if s % 2 == 0 and pi == 'p':
        print(f'...e é PAR!!! VOCÊ GANHOU!!!')
    elif s % 2 != 0 and pi == 'i':
        print('... e é ÍMPAR!!! VOCÊ GANHOU!!!')
    else:
        print('VOCÊ PERDEU...')
        break