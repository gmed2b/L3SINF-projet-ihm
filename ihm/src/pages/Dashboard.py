import flet as ft
from src.components.organisms.BottomBar import BottomNavigationBar

class DashboardPage(ft.View):

    def __init__(self, page: ft.Page):
        super(DashboardPage, self).__init__()
        self.page = page
        self.page.title = "Dashboard page"

        self.navigation_bar = BottomNavigationBar(self.page, selected_index=1)

        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text("P.O.O", size=60),
                padding=ft.padding.symmetric(vertical=50),
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Card(
                        content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    title=ft.Text("Polymorphisme"),
                                    subtitle=ft.Text(),
                                ),
                                ft.Row(
                                    # [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                        width=400,
                        padding=100,
                    ),
        )
                # padding=ft.padding.symmetric(vertical=20),

                ]
            ),
            ft.CupertinoButton(
                "Révéler",
                bgcolor=ft.colors.GREEN_ACCENT_100,
            ),
        ]