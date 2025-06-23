# calculando imc
p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p/a**2
print('O IMC dessa pessoa é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Ela está \033[7;33mABAIXO DO PESO\033[m.')
elif 18.5 <= imc < 25:
    print('Ela está no \033[7;35mPESO IDEAL\033[m.')
elif imc < 30:
    print('Ela está com \033[7;34mSOBREPESO\033[m.')
elif imc < 40:
    print('Ela está com \033[7;31mOBESIDADE\033[m.')
else:
    print('Ela está com \033[7;30;47mOBESIDADE MÓRBIDA\033[m.')
