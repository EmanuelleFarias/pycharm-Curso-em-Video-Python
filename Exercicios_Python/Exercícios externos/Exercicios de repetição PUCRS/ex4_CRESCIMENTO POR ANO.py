'''4. Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto
Zé tem 1,10 metro e cresce 3 centímetros por ano. Construa um
algoritmo que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.'''



print('...'*20)
print(f"{'CRESCIMENTO ANUAL':^60}")
print('...'*20)

chico = 1.50
ze = 1.10
tx_chico = 2
tx_ze = 3
anos = 0
while ze <= chico:
    chico += tx_chico/100
    ze += tx_ze/100
    anos += 1
print(f'\nSerão necessários {anos} anos para que Zé ultrapasse Chico.')
