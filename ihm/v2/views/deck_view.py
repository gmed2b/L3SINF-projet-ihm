import flet as ft
from flet_route import Params,Basket
from components.Snack import Snack
from components.CardElement import CardElement
from components.PrimaryButton import PrimaryButton
import services.decks_service as ds

class DeckView:
    def __init__(self):
        self.current_deck = None


    def on_card_click(self, card: dict):
        self.basket.editing_card = card
        self.page.go(f"/decks/{self.deck_id}/cards/{card['id']}")


    def get_cards_elements(self, page:ft.Page, deck_id:str):
        if not self.current_deck:
            return []

        cards = self.current_deck["cards"]
        return [
            CardElement(page, card, on_card_click=self.on_card_click)
            for card in cards
        ]


    def save_deck(self, page:ft.Page):
        deck = {
            'name': self.DeckNameField.value,
            'color': self.DeckColorField.value,
        }
        try:
            ds.update_deck(page, self.deck_id, deck)
            Snack(page, "Deck sauvegardé avec succès", bgcolor=ft.colors.GREEN_ACCENT_700)
        except Exception as e:
            Snack(page, str(e))


    def view(self, page:ft.page, params:Params, basket:Basket):
        self.page = page
        self.basket = basket

        self.deck_id = params.get("deck_id")

        try:
            self.current_deck = ds.fetch_deck(page, self.deck_id)
        except Exception as e:
            Snack(page, str(e))


        self.DeckNameField = ft.TextField(
            label="Nom du deck",
            value=self.current_deck["name"],
        )

        self.DeckColorField = ft.TextField(
            label="Couleur",
            value=self.current_deck["color"],
        )


        return ft.View(
            "/decks/:deck_id",
            padding=20,
            controls=[
                ft.Container(
                    padding=ft.padding.only(top=10, bottom=30),
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon="arrow_circle_left_outlined",
                                icon_color="green400",
                                on_click=lambda _: page.go("/profile")
                            ),
                            ft.Container(
                                expand=True,
                                padding=ft.padding.symmetric(vertical=5),
                                bgcolor=ft.colors.GREEN_ACCENT_100,
                                border_radius=ft.border_radius.all(5),
                                content=ft.Text(self.current_deck["name"], size=24, text_align="center")
                            ),
                            ft.Card(
                                color=ft.colors.RED_ACCENT_200,
                                content=ft.IconButton(
                                    icon=ft.icons.DELETE,
                                    icon_color="white",
                                    icon_size=20
                                ),
                            )
                        ]
                    )
                ),

                ft.Container(
                    expand=True,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        spacing=20,
                        controls=[
                            ft.Container(
                                expand=True,
                                content=ft.Column(
                                    spacing=20,
                                    controls=[
                                        self.DeckNameField,
                                        self.DeckColorField,

                                        ft.Container(
                                            expand=True,
                                            content=ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                        controls=[
                                                            ft.Text("Cartes", size=20),
                                                            ft.IconButton(
                                                                icon=ft.icons.ADD_CIRCLE_OUTLINE,
                                                                icon_color=ft.colors.GREEN_400,
                                                                icon_size=22,
                                                                on_click=lambda _: self.page.go(f"/decks/{self.deck_id}/cards/new")
                                                            )
                                                        ]
                                                    ),
                                                    ft.ListView(
                                                        expand=True,
                                                        spacing=10,
                                                        controls=self.get_cards_elements(page, self.deck_id)
                                                    )
                                                ]
                                            )
                                        ),
                                    ]
                                )
                            ),

                            ft.Container(
                                margin=ft.margin.only(top=20),
                                content=ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                    controls=[
                                        ft.CupertinoButton(
                                            content=ft.Text("Sauvegarder", color=ft.colors.WHITE),
                                            bgcolor=ft.colors.GREEN_ACCENT_700,
                                            opacity_on_click=0.5,
                                            on_click=lambda e: self.save_deck(page),
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
