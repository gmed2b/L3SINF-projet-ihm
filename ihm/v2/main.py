import flet as ft
from flet_route import Routing
from routes import app_routes
from middlewares.app_middleware import AppBasedMiddleware

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="green")

    page.window_resizable = True
    page.window_width = 650
    page.window_min_width = 650
    page.window_height = 1000
    page.window_min_height = 1000

    Routing(
        page = page,
        app_routes = app_routes,
        middleware = AppBasedMiddleware().call_me,
        navigation_bar = ft.NavigationBar(
            bgcolor= ft.colors.TRANSPARENT,
            on_change=lambda e: on_tab_change(e, page),
            selected_index=page.client_storage.get("selected_tab") or 1,
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.EXPLORE,
                    label="Explorer",
                ),
                ft.NavigationDestination(icon=ft.icons.CARD_MEMBERSHIP,
                 label="Jouer"
                ),
                ft.NavigationDestination(
                    icon=ft.icons.ACCOUNT_CIRCLE,
                    label="Profil",
                ),
            ]
        )
    )

    page.go(page.route)


    def on_tab_change(e, page: ft.Page):
        page.client_storage.set("selected_tab", e.control.selected_index)
        match e.control.selected_index:
            case 0:
                page.go("/explore")
            case 1:
                page.go("/")
            case 2:
                page.go("/profile")
            case _:
                page.go("/")


ft.app(
    target=main,
    port=8008,
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER
)

