'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''

palavras = ('palanka', 'kikita', 'negro', 'jojo', 'pequeneas', 'vitorias')

for palavra in palavras:
    print(f'\nAs vogais da palavra {palavra.upper()} são: ', end='')
    for letras in palavra:
        if letras in 'aeiou':
            print(letras, end=' ')