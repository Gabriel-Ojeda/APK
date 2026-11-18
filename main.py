import math
import flet as ft

def main(page: ft.Page):
    page.title = "Factorizador de Polinomios"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de texto para a, b y c
    input_a = ft.TextField(label="Coeficiente a", value="1", keyboard_type=ft.KeyboardType.NUMBER, width=100)
    input_b = ft.TextField(label="Coeficiente b", value="0", keyboard_type=ft.KeyboardType.NUMBER, width=100)
    input_c = ft.TextField(label="Coeficiente c", value="0", keyboard_type=ft.KeyboardType.NUMBER, width=100)
    
    result_text = ft.Text(value="", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    def calcular_factorizacion(e):
        try:
            a = float(input_a.value)
            b = float(input_b.value)
            c = float(input_c.value)

            if a == 0:
                result_text.value = "Error: 'a' no puede ser 0 (no sería de segundo grado)."
                page.update()
                return

            # Discriminante
            delta = b**2 - 4 * a * c

            if delta < 0:
                result_text.value = "El polinomio tiene raíces complejas (no se puede factorizar en los reales fácilmente)."
            else:
                # Raíces
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)

                # Formatear la salida de manera limpia
                def format_factor(root):
                    if root == 0:
                        return "x"
                    elif root > 0:
                        return f"(x - {root:g})"
                    else:
                        return f"(x + {-root:g})"

                factor_a = f"{a:g}" if a != 1 else ""
                if a == -1:
                    factor_a = "-"

                fact_str = f"{factor_a}{format_factor(x1)}{format_factor(x2)}"
                
                result_text.value = (
                    f"Raíces: x₁ = {x1:g}, x₂ = {x2:g}\n\n"
                    f"Forma factorizada:\n{fact_str}"
                )
        except ValueError:
            result_text.value = "Por favor, ingresa números válidos."
        
        page.update()

    # Botón para Flet 1.0
    calc_button = ft.Button(content="Factorizar", on_click=calcular_factorizacion)

    # Diseño de la interfaz (sin ft.colors para evitar conflictos)
    page.add(
        ft.Text("Factorizador de 2do Grado", size=22, weight=ft.FontWeight.BOLD),
        ft.Text("Introduce los valores de ax² + bx + c:", size=14),
        ft.Row([input_a, input_b, input_c], alignment=ft.MainAxisAlignment.CENTER),
        calc_button,
        ft.Divider(),
        result_text
    )

ft.run(main)