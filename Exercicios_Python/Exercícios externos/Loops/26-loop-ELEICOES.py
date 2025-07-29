'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''


print('...'*20)
print(f"{'programa de eleições':^60}")
print('...'*20)

num_eleitores = int(input('\nInforme o número total de eleitores: '))
print(''' \nCandidatos 
    [1] Joãozinho
    [2] Zezinho
    [3] Luisinho''')

opcao_1 = 0
opcao_2 = 0
opcao_3 = 0

for e in range(1, num_eleitores+1):
    voto = int(input('\nEm quem deseja votar? '))

    if voto == 1:
        opcao_1 += 1
        print('VOTO REGISTRADO')

    elif voto == 2:
        opcao_2 += 1
        print('VOTO REGISTRADO')

    else:
        opcao_3 += 1
        print('VOTO REGISTRADO\n')

if opcao_1 > opcao_2 and opcao_1 > opcao_3:
    print(f'\nO candidato Joãozinho venceu com {opcao_1} votos.')
    print(f'\nO candidato Zezinho recebeu {opcao_2} votos.')
    print(f'O candidato Luisinho recebeu {opcao_3} votos.')
elif opcao_2 > opcao_1 and opcao_2 > opcao_3:
    print(f'\nO candidato Zezinho venceu com {opcao_2} votos.')
    print(f'\nO candidato Joãozinho recebeu {opcao_1} votos.')
    print(f'O candidato Luisinho recebeu {opcao_3} votos.')
elif opcao_3 > opcao_1 and opcao_3 > opcao_2:
    print(f'\nO candidato Luisinho venceu com  {opcao_3} votos.')
    print(f'\nO candidato Joãozinho recebeu {opcao_1} votos.')
    print(f'O candidato Zezinho recebeu {opcao_2} votos.')
elif opcao_1 == opcao_2 and opcao_2 == opcao_3:
    print('EMPATE')



