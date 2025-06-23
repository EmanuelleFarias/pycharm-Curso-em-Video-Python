'''  tabuada de um número
que o usuário escolher, utilizando um laço for'''
7
n = int(input('Digite um número: '))
for c in range(n*0,n*11,n):
    print(c, end=' ') # end=' ' pra ficar na horizontal


n = int(input("\nDigite um número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")