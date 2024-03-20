import flet as ft
from src.routes import ROUTES

def main(page: ft.Page):
    page.title = "NotaBene"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="green")

    def route_change(route):
        page.views.clear()
        for route in ROUTES:
            if route == page.route:
                page.views.append(ROUTES[route](page))
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")


<<<<<<< HEAD
ft.app(port=8550, target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
=======
ft.app(
    port=8550,
    target=main,
    view=ft.AppView.WEB_BROWSER,
    assets_dir="assets"
)
>>>>>>> a22ebd6 (new: navigation bottom bar, profile page components)
