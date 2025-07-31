'''7. Escreva um algoritmo que calcule a média aritmética das 3 notas dos alunos de uma classe.
O algoritmo deverá ler, além das notas, o código do aluno e deverá ser encerrado quando o código for igual a zero.'''


print('⁀' * 43)
print(f"{'PROGRAMINHA DE NOTAS':^60}")
print('‿' * 43)

total = 0
cont = 0
while True:
    codigo = int(input('\nCódigo do Aluno (para encerrar digite 0): '))
    if codigo == 0:
        print('\nPrograma encerrado.\n')
        break
    for n in range(1, 4):
        nota = float(input(f'Nota {n}: '))
        total += nota
        cont += 1
    media = total/cont
    print(f'A média do aluno é {media:.2f}.')
