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
    print('Voto registrado.')
    if voto == 0:
        print('Programa finalizado.')
        break

    lista_votos.append(voto)


print('--'*30)
print(f"{'RESULTADO DA VOTAÇÃO':^60}")
print('--'*30)
print(f"Joãozinho: {lista_votos.count(1)} voto(s)")
print(f"Zezinho: {lista_votos.count(2)} voto(s)")
print(f"Luisinho: {lista_votos.count(3)} voto(s)")
print(f"Huguinho: {lista_votos.count(4)} voto(s)")
print(f"Nulo: {lista_votos.count(5)} voto(s)")
print(f"Branco: {lista_votos.count(6)} voto(s)")
print(f"Total de votos: {len(lista_votos)}.")




