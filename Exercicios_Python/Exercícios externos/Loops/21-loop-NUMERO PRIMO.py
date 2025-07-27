#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int(input('Digite um número: '))

div = []
cont = 0

print(f"\n{num} é divisível por ele mesmo e mais ", end='')
for i in range(1, 10):
    if num % i == 0:
        div.append(i)
        cont+= 1

print(f'{cont} números: ')
print((', '.join(str(i) for i in div)), ".\nLogo, NÃO É UM NÚMERO PRIMO."if cont > 2 else f".\nLogo, É UM NÚMERO PRIMO.")

