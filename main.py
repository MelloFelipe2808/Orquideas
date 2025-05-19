import flet as ft

def main(page: ft.Page):
    page.title = "Recanto Access"
    page.scroll = 'auto'
    page.adaptive = True
    page.window_width = 1080
    page.window_height = 1920

    # ESSENCIAL PARA OCUPAR TELA TODA
    page.padding = 0
    page.margin = 0
    page.spacing = 0
    page.horizontal_alignment = 'stretch'
    page.vertical_alignment = 'stretch'

    fundo = ft.Image(
        width=1080,
        height=1920,
        src="img.png",
        fit=ft.ImageFit.COVER,
        expand=True,
    )


    conteudo = ft.Container(
        expand=True,
        content=ft.Column(
            [
                ft.Text("Bem-vindo!", size=30, color="white"),
                ft.ElevatedButton("Entrar", on_click=lambda e: print("Entrar")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(
        ft.Stack(
            controls=[fundo, conteudo],
            expand=True,
        )
    )

ft.app(
    target=main,
    view="web_browser",
    assets_dir="assets"
)
