'''
from tkinter import *
from math import *

ventana = Tk()
ventana.title('Calculadora')
ventana.geometry('400x550')
ventana.resizable(False, False)
ventana.configure(background = 'paleturquoise2')
text_pantalla = StringVar()
Pantalla = Entry(ventana, font = ('arial', 20, 'bold'), width = 22, borderwidth = 10, relief = 'sunken', background = 'bisque', textvariable = text_pantalla) #parte 2 do video acrescentar textvariable

Pantalla.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 20, sticky='nsew')

color_boton = 'bisque'
ancho_boton = 5
alto_boton = 1
fonte = 'arial', 14, 'bold'
bordas = 'groove'
operador = ''

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
        r = str(eval(operador, {"__builtins__": None}, {"sqrt": sqrt, "log": log, "exp": exp, "factorial": factorial}))
    except:
        r = 'ERROR'
    text_pantalla.set(r)

def raiz_quadrada():
    global operador
    valor = float(eval(operador))
    resultado = sqrt(valor)
    operador = str(resultado)

def porcentagem():
    global operador
    if operador.strip():
        valor = float(eval(operador))
        resultado = valor / 100
        operador = str(resultado)
        text_pantalla.set(operador)

def apagar_ultimo():
    global operador
    operador = operador[:-1]
    text_pantalla.set(operador)

#botones de la primera fila
BotonExp = Button(ventana, text = 'exp', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                  command=lambda:click('exp')).grid(row = 1, column = 0, padx = 10,pady = 10, sticky="nsew")
BotonParIz = Button(ventana, text = '(', font= fonte,bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                    command=lambda:click('(')).grid(row = 1, column = 1,padx = 10, pady = 10, sticky="nsew")
BotonParDer = Button(ventana, text = ')', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                     command=lambda:click(')')).grid(row = 1, column = 2,padx = 10, pady = 10, sticky="nsew")
BotonClear = Button(ventana, text = 'C', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                    command=lambda:clear()).grid(row = 1, column = 3, padx = 10, pady = 10, sticky="nsew")

#botones de la segunda fila
BotonRaiz = Button(ventana, text = '√', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                   command=raiz_quadrada).grid(row = 2, column = 0, padx = 10,pady = 10, sticky="nsew")
BotonMod = Button(ventana, text = '%', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                  command = lambda:porcentagem()).grid(row = 2, column = 1, padx = 10,pady = 10, sticky="nsew")
BotonLog = Button(ventana, text = 'log', font=('arial',14,'bold'), bg=color_boton, width=ancho_boton, height=alto_boton, bd=5, relief=bordas,
                  command=lambda:click('log(')).grid(row = 2, column = 2, padx=10, pady=10, sticky="nsew")
BotonFact = Button(ventana, text = '!', font=fonte, bg=color_boton, width=ancho_boton, height=alto_boton, bd=5, relief=bordas,
                   command=lambda:click('factorial(')).grid(row = 2, column = 3, padx=10, pady=10, sticky="nsew")

#botones de la tercera fila
Boton7 = Button(ventana, text = '7', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(7)).grid(row = 3, column = 0,padx = 10, pady = 10, sticky="nsew")
Boton8 = Button(ventana, text = '8', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(8)).grid(row = 3, column = 1,padx = 10, pady = 10, sticky="nsew")
Boton9 = Button(ventana, text = '9', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(9)).grid(row = 3, column = 2, padx = 10,pady = 10, sticky="nsew")
BotonDiv = Button(ventana, text = '÷', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                  command=lambda:click('/')).grid(row = 3, column = 3,padx = 10, pady = 10, sticky="nsew")

#botones de la quarta fila
Boton4 = Button(ventana, text = '4', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(4)).grid(row = 4, column = 0, padx = 10,pady = 10, sticky="nsew")
Boton5 = Button(ventana, text = '5', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(5)).grid(row = 4, column = 1,padx = 10, pady = 10, sticky="nsew")
Boton6 = Button(ventana, text = '6', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(6)).grid(row = 4, column = 2, padx = 10,pady = 10, sticky="nsew")
BotonMult = Button(ventana, text = 'x', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                   command=lambda:click('*')).grid(row = 4, column = 3, padx = 10,pady = 10, sticky="nsew")


#botones de la quinta fila
Boton1 = Button(ventana, text = '1', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(1)).grid(row = 5, column = 0, padx = 10,pady = 10, sticky="nsew")
Boton2 = Button(ventana, text = '2', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(2)).grid(row = 5, column = 1, padx = 10,pady = 10, sticky="nsew")
Boton3 = Button(ventana, text = '3', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(3)).grid(row = 5, column = 2, padx = 10,pady = 10, sticky="nsew")
BotonResta = Button(ventana, text = '-', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                    command=lambda:click('-')).grid(row = 5, column = 3, padx = 10,pady = 10, sticky="nsew")


#botones de la sexta fila
Boton0 = Button(ventana, text = '0', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                command=lambda:click(0)).grid(row = 6, column = 0, padx = 10,pady = 10, sticky="nsew")
Boton00 = Button(ventana, text = '00', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                 command=lambda:click('00')).grid(row = 6, column = 1, padx = 10,pady = 10, sticky="nsew")
BotonPunto = Button(ventana, text = '.', font= fonte, bg = 'salmon1', width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                    command=lambda:click('.')).grid(row = 6, column = 2, padx = 10,pady = 10, sticky="nsew")
BotonSuma = Button(ventana, text = '+', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                   command=lambda:click('+')).grid(row = 6, column = 3, padx = 10,pady = 10, sticky="nsew")

#botones de la setima fila
BotonApUl= Button(ventana, text = '◄', font=fonte, bg = 'salmon1', width=ancho_boton, height=alto_boton, bd=5, relief=bordas,
                   command=lambda:apagar_ultimo()).grid(row = 7, column = 0, columnspan=2, padx=10, pady=10, sticky="nsew")
BotonIgual= Button(ventana, text = '=', font= fonte, bg = color_boton, width = ancho_boton, height = alto_boton,bd=5,relief=bordas,
                   command=lambda:resultado()).grid(row = 7, column = 2, columnspan = 2, padx = 10,pady = 10, sticky="nsew")


ventana.mainloop()
'''

from tkinter import *
from math import *
#from emoji import emojize

# Criar janela principal
janela = Tk()
janela.title("Calculadora 🔢")
janela.geometry("400x550")
janela.resizable(False, False)
janela.configure(background='bisque')

# Criar tela
texto = StringVar()
tela = Entry(janela, textvariable=texto, font=('Calibri', 24, 'bold'), bd=10, background='paleturquoise2', relief='sunken', justify='right')
tela.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')



#Criar funções
operacao = ''

def limpar():
    global operacao
    operacao = ''
    texto.set('0')

def clicar(b):
    global operacao
    operacao += str(b)
    texto.set(operacao)

def calcular():
    global operacao
    try:
        resultado = str(eval(operacao, {"__builtins__": None},
                             {"sqrt": sqrt, "log": log, "exp": exp, "factorial": factorial}))
        texto.set(resultado)
        operacao = resultado
    except:
        resultado = 'ERROR'
        texto.set(resultado)


def raiz_quadrada():
    global operacao
    valor = float(eval(operacao))
    resultado = sqrt(valor)
    operacao = str(resultado)

def porcentagem():
    global operacao
    if operacao.strip():
        valor = float(eval(operacao))
        resultado = valor / 100
        operacao = str(resultado)
        texto.set(operacao)

def fatorial():
    global operacao
    valor = int(eval(operacao))
    resultado = factorial(valor)
    operacao = str(resultado)

def apagar_ultimo():
    global operacao
    operacao = operacao[:-1]
    texto.set(operacao)

# Criar botões
botoes = [
    ('exp(', 1, 0), ('(', 1, 1), (')', 1, 2), ('C', 1, 3),
    ('√', 2, 0), ('%', 2, 1), ('log(', 2, 2), ('!', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('÷', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('x', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3),
    ('0', 6, 0), ('00', 6, 1), ('.', 6, 2), ('+', 6, 3),
    ('◄', 7, 0, 2), ('=', 7, 2, 2)
    ]

for item in botoes:
    texto_botao = item[0]
    linha = item[1]
    coluna = item[2]
    qtde_colunas = item[3] if len(item) == 4 else 1

    # Associar comandos aos botões
    if texto_botao == 'C':
        comando = limpar
    elif texto_botao == '◄':
        comando = apagar_ultimo
    elif texto_botao == '=':
        comando = calcular
    elif texto_botao == '√':
        comando = lambda: raiz_quadrada()
    elif texto_botao == '%':
        comando = lambda: porcentagem()
    elif texto_botao == '!':
        comando = lambda: fatorial()
    elif texto_botao == 'x':
        comando = lambda t=texto_botao: clicar('*')
    elif texto_botao == '÷':
        comando = lambda t=texto_botao: clicar('/')
    else:
        comando = lambda t=texto_botao: clicar(t)

    # Criar botão e posicionar
    cor = 'light pink1'

    if texto_botao in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '00', '.']:
        cor = 'light pink3'
    elif texto_botao in ['◄', 'C']:
        cor = 'coral'

    botao = Button(janela, text=texto_botao, font=('Arial', 16, 'bold'), bg=cor, width=5, height=1, bd=4,
                   relief='groove', command=comando)
    botao.grid(row=linha, column=coluna, columnspan=qtde_colunas, padx=5, pady=5, sticky='nsew')

#Ajustar
for i in range(7):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()