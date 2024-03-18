import flet as ft

class DashboardPage(ft.View):

    def __init__(self, page: ft.Page):
        super(DashboardPage, self).__init__(
            route="/dashboard",
        )
        self.page = page
        self.page.title = "Dashboard page"

        self.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.colors.AMBER_100,
            inactive_color=ft.colors.GREY,
            active_color=ft.colors.BLACK,
            on_change=lambda e: print("Selected tab:", e.control.selected_index),
            destinations=[
                ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
                ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
                ft.NavigationDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Explore",
                ),
            ]
        )

        self.controls = [
            ft.Container(
                content=ft.Text("Dashboard", size=30),
                padding=ft.padding.symmetric(vertical=50),
            )
        ]