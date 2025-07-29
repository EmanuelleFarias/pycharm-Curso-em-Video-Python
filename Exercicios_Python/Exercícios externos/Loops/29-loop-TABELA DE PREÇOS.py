'''O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém
o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente
do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os
preços de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50'''

print('...'*20)
print(f"{'Programa de Tabela de Preços':^60}")
print('...'*20)
print('')

tabela = ('1', '1.99',
          '2', '3.98',
          '3', '2.50',
          '4', '4.00',
          '5', '2.50',
          '6', '7.99',
          '7', '2.10',
          '8', '5.30',
          '9', '3.45',
          '10', '6.99',
          '11', '4.75',
          '12', '2.25',
          '13', '3.15',
          '14', '6.50',
          '15', '1.89',
          '16', '5.60',
          '17', '2.95',
          '18', '4.40',
          '19', '7.20',
          '20', '3.80',
          '21', '2.99',
          '22', '1.50',
          '23', '6.10',
          '24', '3.33',
          '25', '2.20',
          '26', '7.75',
          '27', '4.99',
          '28', '5.15',
          '29', '3.00',
          '30', '1.70',
          '31', '4.25',
          '32', '2.35',
          '33', '6.45',
          '34', '7.10',
          '35', '3.22',
          '36', '5.55',
          '37', '2.80',
          '38', '4.10',
          '39', '6.85',
          '40', '1.60',
          '41', '3.75',
          '42', '5.95',
          '43', '2.40',
          '44', '4.50',
          '45', '6.00',
          '46', '1.80',
          '47', '3.90',
          '48', '5.40',
          '49', '2.70',
          '50', '4.60')


for p in range(0, len(tabela), 2):
    nome = tabela[p]
    preco = tabela[p+1]
    print(f'{nome:•<50} R${preco:>7}')