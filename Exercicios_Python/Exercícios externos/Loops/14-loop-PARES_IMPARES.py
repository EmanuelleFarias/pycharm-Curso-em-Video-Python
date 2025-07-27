#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
# números pares e a quantidade de números impares.

pares = []
impares = []

for n in range(1,11):
    num = int(input(f'Digite o {n}º número inteiro: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'A quantidade de números pares é: {len(pares)}')
print(f'A quantidade de números ímpares é: {len(impares)}')