'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''


print('⏔'*40)
print(f"{'CADASTRO DE USUÁRIOS':^55}")
print('⏔'*40)

nome = str(input('Informe seu nome: ')).strip().lower()
while len(nome) < 3 or not nome.isalpha():
    print('Nome inválido. Informe um nome com mais de 3 letras.')
    nome = str(input('Informe seu nome: '))
print('\nNOME VALIDADO\n')

idade = int(input('Informe sua idade (entre 0 e 150 anos): '))
while idade < 0 or idade >150:
    print('Idade inválida. Informe uma idade entre 0 e 150 anos.')
    idade = int(input('Informe sua idade (entre 0 e 150 anos): '))
print('\nIDADE VALIDADA\n')

salario = float(input('Informe seu salário: '))
while salario < 0:
    print('Valor inválido. Digite um valor maior que zero.')
    salario = float(input('Informe seu salário: '))
print('\nSALÁRIO VALIDADO\n')

sexo = str(input('Informe seu sexo (M/F): ')).strip().lower()
while sexo not in 'mf':
    print('Opção inválida. Digite M para Masculino e F para Feminino.')
    sexo = str(input('Informe seu sexo (M/F): ')).strip().lower()
print('\nSEXO VALIDADO\n')

estado_civil = str(input('Informe seu estado civil (S/C/D/V): ')).strip().lower()
while estado_civil not in 'scdv':
    print('Opção inválida. Digite S para Solteira, C para Casada, D para Divorciada ou V para Viúva.')
    estado_civil = str(input('Informe seu estado civil (S/C/D/V): ')).strip().lower()
print('\nESTADO CIVIL VALIDADO\n')
print('Cadastro realizado com sucesso.')

print('\n CADASTRO COMPLETO')
print(f"{'Nome:':<15}{nome}")
print(f"{'Idade:':<15}{idade} anos")
print(f"{'Salário:':<15}R$ {salario:.2f}")
print(f"{'Sexo:':<15}{'Masculino' if sexo == 'm' else 'Feminino'}")
estado_civil_map = {'s': 'Solteiro(a)', 'c': 'Casado(a)', 'd': 'Divorciado(a)', 'v': 'Viúvo(a)'}
print(f"{'Estado Civil:':<15}{estado_civil_map[estado_civil]}")
print('_'*60)