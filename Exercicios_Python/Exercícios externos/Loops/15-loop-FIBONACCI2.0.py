qtde = int(input('🔢 Quantos números da sequência? '))
seq = [1, 1]

while qtde > len(seq):
    for n in range(len(seq), qtde):
        seguinte = seq[n - 1] + seq[n - 2]
        seq.append(seguinte)
print(', '.join(str(i) for i in seq))

while True:
    mais = int(input('➕ Quantos termos quer adicionar (para finalizar digite 0)? '))
    if mais == 0:
        break
    qtde += mais
    while qtde > len(seq):
        seguinte = seq[-1] + seq[-2]
        seq.append(seguinte)
    print(', '.join(str(i) for i in seq))

print('✅ Finalizado.')