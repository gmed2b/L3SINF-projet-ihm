import requests, flet as ft
from auth import API_URL
from flet_route import Params,Basket
from components.PrimaryButton import PrimaryButton
from components.Snack import Snack

class LoginView:
    def __init__(self):
        ...


    def handle_login(self, e):
        email = self.EmailField.value
        password = self.PasswordField.value

        response = requests.post(
            url=f"{API_URL}/token",
            data={
                "username": email,
                "password": password
            }
        )

        if response.status_code != 200:
            Snack(self.page, "Erreur lors de la connexion")
        else:
            token = response.json()["access_token"]
            self.page.client_storage.set("access_token", token)

            Snack(self.page, "Connexion réussie", bgcolor=ft.colors.GREEN_400)
            self.page.go("/")


    def view(self, page:ft.page, params:Params, basket:Basket):
        self.page = page
        self.basket = basket
        page.title = "Login - Notabene"

        self.EmailField = ft.TextField(
            label="Email",
            value="admin@notabene.fr"
        )

        self.PasswordField = ft.TextField(
            label="Password",
            value="notabene",
            password=True
        )

        return ft.View(
            "/login",
            horizontal_alignment="center",
            padding=ft.padding.all(40),
            controls=[
                ft.Image(
                    src=f"/images/logo.png",
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Image(
                    src=f"/images/login_sprite.png",
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Column(
                    spacing=30,
                    controls=[
                        self.EmailField,
                        self.PasswordField,
                    ]
                ),
                ft.Row(
                    spacing=20,
                    controls=[
                        PrimaryButton("Login", on_click=self.handle_login),
                        ft.TextButton("Forgot password?")
                    ]
                )
            ]
        )
