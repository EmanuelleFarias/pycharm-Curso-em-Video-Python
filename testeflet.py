import flet as ft

def main(page: ft.Page):
    page.title = "Conversor de Temperatura"
    page.theme_mode = "light"
    page.vertical_alignment = "center"

    # Campo de entrada
    input_temp = ft.TextField(label="Temperatura", width=200)

    # Menu de seleção
    unidade_origem = ft.Dropdown(
        label="De",
        width=150,
        options=[
            ft.dropdown.Option("Celsius"),
            ft.dropdown.Option("Fahrenheit"),
            ft.dropdown.Option("Kelvin"),
        ]
    )

    unidade_destino = ft.Dropdown(
        label="Para",
        width=150,
        options=[
            ft.dropdown.Option("Celsius"),
            ft.dropdown.Option("Fahrenheit"),
            ft.dropdown.Option("Kelvin"),
        ]
    )

    resultado = ft.Text(size=20, weight="bold")

    def converter(e):
        try:
            valor = float(input_temp.value)
            origem = unidade_origem.value
            destino = unidade_destino.value
            temp = valor

            # Lógica de conversão
            if origem == destino:
                convertido = temp
            elif origem == "Celsius":
                if destino == "Fahrenheit":
                    convertido = temp * 9/5 + 32
                elif destino == "Kelvin":
                    convertido = temp + 273.15
            elif origem == "Fahrenheit":
                if destino == "Celsius":
                    convertido = (temp - 32) * 5/9
                elif destino == "Kelvin":
                    convertido = (temp - 32) * 5/9 + 273.15
            elif origem == "Kelvin":
                if destino == "Celsius":
                    convertido = temp - 273.15
                elif destino == "Fahrenheit":
                    convertido = (temp - 273.15) * 9/5 + 32

            resultado.value = f"{valor} {origem} = {round(convertido, 2)} {destino}"
            page.update()
        except:
            resultado.value = "Erro na conversão"
            page.update()

    botao_converter = ft.ElevatedButton(text="Converter", on_click=converter)

    page.add(
        ft.Column([
            ft.Text("🌡️ Conversor de Temperatura", size=24, weight="bold"),
            input_temp,
            ft.Row([unidade_origem, unidade_destino], alignment="center"),
            botao_converter,
            resultado
        ], alignment="center", horizontal_alignment="center")
    )

ft.app(target=main)