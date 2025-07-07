import json
import random
import os

ARQUIVO = "tickets.json"

# Carregar tickets salvos
def carregar_tickets():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Salvar tickets
def salvar_tickets(tickets):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=4, ensure_ascii=False)

# Mostrar ticket formatado
def exibir_ticket(ticket):
    print("+" + "-"*60 + "+")
    print(f"| Nome    : {ticket['nome']:<48}|")
    print(f"| Setor   : {ticket['setor']:<48}|")
    print(f"| Assunto : {ticket['assunto']:<48}|")
    print(f"| Nº Ticket: {ticket['numero']:<47}|")
    print("| Mensagem:".ljust(61) + "|")
    mensagem = ticket["mensagem"]
    linhas = [mensagem[i:i+56] for i in range(0, len(mensagem), 56)]
    for linha in linhas:
        print(f"|   {linha:<56}|")
    print("+" + "-"*60 + "+")
    print("🔔 Guarde o número do seu ticket.")

# Criar ticket
def alta_ticket(tickets):
    while True:
        print("\n📨 Gerar novo ticket")
        nome = input("Nome: ")
        setor = input("Setor: ")
        assunto = input("Assunto: ")
        mensagem = input("Mensagem: ")
        numero = str(random.randint(1000, 9999))

        ticket = {
            "nome": nome,
            "setor": setor,
            "assunto": assunto,
            "mensagem": mensagem,
            "numero": numero
        }

        tickets[numero] = ticket
        salvar_tickets(tickets)
        print("\n🧾 Ticket criado com sucesso!")
        exibir_ticket(ticket)

        novo = input("\nDeseja criar outro ticket? (S/N): ").strip().lower()
        if novo != "s":
            break

# Ler ticket
def ler_ticket(tickets):
    while True:
        print("\n🔍 Ler ticket existente")
        numero = input("Digite o número do ticket: ").strip()
        ticket = tickets.get(numero)
        if ticket:
            exibir_ticket(ticket)
        else:
            print("❌ Ticket não encontrado.")
        outro = input("\nDeseja ler outro ticket? (S/N): ").strip().lower()
        if outro != "s":
            break

# Menu principal
def menu():
    tickets = carregar_tickets()
    while True:
        print("\n" + "="*60)
        print("{:^60}".format("🎫 SISTEMA DE TICKETS"))
        print("="*60)
        print("1 - Gerar novo ticket")
        print("2 - Ler ticket existente")
        print("3 - Sair")
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            alta_ticket(tickets)
        elif opcao == "2":
            ler_ticket(tickets)
        elif opcao == "3":
            confirmar = input("Deseja mesmo sair? (S/N): ").strip().lower()
            if confirmar == "s":
                print("👋 Encerrando o sistema...")
                break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

# Execução
if __name__ == "__main__":
    menu()








'''import random
import os
import textwrap

# Diccionario para almacenar tickets
base_tickets = {}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_ticket(ticket):
    mensaje = textwrap.fill(ticket["problema"], width=58)
    print('\n' + '═'*64)
    print(f'╔{"═"*62}╗')
    print(f'║{" TICKET DE SOPORTE ":^62}║')
    print(f'╚{"═"*62}╝')
    print(f'║  Nombre: {ticket["nombre"]:<52}║')
    print(f'║  Nº Ticket: {ticket["numero"]:<49}║')
    print(f'║  Sector: {ticket["sector"]:<52}║')
    print(f'║  Asunto: {ticket["asunto"]:<52}║')
    print(f'║{"":<62}║')
    print(f'║  Problema:'.ljust(63) + '║')
    for linea in mensaje.split('\n'):
        print(f'║    {linea:<58}║')
    print(f'╚{"═"*62}╝')

def alta_ticket():
    while True:
        limpiar_pantalla()
        print('🔹 Alta de nuevo ticket 🔹\n')
        nombre = input('Nombre: ')
        sector = input('Sector: ')
        asunto = input('Asunto: ')
        problema = input('Describa el problema: ')
        numero = random.randint(1000, 9999)

        ticket = {
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "problema": problema,
            "numero": numero
        }

        base_tickets[numero] = ticket
        mostrar_ticket(ticket)
        print('\n🔔 Recuerde su número de ticket.')

        repetir = input('\n¿Desea crear otro ticket? (S/N): ').strip().lower()
        while repetir not in ('s', 'n'):
            repetir = input('Ingrese S para sí o N para no: ').strip().lower()
        if repetir == 'n':
            break

def leer_ticket():
    while True:
        limpiar_pantalla()
        print('📖 Lectura de ticket\n')
        try:
            numero = int(input('Ingrese el número de ticket: '))
            if numero in base_tickets:
                mostrar_ticket(base_tickets[numero])
            else:
                print('\n❌ Ticket no encontrado.')
        except ValueError:
            print('\n⚠️ Ingrese un número válido.')

        repetir = input('\n¿Desea leer otro ticket? (S/N): ').strip().lower()
        while repetir not in ('s', 'n'):
            repetir = input('Ingrese S para sí o N para no: ').strip().lower()
        if repetir == 'n':
            break

def salir():
    confirmacion = input('\n¿Está seguro que desea salir? (S/N): ').strip().lower()
    while confirmacion not in ('s', 'n'):
        confirmacion = input('Ingrese S para sí o N para no: ').strip().lower()
    return confirmacion == 's'

def menu_principal():
    while True:
        limpiar_pantalla()
        print('=='*30)
        print('{:^60}'.format('🎫 SISTEMA DE GESTIÓN DE TICKETS'))
        print('=='*30)
        print('''#Seleccione una opción:

#[1] Alta ticket
#[2] Leer ticket
#[3] Salir
''')
        opcion = input('Opción seleccionada: ').strip()
        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            if salir():
                print('\n👋 Gracias por usar el sistema. ¡Hasta luego!\n')
                break
        else:
            print('\n⚠️ Opción no válida.')
            input('Presione Enter para continuar...')

if __name__ == "__main__":
    menu_principal()'''