'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
num1 = randint(1,10)
num2 = randint(1,10)
num3 = randint(1,10)
num4 = randint(1,10)
num5 = randint(1,10)
tupnum = (num1,num2,num3,num4,num5)
print('Os números sorteados foram',tupnum)
sorted(tupnum)
print(f'O menor número sorteado foi {min(tupnum)}')
print(f'O maior número sorteado foi {max(tupnum)}')