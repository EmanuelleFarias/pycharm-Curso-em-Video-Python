'''s = 0  # Contador de soma
for num in range(1, 501):  # de 1 até 500
    if num % 2 != 0:  # Ímpares
        if num % 3 == 0:  # Ímpares múltiplos de 3
            s += num  # soma = soma + num
print("A soma dos múltiplos é: {}.".format(s))'''

# Validação do nome
nome = input('Informe seu nome: ').strip()
while len(nome) <= 3:
    print('Seu nome precisa ter mais de 3 caracteres.')
    nome = input('Informe seu nome: ').strip()
print('✅ Nome validado.')

# Validação da idade
while True:
    try:
        idade = int(input('Informe sua idade (entre 0 e 150): '))
        if 0 <= idade <= 150:
            print('✅ Idade validada.')
            break
        else:
            print('A idade precisa estar entre 0 e 150 anos.')
    except ValueError:
        print('⚠️ Digite um número inteiro válido para idade.')

# Validação do salário
while True:
    try:
        salario = float(input('Informe seu salário (maior que zero): '))
        if salario > 0:
            print('✅ Salário validado.')
            break
        else:
            print('O salário precisa ser maior que zero.')
    except ValueError:
        print('⚠️ Digite um número válido para salário.')

# Validação do sexo
while True:
    sexo = input('Informe seu sexo (M/F): ').strip().lower()
    if sexo in ('m', 'f'):
        print('✅ Sexo validado.')
        break
    else:
        print('Valor inválido. Digite apenas M ou F.')

# Validação do estado civil
opcoes_civil = ('s', 'c', 'v', 'd')  # solteiro, casado, viúvo, divorciado
while True:
    est_civil = input('Informe seu estado civil (S/C/V/D): ').strip().lower()
    if est_civil in opcoes_civil:
        print('✅ Estado civil validado.')
        break
    else:
        print('Valor inválido. Use apenas S, C, V ou D.')