
import math


total_salario = 0
total_filhos = 0
num_pessoas = 0
maior_salario = 0
ate_5000 = 0


salario = float(input("Digite o salário (valor negativo para encerrar): "))

while salario >= 0:
    filhos = int(input("Digite o número de filhos: "))

    total_salario += salario
    total_filhos += filhos
    num_pessoas += 1

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 5000:
        ate_5000 += 1

    salario = float(input("Digite o salário (valor negativo para encerrar): "))


if num_pessoas > 0:
    media_salario = total_salario / num_pessoas
    media_filhos = total_filhos / num_pessoas
    percentual_ate_5000 = (ate_5000 / num_pessoas) * 100

    print(f'A média de salário da população é R${media_salario:.2f}.')
    print(f'A média de filhos é de {math.floor(media_filhos)}.')
    print(f'O maior salário informado foi R${maior_salario:.2f}.')
    print(f'{percentual_ate_5000:.1f}% das pessoas recebem até R$5000,00.')
else:
    print("Nenhum dado foi coletado.")