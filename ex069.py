'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:A) quantas pessoas tem mais de 18 anos.
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''



totalm18 = 0
totalhomem = 0
totalmulher = 0
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'mf':
        s = str(input('Sexo (M/F): ')).strip().lower()
    if i > 18:
        totalm18 += 1
    if s == 'm':
        totalhomem += 1
    if s == 'f' and i < 20:
        totalmulher += 1
    r = ' '
    while r not in 'sn':
        r = str(input('Quer continuar? (S/N): ')).strip().lower()
    if r == 'n':
        break

print(f'Ao todo, foram cadastradas {totalm18} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {totalhomem} homens.')
print(f'O total de mulheres menores de 20 anos é {totalmulher}.')