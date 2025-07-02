
'''import tkinter as tk
from tkinter import *

def button_press(num):

    pass

def equals():
    pass

def clear():
    pass

window = tk.Tk()
window.title('Calculadora')
window.geometry('500x500')

equation_text = ''
equation_label = StringVar()
label = Label(window, textvariable=equation_label, font = ('consolas', 20), bg='white', width=24, height=2)
label.pack()

window.mainloop()'''


import tkinter as tk

def click_boton(valor):
    e_texto.insert(tk.END, str(valor))


ventana = tk.Tk()
ventana.title('Calculadora')
ventana.geometry('300x300')
i=0
#entrada
e_texto = tk.Entry(ventana, font=('Arial', 20),insertwidth=2, width=14, borderwidth=4, justify="right")
e_texto.grid(row=0, column=0,columnspan=5, padx=10, pady=10, sticky='nsew')

# Botões da calculadora

boton1 = tk.Button(ventana, text ='1', width = 5, height = 2, command = lambda:click_boton(1))
boton1.grid(row=1, column=0)
boton2 = tk.Button(ventana, text ='2', width = 5, height = 2, command = lambda:click_boton(2))
boton2.grid(row=1, column=1)
boton3 = tk.Button(ventana, text ='3', width = 5, height = 2, command = lambda:click_boton(3))
boton3.grid(row=1, column=2)





ventana.mainloop()

'''import tkinter as tk

def click_boton(valor):
    e_texto.insert(tk.END, str(valor))

def limpar():
    e_texto.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(e_texto.get())
        e_texto.delete(0, tk.END)
        e_texto.insert(tk.END, str(resultado))
    except:
        e_texto.delete(0, tk.END)
        e_texto.insert(tk.END, "Erro")

ventana = tk.Tk()
ventana.title('Calculadora')

e_texto = tk.Entry(ventana, font=('Arial', 20), insertwidth=2, width=14, borderwidth=4, justify="right")
e_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Números de 1 a 9 organizados em grade 3x3
numeros = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('.', 4, 0)
]

for (texto, linha, coluna) in numeros:
    tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 18),
              command=lambda t=texto: click_boton(t))\
        .grid(row=linha, column=coluna, padx=5, pady=5)

# Operadores e funções
operadores = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 2), ('=', 5, 0)
]

for (texto, linha, coluna) in operadores:
    comando = calcular if texto == '=' else (limpar if texto == 'C' else lambda t=texto: click_boton(t))
    tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 18), bg="#e0e0e0",
              command=comando).grid(row=linha, column=coluna, padx=5, pady=5)

ventana.mainloop()'''

