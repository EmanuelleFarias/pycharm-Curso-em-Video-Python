'''Faça um programa que calcule a soma entre todos os números impares
 que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.'''
s = 0
for c in range(1,500,2):
    if c % 3 == 0:
        s = s + c
print('A soma entre os números é {}.'.format(s))

