'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.'''
listagem = ('lápis',1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo',25,
            'canetas', 22.30,
            'réguas', 13)
print('--'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--'*20)
for pos in range(0,len(listagem),2):
    print(f'{listagem[pos]:.<30}', end='')
    print(f'R${listagem[pos+1]:>7.2f}')
print('--'*20)