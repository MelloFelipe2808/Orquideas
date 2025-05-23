import flet as ft
import pyrebase
from firebase_config import firebase_config

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

def registro_view(page: ft.Page):
    nome = ft.TextField(label="NOME", on_change=lambda e: atualizar_maiusculo(e))
    cpf = ft.TextField(label="CPF", on_change=lambda e: formatar_cpf(e))
    contato = ft.TextField(label="CONTATO", on_change=lambda e: formatar_telefone(e))
    email = ft.TextField(label="EMAIL")
    senha = ft.TextField(label="SENHA", password=True)
    placa = ft.TextField(label="PLACA", on_change=lambda e: formatar_placa(e), max_length=8)
    quadra = ft.TextField(label="QUADRA", on_change=lambda e: atualizar_maiusculo(e), max_length=1)
    lote = ft.TextField(label="LOTE", max_length=2)
    feedback = ft.Text(value="", color="red")

    def atualizar_maiusculo(e):
        e.control.value = e.control.value.upper()
        e.control.update()

    def formatar_cpf(e):
        digits = ''.join(filter(str.isdigit, e.control.value))[:11]
        if len(digits) <= 3:
            formatted = digits
        elif len(digits) <= 6:
            formatted = f"{digits[:3]}.{digits[3:]}"
        elif len(digits) <= 9:
            formatted = f"{digits[:3]}.{digits[3:6]}.{digits[6:]}"
        else:
            formatted = f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"
        e.control.value = formatted
        e.control.update()

    def formatar_telefone(e):
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

    def formatar_placa(e):
        value = e.control.value.upper()
        value = ''.join(filter(str.isalnum, value))[:7]
        if len(value) > 3:
            value = value[:3] + '-' + value[3:]
        e.control.value = value
        e.control.update()

    def registrar_usuario(e):
        try:
            user = auth.create_user_with_email_and_password(email.value, senha.value)
            uid = user['localId']
            dados = {
                "nome": nome.value,
                "cpf": cpf.value,
                "contato": contato.value,
                "email": email.value,
                "placa": placa.value,
                "quadra": quadra.value,
                "lote": lote.value
            }
            db.child("usuarios").child(uid).set(dados)
            page.go("/teste")
        except Exception as ex:
            feedback.value = "Erro ao registrar. Verifique os dados ou se o e-mail já existe."
            page.update()

    fundo = ft.Image(src="img.png",
                     width=page.width, height=page.height,
                     fit=ft.ImageFit.COVER, expand=True, scale=1.7)

    conteudo = ft.Container(
        content=ft.Column(
            [
                ft.Text("Registro", size=25, weight="bold"),
                nome,
                cpf,
                contato,
                email,
                senha,
                placa,
                quadra,
                lote,
                feedback,
                ft.Row([
                    ft.ElevatedButton("Registrar", on_click=registrar_usuario),
                    ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/"))
                ])
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        padding=20
    )

    return ft.View(
        route="/registro",
        controls=[ft.Stack([fundo, conteudo])],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )
