import flet as ft
from src.components.atoms.CountDisplay import CountDisplay

TEST_PROFILE_TEXT = 'My teaching activities are taught in the DUT "Multimedia and Internet Professions" (MMI ex-SRC) of the IUT and the Master "Information Systems and Internet" (S2I) of the Faculty of Sciences and Techniques (FST) of the University of Corsica'

class ProfileInformations(ft.UserControl):

    def __init__(self):
        super().__init__()


    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(horizontal=20),
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(
                                            src="/capo.png",
                                            width=60,
                                            height=60,
                                        ),
                                        border_radius=ft.border_radius.all(60)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text(
                                                value="Capo",
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                            ft.Text(
                                                value="@capo",
                                                size=12,
                                            ),
                                        ],
                                        spacing=0,
                                    ),
                                ],
                            ),
                            ft.Row(
                                controls=[
                                    CountDisplay(value="12", label="Decks"),
                                    CountDisplay(value="8", label="J'aime"),
                                    CountDisplay(value="4", label="Abonnés"),
                                ],
                                spacing=30,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(TEST_PROFILE_TEXT, text_align=ft.TextAlign.JUSTIFY),
                        ],
                        wrap=True,
                    ),
                ]
            )
        )
