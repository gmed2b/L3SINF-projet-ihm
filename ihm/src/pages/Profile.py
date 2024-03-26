import requests, flet as ft
from src.components.organisms.BottomBar import BottomNavigationBar
from src.components.organisms.ProfileInformations import ProfileInformations
from src.auth import API_URL, get_auth_header

class ProfilePage(ft.View):

    def __init__(self, page: ft.Page):
        super(ProfilePage, self).__init__()
        self.page = page
        self.page.title = "Profile page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=2)

        self.DecksView = ft.GridView(
                                runs_count=2,
                                run_spacing=10,
                                max_extent=300,
                                height=550
                            )
        self.DecksView.controls = self.fill_user_decks()

        self.SearchField = ft.TextField(
                                hint_text="Rechercher un deck",
                                hint_style={
                                    "color": ft.colors.GREEN_800
                                },
                                autofocus=False,
                                text_size=12,
                                prefix_icon=ft.icons.SEARCH,
                                content_padding=ft.padding.only(left=10),
                                border_radius=ft.border_radius.all(20),
                                bgcolor=ft.colors.GREEN_ACCENT_100,
                                border_width=0,
                                focused_border_width=0,
                            )

        self.fab_actions = []
        if self.page.platform in ["ios", "macos"]:
            self.fab_actions = [
                ft.CupertinoDialogAction(
                    text="OK",
                    on_click=lambda e: self.handle_create_deck()
                ),
                ft.CupertinoDialogAction(
                    text="Cancel",
                    on_click=lambda e: self.close_adaptive_dialog()
                ),
            ]
        else:
            self.fab_actions = [
                ft.TextButton(
                    text="OK",
                    on_click=lambda e: self.handle_create_deck()
                ),
                ft.TextButton(
                    text="Cancel",
                    on_click=lambda e: self.close_adaptive_dialog()
                )
            ]

        self.FabInputField = ft.TextField(label="Standard")

        self.adaptive_alert_dialog = ft.AlertDialog(
                                        adaptive=True,
                                        title=ft.Text("Créer un deck"),
                                        content=ft.Container(
                                            padding=ft.padding.symmetric(vertical=10),
                                            content=ft.Row(
                                                wrap=True,
                                                controls=[
                                                    ft.Text("Entrez le nom du deck :"),
                                                    self.FabInputField,
                                                ]
                                            )
                                        ),
                                        actions=self.fab_actions,
                                    )

        self.controls = [
            ft.Container(
                content=ft.Text(
                    value="Profile",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
                padding=ft.padding.only(top=20, bottom=10),
            ),
            ft.Column(
                spacing=20,
                controls=[
                    ProfileInformations(),
                    self.SearchField,
                    ft.Container(
                        content=self.DecksView,
                    )
                ],
            ),
            ft.FloatingActionButton(
                icon=ft.icons.ADD,
                bgcolor=ft.colors.GREEN_ACCENT_200,
                on_click=lambda e: self.open_adaptive_dialog()
            )
        ]


    def open_adaptive_dialog(self):
        self.page.dialog = self.adaptive_alert_dialog
        self.adaptive_alert_dialog.open = True
        self.page.update()


    def close_adaptive_dialog(self):
        self.adaptive_alert_dialog.open = False
        self.page.update()


    def handle_create_deck(self):
        deck_name = self.FabInputField.value
        if (deck_name == ""):
            self.close_adaptive_dialog()
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Le nom du deck ne peut pas être vide"),
                behavior=ft.SnackBarBehavior.FLOATING,
                bgcolor=ft.colors.RED_400,
            )
            self.page.snack_bar.open = True
            self.page.update()
            return

        self.create_deck(deck_name)


    def create_deck(self, deck_name: str):
        response = requests.post(
            f"{API_URL}/decks/",
            headers=get_auth_header(self.page),
            json={
                "name": deck_name
            }
        )

        if response.status_code != 200:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Erreur lors de la création du deck"),
                behavior=ft.SnackBarBehavior.FLOATING,
                bgcolor=ft.colors.RED_400,
            )
            self.page.snack_bar.open = True
            self.page.update()
        else:
            self.close_adaptive_dialog()
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Deck créé avec succès"),
                behavior=ft.SnackBarBehavior.FLOATING,
                bgcolor=ft.colors.GREEN_400,
            )
            self.page.snack_bar.open = True
            self.DecksView.controls = self.fill_user_decks()
            self.page.update()


    def goto_edit_deck(self, deck_id: int):
        self.page.client_storage.set("editing_deck_id", deck_id)
        self.page.go("/edit")


    def fill_user_decks(self):
        user_decks = self.fetch_user_decks()

        def VisibilityIcon(text: str):
            VIcons = text == "public" and ft.icons.PUBLIC or text == "friends" and ft.icons.PEOPLE_OUTLINE or ft.icons.LOCK
            return ft.Icon(
                name=VIcons,
                color=ft.colors.GREY_500,
                size=18,
            )

        def VisibilityCard(text: str):
            return ft.Card(
                content=ft.Container(
                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                    content=ft.Row(
                        spacing=5,
                        controls=[
                            VisibilityIcon(text),
                            ft.Text(text.capitalize())
                        ]
                    )
                )
            )

        if user_decks and len(user_decks) > 0:
            return [
                ft.Container(
                    data=deck["id"],
                    on_click=lambda e: self.goto_edit_deck(e.control.data),
                    content=ft.Card(
                        color=deck["color"],
                        content=ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row([
                                        VisibilityCard(deck["visibility"]),
                                    ]),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                value=deck["name"],
                                                size=20,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                        ]
                                    ),
                                    ft.Row([
                                        ft.Text(
                                            f"{len(deck['cards'])} carte{'s' if len(deck['cards']) > 1 else ''}",
                                            size=16
                                        )
                                    ]),
                                ]
                            )
                        ),
                    )
                )
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


    def fetch_user_decks(self):
        response = requests.get(
            f"{API_URL}/decks/",
            headers=get_auth_header(self.page)
        )

        if response.status_code != 200:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Erreur lors de la récupération des decks"),
                behavior=ft.SnackBarBehavior.FLOATING,
                bgcolor=ft.colors.RED_400,
            )
            self.page.snack_bar.open = True
            return False
        else:
            return response.json()