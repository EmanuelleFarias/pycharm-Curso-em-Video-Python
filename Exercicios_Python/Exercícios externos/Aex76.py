'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência

No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''
print('⏔' *29)
print(f"{'Lojinha da Melzinha':^43}")
print('⏔' *29)
print('_'*43)
produtos = ('Lápis', 1.00,
         'Caneta', 1.50,
         'Borracha', 0.70,
         'Mesa', 1000.00,
         'Teclado', 600.00,
         'Monitor', 3000.00,
         'Caderno', 50.00,
         'Mouse', 60.00)

for p in range(0, len(produtos),2):
    nome = produtos[p]
    preço = produtos[p+1]
    linha = f"{nome + ' ':•<30} R$ {preço:>7.2f}"
    print(linha.center(43))

print('—'*43)
print('⏔'*29)