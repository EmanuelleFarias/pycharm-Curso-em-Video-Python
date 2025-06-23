from random import choice

n1 = input('nome 1:')
n2 = input('nome 2:')
n3 = input('nome 3:')
n4 = input('nome 4:')
e = choice([n1, n2, n3, n4])
print('O aluno escolhido é {}.'.format(e))

#ou

n1 = str(input('nome 1:'))
n2 = str(input('nome 2:'))
n3 = str(input('nome 3:'))
n4 = str(input('nome 4:'))
l = [n1, n2, n3, n4]
e = choice(l)
print('O aluno escolhido é {}.'.format(e))
