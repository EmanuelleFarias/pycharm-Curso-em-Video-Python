import tkinter as tk
from tkinter import ttk

def converter_temperatura():
    try:
        entrada = float(entrada_temp.get())
        escala_origem = combo_origem.get()
        escala_destino = combo_destino.get()

        resultado = ""
        if escala_origem == escala_destino:
            resultado = entrada
        elif escala_origem == "Celsius":
            if escala_destino == "Fahrenheit":
                resultado = entrada * 9/5 + 32
            elif escala_destino == "Kelvin":
                resultado = entrada + 273.15
        elif escala_origem == "Fahrenheit":
            if escala_destino == "Celsius":
                resultado = (entrada - 32) * 5/9
            elif escala_destino == "Kelvin":
                resultado = (entrada - 32) * 5/9 + 273.15
        elif escala_origem == "Kelvin":
            if escala_destino == "Celsius":
                resultado = entrada - 273.15
            elif escala_destino == "Fahrenheit":
                resultado = (entrada - 273.15) * 9/5 + 32

        label_resultado.config(text=f"Resultado: {resultado:.2f} {escala_destino}")
    except ValueError:
        label_resultado.config(text="Digite um valor válido.")

# Interface Gráfica
janela = tk.Tk()
janela.title("Conversor de Temperatura")
janela.geometry("340x200")
janela.configure(bg="#f0f0f0")

# Widgets
ttk.Label(janela, text="Temperatura:", font=("Segoe UI", 10)).pack(pady=5)
entrada_temp = ttk.Entry(janela, width=20)
entrada_temp.pack()

frame_escalas = ttk.Frame(janela)
frame_escalas.pack(pady=10)

combo_origem = ttk.Combobox(frame_escalas, values=["Celsius", "Fahrenheit", "Kelvin"], width=10)
combo_origem.set("Celsius")
combo_origem.grid(row=0, column=0, padx=5)

ttk.Label(frame_escalas, text="→").grid(row=0, column=1)

combo_destino = ttk.Combobox(frame_escalas, values=["Celsius", "Fahrenheit", "Kelvin"], width=10)
combo_destino.set("Fahrenheit")
combo_destino.grid(row=0, column=2, padx=5)

btn_converter = ttk.Button(janela, text="Converter", command=converter_temperatura)
btn_converter.pack(pady=10)

label_resultado = ttk.Label(janela, text="Resultado: ", font=("Segoe UI", 11))
label_resultado.pack(pady=5)

janela.mainloop()
