import requests, flet as ft
import src.services.user_service as us
import src.services.decks_service as ds
from src.auth import API_URL, get_auth_header
from src.types.CardStatus import CardStatus
from src.components.organisms.BottomBar import BottomNavigationBar
from src.components.molecules.ChangeDeckDialog import ChangeDeckDialog
from src.components.atoms.Snack import Snack

class DashboardPage(ft.View):

    def on_mount(self):
        self.random_picked_card = None
        self.active_deck_name = None

        try:
            self.active_deck_name = ds.fetch_active_deck(self.page)["name"]
        except Exception as e:
            Snack(self.page, str(e))

        try:
            self.random_picked_card = us.fetch_random_card(self.page)
        except Exception as e:
            Snack(self.page, str(e))

        self.front_content_text = self.random_picked_card["front_content"] if self.random_picked_card else "none"
        self.back_content_text = self.random_picked_card["back_content"] if self.random_picked_card else "none"

        self.page.update()


    def __init__(self, page: ft.Page):
        super(DashboardPage, self).__init__()
        self.page = page
        self.page.title = "Dashboard page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=1)
        self.page.dialog = ft.AlertDialog(
            title=ft.Text("Choisir un deck"),
            content=ChangeDeckDialog(self.page, self.on_mount),
        )

        self.on_mount()

        print(self.front_content_text, self.back_content_text)

        # Face recto de la carte
        self.FrontCardText = ft.Text(
            self.front_content_text,
            size=22, text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD
        )
        self.FrontCard = ft.Card(
            content=ft.Container(
                content=self.FrontCardText,
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=300,
                height=300,
                border_radius=10,
            ),
        )

        # Face verso de la carte
        self.BackCardText = ft.Text(self.back_content_text, size=16)
        self.BackCard = ft.Card(
            content=ft.Container(
                content=self.BackCardText,
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=300,
                height=300,
                border_radius=10,
            ),
        )

        # Variable contenant la carte
        self.CardHolder = ft.AnimatedSwitcher(
            content=self.FrontCard,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=500,
            switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
            switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        )

        # Bouton pour révéler la carte
        self.RevealButton = ft.CupertinoButton(
            "Révéler",
            bgcolor=ft.colors.GREEN_ACCENT_700,
            on_click=self.toggle_card_animation,
        )

        # Variable contenant les boutons "pouce"
        self.ThumbsRow = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.THUMB_UP,
                    icon_color="white",
                    bgcolor=ft.colors.GREEN_ACCENT_700,
                    on_click=lambda e: self.update_card_status(CardStatus.MEMORIZED),
                ),
                ft.IconButton(
                    icon=ft.icons.THUMBS_UP_DOWN,
                    icon_color="white",
                    bgcolor=ft.colors.ORANGE_ACCENT_700,
                    on_click=lambda e: self.update_card_status(CardStatus.IN_PROGRESS),
                ),
                ft.IconButton(
                    icon=ft.icons.THUMB_DOWN,
                    icon_color="white",
                    bgcolor=ft.colors.RED_ACCENT_700,
                    on_click=lambda e: self.update_card_status(CardStatus.NOT_MEMORIZED),
                ),
            ],
        )

        # Variable de gestion des boutons
        self.ButtonHolder = ft.Container(
            content=self.RevealButton,
        )

        self.controls = [
            # Header
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    ft.ElevatedButton(
                        "Changer de deck",
                        on_click=self.open_dlg,
                    )
                ],
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text(self.active_deck_name, size=48),
                padding=ft.padding.only(top=20, bottom=10),
                margin=ft.margin.symmetric(horizontal=50, vertical=10),
                border=ft.Border(bottom=ft.BorderSide(
                    width=3,
                    color=ft.colors.GREEN_ACCENT_200,
                )),
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            self.CardHolder, # Carte
                            self.ButtonHolder, # Bouton(s)
                        ],
                    ),
                ],
            ),
        ]


    def toggle_card_animation(self, e):
        self.CardHolder.content = self.BackCard if self.CardHolder.content == self.FrontCard else self.FrontCard
        self.ButtonHolder.content = self.RevealButton if self.CardHolder.content == self.FrontCard else self.ThumbsRow
        self.page.update()


    def open_dlg(self, e):
        # self.page.dialog.open = True
        # self.page.update()
        self.page.go("/changedeck")


    def roll_new_card(self, e):
        # On remet la carte à l'endroit
        self.toggle_card_animation(None)

        # On récupère une nouvelle carte
        self.random_picked_card = us.fetch_random_card(self.page)

        # On met à jour les textes
        self.FrontCardText.value = self.random_picked_card["front_content"]
        self.BackCardText.value = self.random_picked_card["back_content"]

        self.page.update()


    def update_card_status(self, status: CardStatus):
        response = requests.patch(
            f"{API_URL}/cards/{self.random_picked_card['id']}",
            headers=get_auth_header(self.page),
            params={
                "state": status
            }
        )

        if response.status_code != 200:
            self.page.snack_bar = Snack(self.page, "Erreur lors de la mise à jour de la carte")
            self.page.snack_bar.open = True
            self.page.update()
            return False
        else:
            self.roll_new_card(None)
