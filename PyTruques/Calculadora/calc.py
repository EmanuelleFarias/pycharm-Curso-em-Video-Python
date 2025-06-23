from time import sleep # só é adicionar opções e a calculadora tá feita
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
opção1 = num1 + num2
opção2 = num1 * num2
opção3 = max(num1, num2)
opção = 0
while opção != 5:
    print(''' Escolha uma opção:
         [ 1 ] Somar
         [ 2 ] Multiplicar
         [ 3 ] Maior
         [ 4 ] Novos números
         [ 5 ] Sair do programa''')
    print('')
    opção = int(input('>>> Qual é a sua opção? '))
    print('')
    if opção == 1:
        print('A soma dos valores é {}.'.format(opção1))
        sleep(2)
        print('')
    elif opção == 2:
        print('O produto dos dois números é {}.'.format(opção2))
        sleep(2)
        print('')
    elif opção == 3:
        if num2 != num1:
            print('O maior entre os dois números digitados é {}.'.format(opção3))
            sleep(2)
            print('')
        else:
            print('Os números são iguais.')
            sleep(2)
            print('')
    elif opção == 4:
        print('Informe os números novamente.')
        sleep(2)
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um número: '))
    elif opção == 5:
        print('Você está saindo do programa, mas espero te ver em breve!!!')
        sleep(2)
    else:
        print('Opção inválida. Escolha entre 1 e 5.')
        sleep(2)





