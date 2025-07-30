'''6. Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos.
Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:

- 1,2,3,4 = voto para os respectivos candidatos;

- 5 = voto nulo;

- 6 = voto em branco;

Elabore um algoritmo que leia o código do candidado em um voto. Calcule e escreva:

- total de votos para cada candidato;

- total de votos nulos;

- total de votos em branco;

Como finalizador do conjunto de votos, tem-se o valor 0.'''



lista_votos = []
total_jo = 0
total_ze = 0
total_lu = 0
total_hu = 0
total_nu = 0
total_br = 0
total = 0
while True:
    print('⁀' * 43)
    print(f"{'PROGRAMINHA DE VOTOS':^60}")
    print('‿' * 43)

    print('''\nCandidatos:
        [1] Joãozinho
        [2] Zezinho
        [3] Luisinho
        [4] Huguinho
        [5] Nulo
        [6] Branco''')

    voto = int(input('\nEscolha seu candidato (para finalizar digite 0): '))
    if voto == 0:
        print('Programa finalizado.')
        break

    lista_votos.append(voto)
    if voto == 1:
        total_jo += 1
        total += 1
    elif voto == 2:
        total_ze += 1
        total += 1
    elif voto == 3:
        total_lu += 1
        total += 1
    elif voto == 4:
        total_hu += 1
        total += 1
    elif voto == 5:
        total_nu += 1
        total += 1
    else:
        total_br += 1
        total += 1
print('--'*30)
print(f"{'RESULTADO DA VOTAÇÃO':^60}")
print('--'*30)
print(f"Joãozinho: {total_jo} voto(s)")
print(f"Zezinho: {total_ze} voto(s)")
print(f"Luisinho: {total_lu} voto(s)")
print(f"Huguinho: {total_hu} voto(s)")
print(f"Nulo: {total_nu} voto(s)")
print(f"Branco: {total_br} voto(s)")
print(f"Total de votos: {total}.")


