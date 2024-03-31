import flet as ft
from flet_route import Params,Basket
import services.decks_service as ds
from components.Snack import Snack
from components.FlashCard import FlashCard

class IndexView:
    def __init__(self):
        ...


    def get_active_deck(self):
        active_deck = self.basket.get("active_deck")
        if not active_deck:
            try:
                active_deck = ds.fetch_active_deck(self.page)
                self.basket.active_deck = active_deck
            except Exception as e:
                Snack(self.page, str(e))

        return active_deck


    def view(self, page:ft.page, params:Params, basket:Basket):
        self.page = page
        self.basket = basket
        page.title = "NotaBene"

        self.active_deck = self.get_active_deck()

        return ft.View(
            "/",
            padding=20,
            controls=[
                # Header row
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        # Progress ring
                        ft.Stack(
                            controls=[
                                ft.ProgressRing(width=52, height=52, stroke_width=5, color=ft.colors.GREEN_ACCENT_100, value=1), # Placeholder
                                ft.ProgressRing(width=52, height=52, stroke_width=5, value=0.3), # Actual progress
                                ft.Text(
                                    f"{30}%",
                                    size=14,
                                    color=ft.colors.GREY_800,
                                    text_align=ft.TextAlign.CENTER,
                                    left=11,
                                    top=15
                                ),
                            ]
                        ),

                        # Change deck button
                        ft.ElevatedButton(
                            "Changer de deck",
                            on_click=lambda _: page.go(f"/change-deck/{self.active_deck['id']}")
                        )
                    ],
                ),

                # Deck name
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        self.active_deck["name"],
                        size=38
                    ),
                    padding=ft.padding.only(top=20, bottom=10),
                    margin=ft.margin.symmetric(horizontal=80, vertical=10),
                    border=ft.Border(bottom=ft.BorderSide(
                        width=3,
                        color=ft.colors.GREEN_ACCENT_200,
                    )),
                ),

                # Flashcard
                ft.Row(
                    alignment="center",
                    controls=[
                        FlashCard(
                            page=page,
                        )
                    ]
                )
            ]
        )
