import flet as ft
from src.components.organisms.BottomBar import BottomNavigationBar

class DashboardPage(ft.View):

    def __init__(self, page: ft.Page):
        super(DashboardPage, self).__init__()
        self.page = page
        self.page.title = "Dashboard page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=1)

        self.FrontCard = ft.Card(
            content=ft.Container(
                padding=60,
                content=ft.Container(
                    content=ft.Text("Polymorphisme", size=18),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
            ),
        )

        self.BackCard = ft.Card(
            content=ft.Container(
                padding=60,
                content=ft.Container(
                    content=ft.Text("Le concept consistant à fournir une interface unique à des entités pouvant avoir différents types morphisme", size=12),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
            ),
        )

        self.CardHolder = ft.AnimatedSwitcher(
            content=self.FrontCard,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=500,
            switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
            switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        )

        self.RevealButton = ft.CupertinoButton(
            "Révéler",
            bgcolor=ft.colors.GREEN_ACCENT_700,
            on_click=self.animate_card,
        )

        self.ThumbsRow = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.THUMB_UP,
                    icon_color="white",
                    bgcolor=ft.colors.GREEN_ACCENT_700,
                    on_click=self.animate_card,
                ),
                ft.IconButton(
                    icon=ft.icons.THUMBS_UP_DOWN,
                    icon_color="white",
                    bgcolor=ft.colors.ORANGE_ACCENT_700,
                    on_click=self.animate_card,
                ),
                ft.IconButton(
                    icon=ft.icons.THUMB_DOWN,
                    icon_color="white",
                    bgcolor=ft.colors.RED_ACCENT_700,
                    on_click=self.animate_card,
                ),
            ],
        )

        self.ButtonHolder = ft.Container(
            content=self.RevealButton,
        )
        
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text("P.O.O", size=60),
                padding=ft.padding.symmetric(vertical=50),
            ),

            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            self.CardHolder,
                            self.ButtonHolder,
                        ],
                    ),
                ],
            ),
        ]


    def animate_card(self, e):
        self.CardHolder.content = self.BackCard if self.CardHolder.content == self.FrontCard else self.FrontCard
        self.ButtonHolder.content = self.RevealButton if self.CardHolder.content == self.FrontCard else self.ThumbsRow
        self.page.update()
