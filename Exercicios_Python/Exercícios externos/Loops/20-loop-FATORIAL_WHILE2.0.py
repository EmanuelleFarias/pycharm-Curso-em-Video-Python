
while True:
    num = int(input('O fatorial de → '))
    print(f'{num}! = ', end='')

    f = 1
    while num > 0:
        print(f'{num}', end=' x ' if num > 1 else ' \né... ')
        f *= num
        num -= 1
    print(f)

    mais = str(input('Deseja calcular o fatorial de outro número(S/N)? ')).strip().lower()
    while mais not in 'sn':
        print('Opção inválida. Digite S para Sim e N para Não.')
        mais = str(input('Deseja calcular o fatorial de outro número(S/N)? ')).strip().lower()
    if mais == 'n':
        print('Até a próxima!!!')
        break