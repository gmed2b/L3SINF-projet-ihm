import flet as ft

class BottomBar(ft.View):

    def __init__(self, page: ft.Page):
        super(BottomBar, self).__init__(
            route="/",
            horizontal_alignment="center",
            vertical_alignment="center",
        )

        self.page = page

        self.controls = [
            ft.Text(
                text="Hello, World!",
                font_size=30,
                color="black",
            ),
            ft.Button(
                text="Click me!",
                on_click=self.on_click,
            ),
        ]