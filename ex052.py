''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''
t = 0 #contagem de números divisíveis zerada
num = int(input('Digite um número inteiro: '))
for p in range(1,num+1):
    if num % p == 0:
        print('\033[33m', end='') # linha de cor (esse end='' é pra seguir na mesma linha)
        t += 1 #cada vez que for divisível soma 1 ao total 0, por isso t = t +1
    else:
        print('\033[31m',end = '')# linha de cor
    print('{}'.format(p), end='') #linha que aparece a contagem
print('\n\033[mO número {} foi dividido {} vezes.'.format(num,t))
if t == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')




