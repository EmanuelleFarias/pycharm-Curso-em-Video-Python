'''import tkinter as tk

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora Tkinter")
janela.geometry("300x400")
janela.resizable(False, False)

# Variável para exibir o texto
entrada_texto = tk.StringVar()

# Campo de entrada
entrada = tk.Entry(janela, textvariable=entrada_texto, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

bd=Define a espessura da borda (border depth)
relief = Estilo da borda (pode usar "flat", "sunken", "raised"...).
padx/pady = Adiciona espaço ao redor do campo para não ficar colado nas bordas
nsew = Faz o campo expandir vertical e horizontal, ocupando toda a célula (Norte Sul Leste Oeste = nsew)
columnspan = quantas colunas o campo/botao vai ocupar

# Variável de operação
operacao = ""

# Funções
def clique(valor):
    global operacao
    operacao += str(valor)
    entrada_texto.set(operacao)

def limpar():
    global operacao
    operacao = ""
    entrada_texto.set("")

def calcular():
    global operacao
    try:
        resultado = str(eval(operacao))
        entrada_texto.set(resultado)
        operacao = resultado
    except:
        entrada_texto.set("Erro")
        operacao = ""

# Botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)  # Botão igual ocupa 4 colunas
]

for item in botoes:
    texto = item[0]
    linha = item[1]
    coluna = item[2]
    colspan = item[3] if len(item) == 4 else 1

    comando = calcular if texto == '=' else limpar if texto == 'C' else lambda t=texto: clique(t)

    botao = tk.Button(janela, text=texto, font=("Arial", 18), bd=5, relief="ridge",
                      command=comando, bg="bisque")
    botao.grid(row=linha, column=coluna, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# Ajustar proporções
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()'''

import tkinter as tk
from math import sqrt, log, exp, factorial

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("380x580")
janela.resizable(False, False)

# Variável da tela
texto = tk.StringVar()
tela = tk.Entry(janela, textvariable=texto, font=("Arial", 24), bd=10, relief="ridge", justify="right")
tela.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

operacao = ""

# Funções
def clicar(valor):
    global operacao
    operacao += str(valor)
    texto.set(operacao)

def limpar():
    global operacao
    operacao = ""
    texto.set("")

def apagar_ultimo():
    global operacao
    operacao = operacao[:-1]
    texto.set(operacao)

def calcular():
    global operacao
    try:
        resultado = str(eval(operacao, {"__builtins__": None}, {
            "sqrt": sqrt,
            "log": log,
            "exp": exp,
            "factorial": factorial
        }))
        texto.set(resultado)
        operacao = resultado
    except:
        texto.set("Erro")
        operacao = ""

# Botões da calculadora
botoes = [
    ('(', 1, 0), (')', 1, 1), ('C', 1, 2), ('⌫', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('%', 5, 2), ('+', 5, 3),
    ('sqrt(', 6, 0), ('log(', 6, 1), ('exp(', 6, 2), ('factorial(', 6, 3),
    ('**', 7, 0), ('x²', 7, 1), ('=', 7, 2, 2)  # '=' ocupa coluna 2 e 3
]

for item in botoes:
    texto_botao = item[0]
    linha = item[1]
    coluna = item[2]
    colspan = item[3] if len(item) == 4 else 1

    # Associa comandos aos botões
    if texto_botao == 'C':
        comando = limpar
    elif texto_botao == '⌫':
        comando = apagar_ultimo
    elif texto_botao == '=':
        comando = calcular
    elif texto_botao == 'x²':
        comando = lambda: clicar('**2')
    elif texto_botao == '%':
        comando = lambda: clicar('/100')
    else:
        comando = lambda x=texto_botao: clicar(x)

    # Cria botão e posiciona
    botao = tk.Button(janela, text=texto_botao, font=("Arial", 16), bg="lightblue", bd=4,
                      relief="raised", command=comando)
    botao.grid(row=linha, column=coluna, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# Responsividade
for i in range(8):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()