'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a
turma é jovem, adulta ou idosa, conforme a média calculada.'''

print('...'*20)
print(f"{'programa de media de grupos':^60}")
print('...'*20)

grupo = int(input('Qual o tamanho do seu grupo? '))

print('\nOk. Vamos começar!!!\n')


soma = 0
for i in range(1, grupo+1):
    idade = int(input(f'Digite a {i}ª idade: '))
    soma += idade

media = soma/grupo
if media <= 25:
    print('\nO grupo é majoritariamente jovem.')
elif media <= 60:
    print('\nO grupo é majoritariamente adulto.')
else:
    print('\nO grupo é majoritariamente idoso.')