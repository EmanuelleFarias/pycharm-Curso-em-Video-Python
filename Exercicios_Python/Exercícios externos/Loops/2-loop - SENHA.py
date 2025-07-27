#Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome = str(input('Informe seu nome: ')).strip().lower().split()
    senha = str(input('Digite sua senha: ')).strip().lower()

    if any(nome in senha for nome in nome): # SE ALGUM NOME TIVER NA SENHA NO INTERVALO DOS NOMES (CASO INFORME O NOME 'MARIA JOSE', POR EXEMPLO
        print('\nSenha inválida. O nome não pode estar contido na senha.\n')
    else:
        print('Senha validada com sucesso.')
        break