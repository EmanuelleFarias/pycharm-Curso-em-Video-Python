''' Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
soma = 0
cont = 0
n = 0
while True:
    n = int(input('Digite um número: '))
    cont += 1
    if n == 999:
        break
    soma += n
print(f'A soma é {soma}.')
