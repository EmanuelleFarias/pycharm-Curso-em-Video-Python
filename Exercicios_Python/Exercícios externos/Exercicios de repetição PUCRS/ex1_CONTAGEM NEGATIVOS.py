'''1. Escrever um algoritmo que lê 5 valores para a, um de cada vez,
e conta quantos destes valores são negativos, escrevendo esta informação.'''

print('...'*20)
print(f"{'programa de contagem de negativos':^60}")
print('...'*20)

cont = 0
for v in range(1,6):
    a = int(input('Digite um valor: '))
    if a < 0:
        cont += 1
print(f"\nForam digitados {cont} números negativos.")
