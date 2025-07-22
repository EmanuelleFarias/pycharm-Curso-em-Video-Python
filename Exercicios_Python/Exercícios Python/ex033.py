n1 = int(input('número 1: '))
n2 = int(input('número 2: '))
n3 = int(input('número 3: '))
#para o número maior
if n1 > n2 and n1 > n3:
    print('O número {} é o maior de todos.'.format(n1))
if n2 > n1 and n2 > n3:
    print(' O número {} é o maior de todos.'.format(n2))
if n3 > n1 and n3 > n2:
    print('O número {} é o maior de todos.'.format(n3))
#para o número menor
if n1 < n2 and n1 < n3:
    print('O número {} é o menor de todos.'.format(n1))
if n2 < n1 and n2 < n3:
    print('O número {} é o menor de todos.'.format(n2))
if n3 < n1 and n3 < n2:
    print('O número {} é o menor de todos.'.format(n3))

    #outro jeito = descarta o menor e o maior e manda substituir

menor = n1 # quando boto assim estou atribuindo informação ( igual a primeira linha de todas )
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2> n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número é {}.'.format(maior))
print('O menor valor é {}.'.format(menor))
