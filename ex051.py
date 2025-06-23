''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''
t = int(input('digite o primeiro termo da PA: ')) #primeiro termo
r = int(input('Digite a razão da PA: ')) #razão
u = t + (10) * r #último termo
for m in range(t,u,r):
    print(m)

num=int(input('ingresa num: '))
diferencia_comun=int(input('ingresa el comun: '))

for progresion_aritetica in range(9):
    print(num)
    num=num+diferencia_comun
print(num)