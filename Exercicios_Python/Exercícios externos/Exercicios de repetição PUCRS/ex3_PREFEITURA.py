'''3. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando
dados sobre o salário e número de filhos. A prefeitura deseja saber:

a) média do salário da população;

b) média do número de filhos;

c) maior salário;

d) percentual de pessoas com salário até R$100,00.

O final da leitura de dados se dará com a entrada de um salário negativo. (Use o comando ENQUANTO-FAÇA)'''
import math

print('...'*20)
print(f"{' 🔎📈 PREFEITURA - Pesquisa Habitantes 🤱📊':^60}")
print('...'*20)


lista_salario = []
soma_salario = 0
soma_filhos = 0
cont_s = 0
cont_f = 0
cont_sb = 0
while True:
    print('⁀'*43)
    print('Para finalizar digite um salário negativo')
    print('‿' * 43)
    salario = float(input('Informe seu salário: '))
    if salario < 0:
        print('\nPrograma finalizado.\n')
        break
    if salario <= 5000:
        cont_sb += 1
    lista_salario.append(salario)
    soma_salario += salario
    cont_s += 1
    media_s = soma_salario/cont_s

    filhos = int(input('Informe a quantidade de filhos que você tem: '))
    soma_filhos += filhos
    cont_f += 1
    media_f = soma_filhos/cont_f
    print('')

    porcentagem = cont_sb*100/cont_s

print(f'\nA média de salários é de R${media_s:.2f}.')
print(f'A média de filhos é de {math.floor(media_f)}.')
print(f'O maior salário é R${max(lista_salario)}.')
print(f'A porcentagem de pessoas que recebem menos de R$5000.00 é {round(porcentagem)}%')
