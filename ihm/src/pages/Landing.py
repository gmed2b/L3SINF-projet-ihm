import flet as ft
from src.components.atoms.PrimaryButton import PrimaryButton
from src.components.atoms.SecondaryButton import SecondaryButton

class LandingPage(ft.View):

    def __init__(self, page: ft.Page):
        super(LandingPage, self).__init__(
            route="/",
            horizontal_alignment="center",
            padding=ft.padding.symmetric(horizontal=40),
        )
        self.page = page
        self.page.title = "Landing page"

        self.controls = [
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text("NotaBene", size=30),
                        padding=ft.padding.symmetric(vertical=50),
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                "Réinventez l'apprentissage avec l'intelligence collective",
                                size=20,
                                weight=ft.FontWeight.W_600
                            ),
                            PrimaryButton(
                                text="Créer un compte",
                                on_click=self.on_register_click
                            ),
                            SecondaryButton(
                                text="Se connecter",
                                on_click=self.on_login_click
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        ]


    def on_login_click(self, e):
        self.page.go("/login")


    def on_register_click(self, e):
        self.page.go("/register")