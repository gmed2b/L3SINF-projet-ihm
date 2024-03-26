import flet as ft
from src.components.organisms.BottomBar import BottomNavigationBar

class ExplorePage(ft.View):

    def __init__(self, page: ft.Page):
        super(ExplorePage, self).__init__()
        self.page = page
        self.page.title = "Explore page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=0)

        self.controls = [
            ft.Container(
                content=ft.Text(
                    value="Explore",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
                padding=ft.padding.only(top=20, bottom=10),
            ),
            ft.TextField(
                hint_text="Rechercher des utilisateurs",
                hint_style={
                    "color": ft.colors.GREEN_800
                },
                autofocus=False,
                text_size=12,
                prefix_icon=ft.icons.SEARCH,
                content_padding=ft.padding.only(left=10),
                border_radius=ft.border_radius.all(20),
                bgcolor=ft.colors.GREEN_ACCENT_100,
                border_width=0,
                focused_border_width=0,
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text(
                    value="Il n'y a pas de contenu à afficher pour le moment.",
                    color=ft.colors.GREY_500,
                ),
                padding=ft.padding.symmetric(vertical=20),
            )
        ]

