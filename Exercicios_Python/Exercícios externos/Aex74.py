'''
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
'''

from random import randint
tupla = ()
lista = list(tupla)


for n in range(0,5):
    lista.append(randint(0,100))
tupla = tuple(lista)
print('Os números sorteados foram:', end=' ')

print(', '.join(str(n) for n in tupla))
print(f'\nO maior número é {max(tupla)}.')
print(f'O menor número é {min(tupla)}.')
