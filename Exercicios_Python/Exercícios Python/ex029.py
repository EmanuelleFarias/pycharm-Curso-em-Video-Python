print('')
v = float(input('Qual a velocidade atual do veículo? '))
ve = v-80
print('')

if v<=80:
    print('Você está dentro do limite de segurança. Tenha uma boa viagem!!!')
else:
    print('--- ATENÇÃO ---')
    print('Você ultrapassou o limite de segurança que é 80km/h. Você está sendo multado em R${:.2f}.'.format(ve*7.00))
    print('Reduza a velocidade. Dirija com responsabilidade e tenha uma boa viagem.')