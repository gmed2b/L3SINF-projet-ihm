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
                controls=[
                    ft.Container(
                        bgcolor=ft.colors.GREEN_ACCENT_700,
                        height=2,
                    )
                ]
            )
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Card(
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
                # padding=ft.padding.symmetric(vertical=20),

                ]
            ),

            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.CupertinoButton(
                        "Révéler",
                        bgcolor=ft.colors.GREEN_ACCENT_700,
                    ),
                ]
            ),
            
        ]