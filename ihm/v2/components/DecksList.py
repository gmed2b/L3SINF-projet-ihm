import requests, flet as ft
from services.cards_service import update_card_status
import services.user_service as us
import services.decks_service as ds
from interfaces.CardStatus import CardStatus
from components.Snack import Snack
from components.DeckCard import DeckCard

def DecksList(page: ft.Page) -> ft.Container:

    def get_user_decks():
        try:
            user_decks = ds.fetch_decks(page)

            if user_decks and len(user_decks) > 0:
                return [
                    DeckCard(page, deck)
                    for deck in user_decks
                ]
            else:
                return [ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        value="Vous ne possédez aucun deck.",
                        color=ft.colors.GREY_500,
                        size=16
                    ),
                    padding=ft.padding.symmetric(vertical=20),
                )]

        except Exception as e:
            Snack(page, str(e))


    DecksView = ft.GridView(
        expand=True,
        runs_count=2,
        run_spacing=10,
        max_extent=300,
    )
    DecksView.controls = get_user_decks()

    return ft.Container(
        expand=True,
        content=DecksView,
    )
