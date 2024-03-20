import flet as ft
from src.components.organisms.BottomBar import BottomNavigationBar

class DashboardPage(ft.View):

    def __init__(self, page: ft.Page):
        super(DashboardPage, self).__init__()
        self.page = page
        self.page.title = "Dashboard page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=1)

        self.controls = [
            ft.Container(
                content=ft.Text("Dashboard", size=30),
                padding=ft.padding.symmetric(vertical=50),
            ),
            ft.CupertinoButton(
                "Se déconnecter",
                bgcolor=ft.colors.RED_ACCENT,
            ),
        ]

