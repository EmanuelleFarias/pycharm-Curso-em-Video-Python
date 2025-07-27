#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

qtde = int(input('Quantos números da sequência? '))

seq = [1,1]
for n in range(2, qtde):
    seguinte = seq[n-1] + seq[n-2] #(seq[n-1] = último numero da lista seq) + (seq[n-2] = penúltimo número da lista seq)
    seq.append(seguinte)
print(', '.join(str(i) for i in seq))


