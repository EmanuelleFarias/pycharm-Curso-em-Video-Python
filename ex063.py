'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
N primeiros elementos de uma Sequência de Fibonacci. Exemplo:0 1 1 2 3 5 8'''

print('~~~~ Sequência Fibonacci ~~~~')
qtde_termos = int(input('Quantos termos você quer ver? '))
a = 0
b = 1
print(a,'→',b,'→', end='')
c = b
cont = 3
while cont < qtde_termos + 1:
    print('{} → '.format(c), end='')
    a = b
    b = c
    c = a + b
    cont += 1
print('fim')
print()


