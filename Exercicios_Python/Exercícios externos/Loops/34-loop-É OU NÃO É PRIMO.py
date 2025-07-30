'''Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível
apenas por um e por ele mesmo. Faça um programa que peça um número
inteiro e determine se ele é ou não um número primo.'''


print('...'*20)
print(f"{' 🔢 É ou não é primo? 🔢':^60}")
print('...'*20)
print('')

num = int(input('Digite um número →  '))

cont = 0
for n in range(1, num + 1):
    if num % n == 0:
        cont += 1
if cont > 2:
    print(f'O número {num} NÃO É PRIMO.👎')
else:
    print(f'O número {num} É PRIMO.👍')

