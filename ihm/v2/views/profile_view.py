import flet as ft
from flet_route import Params,Basket
from components.ProfileInformations import ProfileInformations
from components.DecksList import DecksList

class ProfileView:
    def __init__(self):
        ...

    def view(self, page:ft.page, params:Params, basket:Basket):
        self.page = page

        self.SearchField = ft.TextField(
            hint_text="Rechercher un deck",
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
        )

        return ft.View(
            "/profile",
            controls=[
                ft.Container(
                    content=ft.Text(
                        value="Votre Profil",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                    ),
                    padding=ft.padding.only(top=20, bottom=10),
                ),
                ProfileInformations(self.page),
                self.SearchField,

                ft.Container(
                    expand=True,
                    content=DecksList(self.page),
                ),


                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    bgcolor=ft.colors.GREEN_ACCENT_200,
                    on_click=lambda e: self.page.go("/decks/new")
                )
            ]
        )
