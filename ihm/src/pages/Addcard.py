import requests, flet as ft
from src.auth import API_URL, get_auth_header

class AddCardPage(ft.View):

    def __init__(self, page: ft.Page):
        super(AddCardPage, self).__init__()
        self.page = page
        self.page.title = "AddCard page"

        self.editing_deck_id = self.page.client_storage.get('editing_deck_id')

        self.CardNameField = ft.CupertinoTextField(
            placeholder_text="Nom de la carte",
        )

        self.CardDescriptionField = ft.CupertinoTextField(
            placeholder_text="Description",
            multiline=True,
            min_lines=5,
        )

        self.controls = [
            ft.Container(
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                    width=500,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                    icon_color="blue400",
                                    icon_size=20,
                                    on_click=lambda _: self.page.go("/edit")
                                ),
                                ft.Text("Créer une carte", size=30),
                            ]
                        ),
                        self.CardNameField,
                        self.CardDescriptionField,
                        ft.ElevatedButton("Créer", on_click=lambda _: self.handle_add_card()),
                    ],
                ),
            ),
        ]


    def handle_add_card(self):
        deck_name = self.CardNameField.value
        deck_description = self.CardDescriptionField.value

        response = requests.post(
            f"{API_URL}/cards/",
            headers=get_auth_header(self.page),
            params={
                "deck_id": self.editing_deck_id,
            },
            json={
                "front_content": deck_name,
                "back_content": deck_description,
            },
        )

        if response.status_code == 200:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Carte ajoutée avec succès"),
                behavior=ft.SnackBarBehavior.FLOATING,
                bgcolor=ft.colors.GREEN_400,
            )
            self.page.snack_bar.open = True
            self.page.go("/edit")
        else:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Erreur lors de l'ajout de la carte"),
                behavior=ft.SnackBarBehavior.FLOATING,
                bgcolor=ft.colors.RED_400,
            )
            self.page.snack_bar.open = True
            self.page.update()