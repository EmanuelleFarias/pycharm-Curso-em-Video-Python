'''3. Faça um programa, utilizando while e listas, que permita o usuário escrever o nome de cinco pessoas
e os mostre na tela.'''

nomes = []
cont = 0
while cont < 5:
    nome = input('digite um nome: ').strip()
    nomes.append(nome)
    cont += 1
print(nomes)

