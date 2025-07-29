'''Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos'''

print('...'*20)
print(f"{'Programa de Turmas':^60}")
print('...'*20)

print('Vamos calcular a média de alunos por turma.\n')
turmas = int(input('Informe a quantidade de turmas → '))
total_alunos = 0
for a in range(1, turmas + 1):
    alunos = int(input('\nInforme a quantidade de alunos → '))
    total_alunos += alunos
    while alunos > 40:
        print('\nNúmero de alunos excede o máximo permitido. Por favor informe um valor menor que 40.')
        alunos = int(input('\nInforme a quantidade de alunos → '))
        total_alunos += alunos
media = total_alunos/turmas
print(f'\nA média de alunos por turma é de {media:.1f}.')