'''5. Construir um algoritmo que calcule a média aritmética de vários
valores inteiros positivos, lidos externamente. O final da leitura
acontecerá quando for lido um valor negativo.'''



print('...'*20)
print(f"{'MEDIA':^60}")
print('...'*20)
print('')


total = 0
cont = 0

while True:
    print('Para encerrar digite um número inteiro negativo.')
    num = input('\nDigite um número inteiro positivo: ')
    if not num.lstrip("-").isdigit():
        print('Entrada inválida. Digite apenas um número inteiro positivo.')
        continue
    num = int(num)

    if num < 0:
        break
    total += num
    cont += 1
if cont > 0:
    media = total / cont
    print(f'\nA média entre os {cont} números digitados é {media:.2f}.')
else:
    print('\nNenhum número positivo foi inserido.')





