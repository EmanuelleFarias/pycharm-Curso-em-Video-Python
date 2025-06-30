
''' Faça um programa que leia um número qualquer e mostre
o seu fatorial '''

num = int(input('Digite um número: ')) # 5
resultado = 1
cont = 1
while cont <= num: #(1,2,3,4,5)
    resultado *= cont
    cont += 1
    print(resultado)

    #outro jeito

n = int(input('Fatorial de: '))
c = n
f = 1 #pq a base de multiplicação é 1, se fosse 0 o resultado seria sempre 0
print('Calculando...\n{}! = '.format(n), end = ' ')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))
