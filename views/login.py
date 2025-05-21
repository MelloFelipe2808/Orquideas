import flet as ft

def login_view(page: ft.Page):
    fundo = ft.Image(src="img.png",
                     width=page.width, height=page.height,
                     fit=ft.ImageFit.COVER, expand=True, scale=1.7)

    conteudo = ft.Container(
        content=ft.Column(
            [
                ft.Container(height=90),
                ft.Image(src="logo.png", width=130, height=130),
                ft.Container(height=10),
                ft.Text("Bem-vindo!", size=25, color="white", weight="bold"),
                ft.TextField(
                    label="Usuário",
                    width=340,
                    color="black",
                    border_color="#FFFFFF",
                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                ),
                ft.TextField(
                    label="Senha",
                    width=340,
                    color="white",
                    border_color="#FFFFFF",
                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                    password=True,
                ),
                ft.ElevatedButton(
                    content=ft.Text("Entrar", size=18, color="white", weight="bold"),
                    width=200,
                    height=50,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor="#000000",
                    ),
                    on_click=lambda e: print("Entrar"),
                ),
                ft.TextButton(
                    "Criar conta",
                    on_click=lambda e: page.go("/registro"),
                    style=ft.ButtonStyle(color="white"),
                ),
            ],
            width=page.width,
            height=page.height,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    return ft.View(
        route="/",
        controls=[ft.Stack([fundo, conteudo], expand=True)],
    )
