import flet as ft
from routes import ROUTES

class LandingPage(ft.View):

    def __init__(self, page: ft.Page):
        super(LandingPage, self).__init__(
            route=ROUTES["landing-page"],
            horizontal_alignment="center",
            vertical_alignment="center",
        )

        self.page = page
        self.c