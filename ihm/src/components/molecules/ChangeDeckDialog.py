import requests, flet as ft
from src.auth import API_URL, get_auth_header
import src.services.user_service as us
from src.components.atoms.Snack import Snack

class ChangeDeckDialog(ft.UserControl):

    def __init__(self, page: ft.Page, on_active_change_callback=None):
        super().__init__()
        self.page = page
        self.active_deck_id = None
        self.decks = []
        self.on_active_change_callback = on_active_change_callback

        try:
            self.active_deck_id = us.fetch_active_deck(self.page)["id"]
            self.decks = us.fetch_decks(self.page)
        except Exception as e:
            Snack(self.page, str(e))


    def build(self):
        return ft.Container(
            height=200,
            content=ft.ListView(
                expand=1,
                controls=[
                    ft.RadioGroup(
                        value=self.active_deck_id,
                        content=ft.Column([
                            ft.Radio(
                                value=deck["id"],
                                label=deck["name"],
                            )
                            for deck in self.decks
                        ]),
                        on_change=self.on_active_deck_change
                    )
                ]
            )
        )


    def on_active_deck_change(self, e):
        if (e.control.value == self.active_deck_id):
            return

        try:
            us.update_active_deck(self.page, e.control.value)
            self.page.dialog.open = False
            Snack(self.page, message="Deck changé avec succès", bgcolor=ft.colors.GREEN_400)
            if self.on_active_change_callback:
                self.on_active_change_callback()

        except Exception as e:
            Snack(self.page, message=str(e))