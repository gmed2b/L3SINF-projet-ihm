import flet as ft
from src.components.organisms.BottomBar import BottomNavigationBar

class EditDeckPage(ft.View):

    def __init__(self, page: ft.Page):
        super(EditDeckPage, self).__init__()
        self.page = page
        self.page.title = "Edit page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=2)

        self.controls = [
            ft.Container(
                content=ft.Text("Edit", size=30),
                padding=ft.padding.symmetric(vertical=50),
            )
        ]
