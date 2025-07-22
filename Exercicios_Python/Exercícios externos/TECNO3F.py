def dibujar_rectangulo(filas, columnas):
    for _ in range(filas):
        print('*' * columnas)

# Solicitar al usuario los valores
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Llamar a la función
dibujar_rectangulo(filas, columnas)




