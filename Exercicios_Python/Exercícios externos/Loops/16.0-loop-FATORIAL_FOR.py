#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('De qual número você quer o fatorial? '))

print(f'{num}! = ', end='')

fat = 1
for n in range(num,0,-1):
    fat *= n
    print(f'{n}',  end=' x ' if n > 1 else ' = ')
print(fat)


