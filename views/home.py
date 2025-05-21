import flet as ft

def teste_view(page: ft.Page):
    fundo = ft.Image(src="img.png",
                     width=page.width, height=page.height,
                     fit=ft.ImageFit.COVER, expand=True, scale=1.7)

    return ft.View(route='/teste', controls=[fundo])
