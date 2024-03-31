import flet as ft
from flet_route import Params,Basket

class ProfileView:
    def __init__(self):
        ...

    def view(self, page:ft.page, params:Params, basket:Basket):

        return ft.View(
            "/profile",
            controls=[
                ft.Text("This Is Profile View"),
                ft.TextButton("logout", on_click=lambda _: page.go("/login"))
            ]
        )
