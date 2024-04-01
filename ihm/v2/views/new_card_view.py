import flet as ft
from flet_route import Params,Basket
from components.Snack import Snack
import services.cards_service as cs

class NewCardView:
    def __init__(self):
        ...


    def save_card(self):
        card = {
            'name': self.CardNameField.value,
            'content': self.CardContentField.value,
        }
        try:
            cs.create_card(self.page, self.deck_id, card["name"], card["content"])
            Snack(self.page, "Carte sauvegardée avec succès", bgcolor=ft.colors.GREEN_ACCENT_700)
            self.page.go(f"/decks/{self.deck_id}")
        except Exception as e:
            Snack(self.page, str(e))


    def view(self, page:ft.page, params:Params, basket:Basket):
        self.page = page
        self.basket = basket

        self.deck_id = params.get("deck_id")

        self.CardNameField = ft.TextField(
            label="Card name",
        )

        self.CardContentField = ft.TextField(
            label="Content",
            multiline=True,
            min_lines=1,
            max_lines=5,
        )

        return ft.View(
            "/decks/:deck_id/cards/new",
            horizontal_alignment="center",
            padding=20,
            controls=[
                ft.Container(
                    padding=ft.padding.only(top=10, bottom=30),
                    content=ft.Row(
                        controls=[
                            ft.OutlinedButton(
                                "Retour",
                                icon="arrow_circle_left_outlined",
                                icon_color="green400",
                                on_click=lambda _: page.go(f"/decks/{self.deck_id}")
                            ),
                            ft.Text("Nouvelle carte", size=30),
                        ]
                    )
                ),

                ft.Column(
                    spacing=20,
                    controls=[
                        self.CardNameField,
                        self.CardContentField,

                        ft.CupertinoButton(
                            content=ft.Text("Sauvegarder", color=ft.colors.WHITE),
                            bgcolor=ft.colors.GREEN_ACCENT_700,
                            opacity_on_click=0.5,
                            on_click=lambda _: self.save_card(),
                        ),
                    ]
                )
            ]
        )
