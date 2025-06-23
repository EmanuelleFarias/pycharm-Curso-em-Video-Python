'''2. Faça um programa, utilizando while, que mostre na tela de 0 até N,
em que N é o limite inserido pelo usuário.'''


limite = int(input('escolha um limite para a contagem: '))
l = 0
while l <= limite:
    l = l +1
    print(l-1, end=' ')
print('fim')