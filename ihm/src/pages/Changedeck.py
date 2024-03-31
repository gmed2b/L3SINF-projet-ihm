import flet as ft
import src.services.user_service as us
from src.components.atoms.Snack import Snack

class ChangedeckPage(ft.View):

    def __init__(self, page: ft.Page):
        super(ChangedeckPage, self).__init__()
        self.page = page
        self.page.title = "Changedeck page"

        self.active_deck_id = None
        self.decks = []

        try:
            self.active_deck_id = us.fetch_active_deck(self.page)["id"]
            self.decks = us.fetch_decks(self.page)
        except Exception as e:
            Snack(self.page, str(e))


        self.controls = [
            ft.Container(
                padding=ft.padding.only(top=10),
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_CIRCLE_LEFT_OUTLINED,
                            icon_color="blue400",
                            icon_size=20,
                            on_click=lambda _: self.page.go("/")
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
                ]
            )
        ]


    def on_active_deck_change(self, e):
        if (e.control.value == self.active_deck_id):
            return

        try:
            us.update_active_deck(self.page, e.control.value)
            Snack(self.page, message="Deck changé avec succès", bgcolor=ft.colors.GREEN_400)

        except Exception as e:
            Snack(self.page, message=str(e))