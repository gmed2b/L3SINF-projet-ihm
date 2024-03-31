import flet as ft
from flet_route import Params,Basket
from components.Snack import Snack
import services.decks_service as ds
import services.user_service as us

class ChangeDeckView:
    def __init__(self):
        ...


    def get_decks(self):
        try:
            decks = ds.fetch_decks(self.page)
        except Exception as e:
            Snack(self.page, str(e))

        return decks


    def on_deck_change(self, e):
        if (e.control.value == self.current_deck_id):
            return

        try:
            new_active_deck = us.update_active_deck(self.page, e.control.value)
            self.basket.active_deck = ds.fetch_active_deck(self.page)
            Snack(self.page, message="Deck changé avec succès", bgcolor=ft.colors.GREEN_400)
            self.page.go("/")

        except Exception as e:
            Snack(self.page, message=str(e))



    def view(self, page:ft.page, params:Params, basket:Basket):
        self.page = page
        self.basket = basket

        self.current_deck_id = params.get("current_deck_id")
        self.decks = self.get_decks()

        return ft.View(
            "/change-deck/:current_deck_id",
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
                                on_click=lambda _: page.go("/")
                            ),
                            ft.Text("Changer de deck", size=30),
                        ]
                    )
                ),

                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ListView(
                            controls=[
                                ft.RadioGroup(
                                    value=self.current_deck_id,
                                    content=ft.Column([
                                        ft.Radio(
                                            value=deck["id"],
                                            label=deck["name"],
                                        )
                                        for deck in self.decks
                                    ]),
                                    on_change=self.on_deck_change
                                )
                            ]
                        )
                    ]
                )
            ]
        )
