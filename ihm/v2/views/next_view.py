import flet as ft
from flet_route import Params,Basket

class NextView:
    def __init__(self):
        ...

    def view(self, page:ft.page, params:Params, basket:Basket):
        print(params)
        print(basket)

        return ft.View(
            "/next_view/:my_id",
            controls=[
                ft.Text("This Is Next View"),
                ft.ElevatedButton("Go Index View", on_click=lambda _: page.go("/")),
            ]
        )
