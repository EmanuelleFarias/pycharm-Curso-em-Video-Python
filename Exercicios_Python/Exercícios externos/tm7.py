'''a = 5
b = 15
c = 20
print('a == b and b > c:', a == b and b > c)
print('a < b or b > c: ', a < b or b > c)
print('not a == b:', not a == b)'''
a = input('Informe um valor para a variável A: ')
b = input('Informe um valor para a variável B: ')
if a > b:
    aux = a
    a = b
    b = aux
print('O valor da variável A agora é ', a)
print('O valor da variável B agora é ', b)
