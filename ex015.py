km = float(input('quantidade de km rodados:'))
d = int(input('quantidade de dias de aluguel:'))
dk = km*0.15
dd = d*60
ct = dk+dd
print('O veículo foi alugado por {} dias sob o valor de R$60.00/dia, totalizando R${:.2f}. \nForam rodados {}km, sendo que cada km custa R$0.15, totalizando R${:.2f}. \nO custo total referente ao período e km percorridos pelo automóvel é de R${:.2f}.'.format(d,dd,km,dk,ct))
