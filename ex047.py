
'''Crie um programa que mostre na tela todos os números pares
que estão no intervalo entre 1 e 20'''

for c in range(0,20,2):
    print(c,' - ' if 18 > c >= 0 else '', end = '')
   # print(c)

for c in range(0,20,2):
    if c < 18:
        print(c, end=' - ')
    else:
        print(c)

