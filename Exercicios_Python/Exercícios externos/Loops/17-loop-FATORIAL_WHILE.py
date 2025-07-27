#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('O fatorial de → '))
print(f'{num}! = ', end='')

f = 1
while num > 0:
    print(f'{num}', end=' x ' if num > 1 else ' \né... ')
    f *= num
    num -= 1
print(f)

