import flet as ft
from flet_route import Params,Basket
from components.Snack import Snack
import services.decks_service as ds

class NewDeckView:
    def __init__(self):
        ...


    def save_deck(self):
        deck = {
            'name': self.DeckNameField.value,
            'color': self.DeckColorField.value,
        }
        try:
            ds.create_deck(self.page, deck["name"], deck["color"])
            Snack(self.page, "Deck sauvegardé avec succès", bgcolor=ft.colors.GREEN_ACCENT_700)
            self.page.go("/profile")
        except Exception as e:
            Snack(self.page, str(e))


    def view(self, page:ft.page, params:Params, basket:Basket):
        self.page = page
        self.basket = basket

        self.DeckNameField = ft.TextField(
            label="Nom du deck",
        )

        self.DeckColorField = ft.TextField(
            label="Couleur",
        )

        return ft.View(
            "/decks/new",
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
                                on_click=lambda _: page.go(f"/profile")
                            ),
                            ft.Text("Créer un deck", size=30),
                        ]
                    )
                ),

                ft.Column(
                    spacing=20,
                    controls=[
                        self.DeckNameField,
                        self.DeckColorField,

                        ft.CupertinoButton(
                            content=ft.Text("Sauvegarder", color=ft.colors.WHITE),
                            bgcolor=ft.colors.GREEN_ACCENT_700,
                            opacity_on_click=0.5,
                            on_click=lambda _: self.save_deck(),
                        ),
                    ]
                )
            ]
        )
