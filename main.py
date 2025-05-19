import flet as ft

def main(page: ft.Page):
    page.title = "Página com Imagem de Fundo"
    page.window_width = 1080
    page.window_height = 1920
    page.scroll = 'auto'
    page.padding = 0
    page.margin = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.STRETCH


    fundo = ft.Image(
        src="img.png",  # Ou "fundo.jpg" se for desktop
        fit=ft.ImageFit.COVER,
        expand=True,
    )

    filtro_fosco = ft.Container(
        expand=True,
        bgcolor="rgba(0, 0, 0, 0.5)",  # Preto com 54% de opacidade
    )

    conteudo = ft.Column(
        [
            ft.Text("Bem-vindo!", size=30, color="white"),
            ft.ElevatedButton("Entrar", on_click=lambda e: print("Entrar")),
        ],
        expand=bool,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=page.window_width,
    )

    # Empilha: imagem no fundo, camada escura, conteúdo por cima
    page.add(
        ft.Stack(
            [
                fundo,
                filtro_fosco,
                ft.Container(expand=True, content=conteudo,),
            ],
            expand= True
            
        )
    )

#ft.app(target=main)



# Apenas esta chamada
ft.app(target=main, view="web_browser", assets_dir='assets')
