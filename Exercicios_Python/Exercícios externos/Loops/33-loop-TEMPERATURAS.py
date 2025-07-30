'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e
a maior temperaturas informadas, bem como a média das temperatura'''



print('...'*20)
print(f"{' 🌡 Temperaturas 🌡':^60}")
print('...'*20)
print('')
print('Informe quantas temperaturas quiser. Para finalizar digite 0.\n')
temp = ''
temps = []
cont = 1
total = 0
while True:
    temp = int(input(f'Informe a {cont}ª temperatura → '))
    if temp == 0:
        break
    total += temp
    cont += 1
    temps.append(temp)

media = total/cont
print(f'\nA menor temperatura informada foi {min(temps)}ºC.')
print(f'A maior temperatura informada foi {max(temps)}ºC.')
print(f'A média entre as temperaturas informadas foi {media:.1f}ºC.')