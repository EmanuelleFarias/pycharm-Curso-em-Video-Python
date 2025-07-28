'''Faça um programa que calcule o mostre a média aritmética de N notas.'''


print('...'*20)
print(f"{'programa de média de notas':^60}")
print('...'*20)

qtde = int(input('Quantas notas deseja informar? '))

notas = []
soma = 0
cont = 0

for n in range(1, qtde + 1):
    nota = float(input(f"Nota {n} → "))
    notas.append(nota)
    soma += nota
    cont += 1
    media = soma / cont
print(f"{media:.1f}")