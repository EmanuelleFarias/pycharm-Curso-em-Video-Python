#for i in range(11):
   # print('2 x', i, '=', i*2) #SUBSTITUI O 2 PELOS NUMEROS QUE QUER DA FAZER A TABUADA


num = int(input('Digite um número: '))

for i in range(1,11):
    mult = num * i
    print('{} x {} = {}'.format(num,i,mult))