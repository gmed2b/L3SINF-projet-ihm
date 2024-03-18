import flet as ft
from src.pages import Landing, Login, Dashboard

def main(page: ft.Page):
    page.title = "NotaBene"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="green")

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        if e.route == "/":
            page.views.append(
                Landing.LandingPage(page)
            )
        elif e.route == "/login":
            page.views.append(
                Login.LoginPage(page)
            )
        elif e.route == "/dashboard":
            page.views.append(
                Dashboard.DashboardPage(page)
            )

        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(main)
