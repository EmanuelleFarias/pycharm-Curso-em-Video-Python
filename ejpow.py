'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = input('Informe seu nome: ').strip()
idade = ' '
salario = ' '
sexo = ' '
est_civil = ' '

while len(nome) < 3:
    print('Seu nome precisa ter no mínimo 3 caracteres.')
    nome = input('Informe seu nome: ').strip()
print('Nome VALIDADO')
idade = int(input('Informe sua idade: '))

while idade < 0 or idade > 150:
    print('A idade precisa ser entre 0 e 150 anos.')
    idade = int(input('Informe sua idade: '))
print('Idade VALIDADA')
salario = float(input('Informe seu salário: '))

while salario <= 0:
    print('Valor inválido. Informe um valor maior que zero.')
    salario = float(input('Informe seu salário: '))
print('Salário VALIDADO')
sexo = input('Informe seu sexo (M/F): ').strip().lower()

while sexo not in 'mf':
    print('Por favor, utilize M para Masculino ou F para Feminino.')
    sexo = input('Informe seu sexo (M/F): ').strip().lower()
print('Sexo VALIDADO')
estado_civil = input('Informe seu estado civil (S/C/D/V): ').strip().lower()

while estado_civil not in 'scdv':
    print('Por favor, utilize S para Solteira(o), C para Casada(o), D para Divorciada(o),V para Viúva(o)')
    estado_civil = input('Informe seu estado civil (S/C/D/V): ').strip().lower()
print('Estado civil VALIDADO')
print('\nInformações registradas.')

