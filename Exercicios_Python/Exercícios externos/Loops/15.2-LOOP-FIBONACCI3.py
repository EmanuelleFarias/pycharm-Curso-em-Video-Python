#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

seq = [1,1]

while True:
    seguinte = seq[-1] + seq[-2] #(seq[-1] = último numero da lista seq) + (seq[-2] = penúltimo número da lista seq)

    if seguinte < 500:
        seq.append(seguinte)
    else:
        print('O próximo termo é maior que 500. Programa finalizado.')
        break

print(', '.join(str(i) for i in seq))
