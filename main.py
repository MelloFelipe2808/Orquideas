import flet as ft
from views.login import login_view
from views.registro import registro_view
from views.home import teste_view

def main(page: ft.Page):
    page.title = "Recanto Access"
    page.scroll = 'auto'
    page.adaptive = True
    page.window_width = 1080
    page.window_height = 1920
    page.padding = 0
    page.margin = 0
    page.spacing = 0
    page.horizontal_alignment = 'stretch'
    page.vertical_alignment = 'stretch'

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(login_view(page))
        elif page.route == "/registro":
            page.views.append(registro_view(page))
        elif page.route == "/teste":
            page.views.append(teste_view(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(
    target=main,
    view="web_browser",
    assets_dir="assets",
    host='192.168.1.7',
    port=5000
)
