import flet as ft
from src.components.atoms.PrimaryButton import PrimaryButton
from src.components.atoms.SecondaryButton import SecondaryButton

class LandingPage(ft.View):

    def __init__(self, page: ft.Page):
        super(LandingPage, self).__init__(
            horizontal_alignment="center",
            padding=ft.padding.symmetric(horizontal=40),
        )
        self.page = page
        self.page.title = "Landing page"

        self.controls = [
            ft.Column(
            controls=[
                ft.Image(
                src=f"/Logo.png",
                width="100vw",
                height="100vh",
                fit=ft.ImageFit.CONTAIN,
                ),
                ft.Column(
                controls=[
                    ft.Text(
                    "Réinventez l'apprentissage avec l'intelligence collective",
                    size=20,
                    weight=ft.FontWeight.W_600
                    ),
                    ft.Image(
                    src=f"/LandingIMG.png",
                    width="100vw",
                    height="100vh",
                    fit=ft.ImageFit.CONTAIN,
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

        self.page.padding = 0
        self.page.add(
            ft.Container(
                image_src='/LandingIMG.png',
                image_fit=ft.ImageFit.COVER,
                expand=True,
                content=ft.Control()
            ),
        )

    def on_login_click(self, e):
        self.page.go("/login")

    def on_register_click(self, e):
        self.page.go("/register")