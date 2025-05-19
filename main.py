import flet as ft

def main(page: ft.Page):
    page.title = "Fundo 100%"
    page.scroll = 'auto'
    page.window_width = 1080
    page.window_height = 1920

    # ESSENCIAL PARA OCUPAR TELA TODA
    page.padding = 0
    page.margin = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.STRETCH

    fundo = ft.Image(
        src="img.png",
        fit=ft.ImageFit.COVER,
        expand=True,
    )

    filtro_fosco = ft.Container(
        expand=True,
        bgcolor="rgba(0, 0, 0, 0.5)",
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
            controls=[fundo, filtro_fosco, conteudo],
            expand=True,
        )
    )

ft.app(
    target=main,
    view="web_browser",
    assets_dir="assets"
)
