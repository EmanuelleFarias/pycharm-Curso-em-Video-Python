'''Faça um programa que calcule o valor total investido por um colecionador
em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um'''
print('...'*20)
print(f"{'Programa de Media de CDs':^60}")
print('...'*20)


qtde_cds = int(input('Informe a quantidade de CDs: '))

total_investido = 0
for cd in range(1, qtde_cds + 1):
    valor_cds = float(input(f'Informe o valor do CD {cd}: '))
    total_investido += valor_cds

media = total_investido/qtde_cds
print(f'Foram gastos em média R${media:.2f} por CD.')