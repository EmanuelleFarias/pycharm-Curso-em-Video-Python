#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

#for n in range(1,21):
    #print(n)

print(', '.join(str(i) for i in range(1, 21))) #str(i) pq o join só funciona com str, não funciona com inteiros


