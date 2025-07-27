#Faça um programa que leia 5 números e informe a soma e a média dos números.

num = []
soma = 0
for n in range(1,6):
    numero = int(input(f'Informe o {n}º número: '))
    soma += numero
    media = soma/5
print(f'\nA soma dos números é {soma}.')
print(f'A média entre os números é {media}.')