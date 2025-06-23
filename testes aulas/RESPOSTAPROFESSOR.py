import random

numero_secreto = random.randint(1,50)
cont = 0
control = True

print("""
    ###################################  
            Bienvenidos !
    Vamos a jugar a Adivinar el Número
    ###################################
\n""")

while control and cont < 5:
    n = input("Ingrese un número entre 1 y 50: ")

    if n.isdigit():
        n = int(n)
        if n > 1 and n <= 50:
            if n > numero_secreto:
                print("El número secreto es MENOR")
                cont += 1
            elif n < numero_secreto:
                print("El número secreto es MAYOR")
                cont += 1
            else:
                print("Felicidades !! Adivinaste el número")
                control = False
        else:
            print("El número ingresado esta fuera del rango")
    else:
        print("En este Juego solo aceptamos Números enteros postivos")


if cont == 5:
    print(f"Pediste.. El número era: {numero_secreto}")