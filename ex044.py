#calculando o preço de acordo com a forma de pagamento
import emoji
print('{:~^40}'.format('🍯 LOJINHA DA MELZINHA 🐝'))
p = float(input('Preço do produto: R$'))
op1 = p - (p*10/100)
op2 = p - (p*5/100)
op3 = p /2
op4 = p + (p*20/100)
print('''Escolha a condição de pagamento:
[ 1 ] à vista/dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] em 3x ou mais no cartão''')
op = int(input('Opção escolhida: '))
if op ==1:
    print('Você escolheu a opção 1. Com o desconto de 10%, o produto fica por R${:.2f}.'.format(op1))
elif op == 2:
    print('Você escolheu a opção 2. Com o desconto de 5%, o produto fica por R${:.2f}.'.format(op2))
elif op == 3:
    print('Você escolheu a opção 3. O produto permanece com o preço normal de R${:.2f}, dividido em 2x de R${:.2f}.'.format(p, op3))
elif op == 4:
    qp = int(input('Em quantas parcelas você deseja dividir a compra? '))
    vp = op4 / qp
    print('Você escolheu a opção 4. O preço sofrerá um acréscimo de 20% de juros, totalizando R${:.2f}.\nDividido em {} parcelas de R${:.2f}'.format(op4, qp, vp))

else:
    print('\033[0;31mA opção escolhida não existe. Por favor digite uma opção válida.')
