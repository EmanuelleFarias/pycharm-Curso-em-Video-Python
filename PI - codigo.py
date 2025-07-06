import random
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
        print('''Seleccione una opción:

[1] Alta ticket
[2] Leer ticket
[3] Salir
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
    menu_principal()