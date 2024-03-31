import requests,json, flet as ft
from src.auth import API_URL
from src.components.atoms.Snack import Snack

class LoginPage(ft.View):

    def __init__(self, page: ft.Page):
        super(LoginPage, self).__init__(
            horizontal_alignment="center",
            padding=ft.padding.symmetric(horizontal=40),
        )
        self.page = page
        self.page.title = "Login page"

        self.EmailField = ft.CupertinoTextField(
            placeholder_text="Email",
            value="admin@notabene.fr",
        )

        self.PasswordField = ft.CupertinoTextField(
            placeholder_text="Mot de passe",
            password=True,
            value="notabene"
        )

        self.controls = [
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text("NotaBene", size=30),
                        padding=ft.padding.symmetric(vertical=50),
                    ),
                    ft.Image(
                        src=f"/Login.png",
                        width="100vw",
                        height="100vh",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    self.EmailField,
                    self.PasswordField,

                    ft.ElevatedButton("Se connecter", on_click=self.handle_login),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]


    def handle_login(self, e):
        # 1. Get email and password from the text fields
        email = self.EmailField.value
        password = self.PasswordField.value

        # 2. Send the data to the server
        response = requests.post(
            url=f"{API_URL}/token",
            data={
                "username": email,
                "password": password
            }
        )

        # 3. If the server responds with a 200 status code, redirect to the dashboard
        # Otherwise show an error message
        if response.status_code == 200:
            token = response.json()["access_token"]
            # TODO: encrypt the token
            self.page.client_storage.set("token", token)

            Snack(self.page, "Authentification réussie", bgcolor=ft.colors.GREEN_ACCENT_200)

            self.page.go("/")
        else:
            Snack(self.page, "Erreur lors de l'authentification")

