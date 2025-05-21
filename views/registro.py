import flet as ft

def registro_view(page: ft.Page):
    def to_uppercase(e):
        e.control.value = e.control.value.upper()
        e.control.update()

    def format_cpf(e):
        digits = ''.join(filter(str.isdigit, e.control.value))[:11]
        if len(digits) <= 3:
            formatted = digits
        elif len(digits) <= 6:
            formatted = f"{digits[:3]}.{digits[3:]}"
        elif len(digits) <= 9:
            formatted = f"{digits[:3]}.{digits[3:6]}.{digits[6:]}"
        else:
            formatted = f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:11]}"
        e.control.value = formatted
        e.control.update()

    def format_phone(e):
        digits = ''.join(filter(str.isdigit, e.control.value))[:11]
        formatted = ''
        if len(digits) >= 2:
            formatted += f'({digits[:2]}) '
            if len(digits) >= 3:
                formatted += f'{digits[2]}-'
                if len(digits) >= 7:
                    formatted += f'{digits[3:7]}-'
                    formatted += digits[7:]
                else:
                    formatted += digits[3:]
        else:
            formatted += digits
        e.control.value = formatted
        e.control.update()

    def format_placa(e):
        value = e.control.value.upper()
        value = ''.join(filter(str.isalnum, value))[:7]
        if len(value) > 3:
            value = value[:3] + '-' + value[3:]
        e.control.value = value
        e.control.update()

    fundo = ft.Image(src="img.png",
                     width=page.width, height=page.height,
                     fit=ft.ImageFit.COVER, expand=True, scale=1.7)

    conteudo_regi = ft.Container(
        content=ft.Column(
            [
                ft.Text("Registro", size=25, weight="bold"),
                ft.TextField(label="NOME", on_change=to_uppercase),
                ft.TextField(label="CPF", on_change=format_cpf),
                ft.TextField(label="CONTATO", on_change=format_phone),
                ft.TextField(label="PLACA", on_change=format_placa, max_length=8),
                ft.TextField(label="QUADRA", on_change=to_uppercase, max_length=1),
                ft.TextField(label="LOTE", max_length=2),
                ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/teste")),
            ]
        )
    )

    return ft.View(
        route="/registro",
        controls=[ft.Stack([fundo, conteudo_regi])],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )
