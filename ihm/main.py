import flet as ft
from src.pages.routes import ROUTES


def main(page: ft.Page):

    def router(route):
        page.views.clear()

        if page.route == ROUTES["landing-page"]:
            from src.pages.Landing import LandingPage
            page.views.append(LandingPage(page))

        page.update()

    page.on_route_change = router
    page.go("/")


ft.app(main)
