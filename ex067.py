''' Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.'''
t = 0
cont = 0
while True:
    t = int(input('Quer ver a tabuada de qual número? '))
    if t < 0:
        break
    for c in range (1,11):
        print(f'{t} x {c} = {c*t}')
print('programa encerrado')