'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução
, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
num = int(input('Digite um número inteiro: '))
lista = [num]
cont = 1
soma = num
while num > 0:
    print()
    p = str(input('Quer continuar digitando? (S/N):')).strip().upper()
    if p == 'S':
        num = int(input('Digite um número inteiro: '))
        lista += [num]
        soma += num
        cont += 1
    elif p == 'N':
        print('ok')
        print('Você digitou {} números.'.format(cont))
        print('O maior número digitado foi {}.'.format(max(lista)))
        print('O menor número digitado foi {}.'.format(min(lista)))
        print('A soma entre todos os números digitados é {}.'.format(soma))
        print('A média entre todos os números digitados é {:.2f}.'.format(soma/cont))
        break
    else:
        print('\033[1;31mOpção inválida. Digite S para SIM ou N para NÃO.\033[m')
print()

#outro jeito (aula)

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:# se o primeiro número...
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
            if núm < menor:
                menor = núm
    resp = str(input('Quer continuar? (S/N)')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))

