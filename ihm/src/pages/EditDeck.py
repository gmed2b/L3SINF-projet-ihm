import requests, flet as ft
import src.services.decks_service as ds
from src.components.organisms.BottomBar import BottomNavigationBar

class EditDeckPage(ft.View):

    def __init__(self, page: ft.Page):
        super(EditDeckPage, self).__init__()
        self.page = page
        self.page.title = "Edition deck"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=2)

        self.editing_deck_id = self.page.client_storage.get('editing_deck_id')
        try:
            self.editing_deck = ds.fetch_deck(self.page, self.editing_deck_id)
        except Exception as e:
            self.page.go("/profile")


        self.DeckNameField = ft.TextField(
            value=self.editing_deck['name'],
            hint_text="Nom du deck",
            autofocus=False,
            text_size=16,
            content_padding=ft.padding.only(left=10),
            bgcolor=ft.colors.WHITE,
        )

        self.DeckColorField = ft.TextField(
            value=self.editing_deck['color'],
            hint_text="Couleur",
            autofocus=False,
            text_size=16,
            content_padding=ft.padding.only(left=10),
            bgcolor=ft.colors.WHITE,
        )


        self.controls = [
            ft.Container(
                padding=ft.padding.only(top=10),
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_CIRCLE_LEFT_OUTLINED,
                            icon_color="blue400",
                            icon_size=20,
                            on_click=lambda _: self.page.go("/profile")
                        ),
                        ft.Text(f"{self.editing_deck['name']}", size=30),
                    ]
                )
            ),
            ft.Container(
                padding=ft.padding.only(top=20),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.DeckNameField,
                        self.DeckColorField,
                    ]
                )
            ),
            ft.Container(
                padding=ft.padding.only(top=20),
                content=ft.Column(
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text("Cartes", size=20),
                                ft.IconButton(
                                    icon=ft.icons.ADD,
                                    icon_color="blue400",
                                    icon_size=20,
                                    on_click=lambda _: self.goto_add_card()
                                )
                            ]
                        ),
                        ft.GridView(
                            max_extent=200,
                            height=550,
                            controls=self.fill_cards()
                        )
                    ]
                )
            ),
            ft.Container(
                padding=ft.padding.only(top=50),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                    controls=[
                        ft.ElevatedButton(
                            text="Enregistrer",
                            on_click=lambda e: self.handle_save_deck()
                        ),
                    ]
                )
            )
        ]


    def goto_add_card(self):
        self.page.go("/add-card")


    def handle_save_deck(self):
        deck = {
            'name': self.DeckNameField.value,
            'color': self.DeckColorField.value,
        }

        try:
            ds.update_deck(self.page, self.editing_deck_id, deck)
            self.page.go("/profile")
        except Exception as e:
            print(e)


    def fill_cards(self):
        return [
            ft.Card(
                content=ft.Container(
                    padding=ft.padding.symmetric(horizontal=20, vertical=15),
                    content=ft.Column(
                        spacing=20,
                        controls=[
                            ft.Text(card['front_content'], text_align=ft.TextAlign.CENTER),
                            ft.Text(card['state'], text_align=ft.TextAlign.CENTER, size=12, color="blue400"),
                        ]
                    )
                )
            )
            for card in self.editing_deck['cards']
        ]
