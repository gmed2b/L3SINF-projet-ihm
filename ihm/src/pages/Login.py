import flet as ft

class LoginPage(ft.View):

    def __init__(self, page: ft.Page):
        super(LoginPage, self).__init__(
            horizontal_alignment="center",
            padding=ft.padding.symmetric(horizontal=40),
        )
        self.page = page
        self.page.title = "Login page"

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
                    ft.CupertinoTextField(
                        placeholder_text="Email",
                    ),
                    ft.CupertinoTextField(
                        placeholder_text="Mot de passe",
                    ),

                    ft.ElevatedButton("Se connecter", on_click=self.handle_login),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]


    def handle_login(self, e):
        print("Login clicked")
        # TODO: Implement login logic
        # 1. Get email and password from the text fields
        # 2. Send the data to the server
        # 3. If the server responds with a 200 status code, redirect to the dashboard
        # 4. Otherwise show an error message
        self.page.go("/dashboard")