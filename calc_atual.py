'''calculadora Tkinter do vídeo https://www.youtube.com/watch?v=GEOSrYgq0E0'''

from tkinter import *
from math import *
#1
'''ventana = Tk()
ventana.mainloop() # qdo corre aqui abre a janelinha vazia da interface gráfica (mainloop tem que ir sempre no fim)'''
#continuando

ventana = Tk()
ventana.title('Calculadora') #nome da calculadora
ventana.geometry('400x550') #tamanho da janela
ventana.resizable(False, False) #aqui diz que a dimensão da janela pode ser modificada
ventana.configure(background = 'paleturquoise2') # posso escolher a cor no https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
# crear pantalla ('tela' da calculadora)
text_pantalla = StringVar() #parte 2 do video
Pantalla = Entry(ventana, font = ('arial', 20, 'bold'), width = 22, borderwidth = 10, background = 'bisque', textvariable = text_pantalla) #parte 2 do video acrescentar textvariable
#situar la pantalla OPCION 1 - PLACE
#Pantalla.place(x = 20, y = 60) - mais liberdade
#OPCION 2 - GRID
#Pantalla.grid(row = 0, column = 0, columnspan = 4) # se correr aqui vai ficar a tela grudada na esquerda e na parte superior da ventana
Pantalla.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 20) #padx e pady coloca espaço pra que nao fique como no comentário anterior
#botoes
color_boton = 'bisque'
ancho_boton = 5
alto_boton = 2
fonte = 'arial', 13, 'bold'
operador = '' #parte 2 do video

#funciones - parte 2 do video
def clear():
    global operador
    operador = ''
    text_pantalla.set('0')

def click(b):
    global operador
    operador += str(b)
    text_pantalla.set(operador)

def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = 'ERROR'
    text_pantalla.set(r)

def raiz_quadrada():
    global operador
    valor = float(eval(operador))  # calcula o valor da expressão digitada
    resultado = sqrt(valor)        # calcula a raiz quadrada
    operador = str(resultado)

def porcentagem():
    global operador
    if operador.strip():
        valor = float(eval(operador))
        resultado = valor / 100
        operador = str(resultado)
        text_pantalla.set(operador)

#botones de la primera fila # NA PARTE 2 DO VIDEO MANDA ACRESCENTAR O COMMAND em todos os botoes de numero
BotonExp = Button(ventana, text = 'exp', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                  command=lambda:click('exp')).grid(row = 1, column = 0, padx = 10,pady = 10, sticky="nsew")
BotonParIz = Button(ventana, text = '(', font= fonte,bg = color_boton, width = ancho_boton, height = alto_boton,
                    command=lambda:click('(')).grid(row = 1, column = 1,padx = 10, pady = 10, sticky="nsew")
BotonParDer = Button(ventana, text = ')', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                     command=lambda:click(')')).grid(row = 1, column = 2,padx = 10, pady = 10, sticky="nsew")
BotonClear = Button(ventana, text = 'C', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                    command=lambda:clear()).grid(row = 1, column = 3, padx = 10, pady = 10, sticky="nsew")
#botones de la segunda fila

Boton7 = Button(ventana, text = '7', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(7)).grid(row = 2, column = 0,padx = 10, pady = 10, sticky="nsew")
Boton8 = Button(ventana, text = '8', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(8)).grid(row = 2, column = 1,padx = 10, pady = 10, sticky="nsew")
Boton9 = Button(ventana, text = '9', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(9)).grid(row = 2, column = 2, padx = 10,pady = 10, sticky="nsew")
BotonDiv = Button(ventana, text = '÷', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                  command=lambda:click('/')).grid(row = 2, column = 3,padx = 10, pady = 10, sticky="nsew")

#botones de la tercera fila
Boton4 = Button(ventana, text = '4', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(4)).grid(row = 3, column = 0, padx = 10,pady = 10, sticky="nsew")
Boton5 = Button(ventana, text = '5', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(5)).grid(row = 3, column = 1,padx = 10, pady = 10, sticky="nsew")
Boton6 = Button(ventana, text = '6', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(6)).grid(row = 3, column = 2, padx = 10,pady = 10, sticky="nsew")
BotonMult = Button(ventana, text = 'x', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                   command=lambda:click('*')).grid(row = 3, column = 3, padx = 10,pady = 10, sticky="nsew")


#botones de la cuarta fila
Boton1 = Button(ventana, text = '1', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(1)).grid(row = 4, column = 0, padx = 10,pady = 10, sticky="nsew")
Boton2 = Button(ventana, text = '2', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(2)).grid(row = 4, column = 1, padx = 10,pady = 10, sticky="nsew")
Boton3 = Button(ventana, text = '3', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(3)).grid(row = 4, column = 2, padx = 10,pady = 10, sticky="nsew")
BotonResta = Button(ventana, text = '-', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                    command=lambda:click('-')).grid(row = 4, column = 3, padx = 10,pady = 10, sticky="nsew")


#botones de la quinta fila
Boton0 = Button(ventana, text = '0', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                command=lambda:click(0)).grid(row = 5, column = 0, padx = 10,pady = 10, sticky="nsew")
Boton00 = Button(ventana, text = '00', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                 command=lambda:click('00')).grid(row = 5, column = 1, padx = 10,pady = 10, sticky="nsew")
BotonPunto = Button(ventana, text = '.', font= fonte, bg = 'sienna3', width = ancho_boton, height = alto_boton,
                    command=lambda:click('.')).grid(row = 5, column = 2, padx = 10,pady = 10, sticky="nsew")
BotonSuma = Button(ventana, text = '+', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                   command=lambda:click('+')).grid(row = 5, column = 3, padx = 10,pady = 10, sticky="nsew")

#botones de la sexta fila
BotonRaiz = Button(ventana, text = '√', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                   command=raiz_quadrada).grid(row = 6, column = 0, padx = 10,pady = 10, sticky="nsew")
BotonMod = Button(ventana, text = '%', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                  command = lambda:porcentagem()).grid(row = 6, column = 1, padx = 10,pady = 10, sticky="nsew")
BotonIgual= Button(ventana, text = '=', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,
                   command=lambda:resultado()).grid(row = 6, column = 2, columnspan = 2, padx = 10,pady = 10, sticky="nsew")


#incio video parte 2
# declara variaveis lá em cima(operador e text_pantalla)
#acrescenta na Pantalla o argumento textvariable = text_pantalla
ventana.mainloop()
