import requests, flet as ft
from src.auth import API_URL, get_auth_header
from src.components.organisms.BottomBar import BottomNavigationBar

class EditDeckPage(ft.View):

    def __init__(self, page: ft.Page):
        super(EditDeckPage, self).__init__()
        self.page = page
        self.page.title = "Edit page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=2)

        self.editing_deck_id = self.page.client_storage.get('editing_deck_id')
        self.editing_deck = self.fetch_deck(self.editing_deck_id)


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
                            tooltip="Pause record",
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
                padding=ft.padding.only(top=50),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                    controls=[
                        ft.ElevatedButton(
                            text="Ajouter une carte",
                            on_click=lambda e: self.goto_add_card()
                        ),
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
        pass


    def fetch_deck(self, deck_id):
        response = requests.get(
            f"{API_URL}/decks/{deck_id}",
            headers=get_auth_header(self.page)
        )

        if response.status_code != 200:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Erreur lors de la récupération du deck"),
                behavior=ft.SnackBarBehavior.FLOATING,
                bgcolor=ft.colors.RED_400,
            )
            self.page.snack_bar.open = True
            return False
        else:
            return response.json()