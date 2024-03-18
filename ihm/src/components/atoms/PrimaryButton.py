import flet as ft

class PrimaryButton(ft.UserControl):

    def __init__(self, text: str = "Primary Button", on_click=None):
        super().__init__()
        self.text = text
        self.on_click = on_click

    def build(self) -> ft.CupertinoButton:
        return ft.CupertinoButton(
            content=ft.Text(self.text, color=ft.colors.WHITE),
            bgcolor=ft.colors.GREEN_ACCENT_700,
            alignment=ft.alignment.top_left,
            border_radius=ft.border_radius.all(5),
            opacity_on_click=0.5,
            on_click=self.on_click
        )
