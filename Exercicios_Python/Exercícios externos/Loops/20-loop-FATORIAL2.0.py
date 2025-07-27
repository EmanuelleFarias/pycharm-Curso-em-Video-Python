#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
# limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    num = int(input('De qual número você quer o fatorial? '))
    print(f'{num}! = ', end='')

    fat = 1
    for n in range(num,0,-1):
        fat *= n
        print(f'{n}',  end=' x ' if n > 1 else ' = ')
    print(fat)

    mais = str(input('Deseja calcular o fatorial de outro número(S/N)? ')).strip().lower()
    while mais not in 'sn':
        print('Opção inválida. Digite S para Sim e N para Não.')
        mais = str(input('Deseja calcular o fatorial de outro número(S/N)? ')).strip().lower()
    if mais == 'n':
        print('Até a próxima!!!')
        break