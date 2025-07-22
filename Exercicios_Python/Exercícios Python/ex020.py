from random import  sample, shuffle

a1 = input('aluno 1:')
a2 = input('aluno 2:')
a3 = input('aluno 3:')
a4 = input('aluno 4:')
l = a1,a2,a3,a4
s = sample(['a1', 'a2', 'a3', 'a4'], k=len(l), counts=[1,1,1,1])
print('a ordem é {}.'.format(l))

#ou
a1 = input('aluno 1:')
a2 = input('aluno 2:')
a3 = input('aluno 3:')
a4 = input('aluno 4:')
l = [a1,a2,a3,a4]
s = shuffle(l)
print('a ordem é {}.'.format(l))