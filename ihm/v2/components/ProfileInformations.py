import flet as ft
import services.user_service as us
from components.CountDisplay import CountDisplay
from components.Snack import Snack

TEST_PROFILE_TEXT = 'My teaching activities are taught in the DUT "Multimedia and Internet Professions" (MMI ex-SRC) of the IUT and the Master "Information Systems and Internet" (S2I) of the Faculty of Sciences and Techniques (FST) of the University of Corsica'

class ProfileInformations(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.user_informations = None
        try:
            self.user_informations = us.fetch_user_info(self.page)
        except Exception as e:
            Snack(self.page, str(e))


    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(horizontal=10),
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(
                                            src="/images/capo.png",
                                            width=60,
                                            height=60,
                                        ),
                                        border_radius=ft.border_radius.all(60)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text(
                                                value=f"{self.user_informations['firstname']} {self.user_informations['lastname']}",
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                            ft.Text(
                                                value=self.user_informations['email'],
                                                size=12,
                                            ),
                                        ],
                                        spacing=0,
                                    ),
                                ],
                            ),
                            ft.Row(
                                controls=[
                                    CountDisplay(value=len(self.user_informations["decks"]), label="Decks"),
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
