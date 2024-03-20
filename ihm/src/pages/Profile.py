import flet as ft
from src.components.organisms.BottomBar import BottomNavigationBar
from src.components.organisms.ProfileInformations import ProfileInformations

class ProfilePage(ft.View):

    def __init__(self, page: ft.Page):
        super(ProfilePage, self).__init__()
        self.page = page
        self.page.title = "Profile page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=2)

        self.controls = [
            ft.Container(
                content=ft.Text(
                    value="Profile",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
                padding=ft.padding.only(top=20, bottom=10),
            ),
            ft.Column(
                controls=[
                    ProfileInformations(),
                ],
            ),
        ]

