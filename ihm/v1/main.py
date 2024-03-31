import requests, flet as ft
from src.routes import ROUTES
from src.auth import API_URL, get_auth_header

def main(page: ft.Page):
    page.title = "NotaBene"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="green")

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        for route in ROUTES:
            if e.route == route:
                page.views.append(ROUTES[route](page))

        verify_token()

        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    def verify_token():
        token = page.client_storage.get("token")
        if not token:
            page.go("/login")
            return
        response = requests.get(
            f"{API_URL}/users/me",
            headers=get_auth_header(page)
        )
        if response.status_code == 401:
            page.go("/login")
            return


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(
    port=8550,
    target=main,
    view=ft.AppView.WEB_BROWSER,
    assets_dir="assets"
)
