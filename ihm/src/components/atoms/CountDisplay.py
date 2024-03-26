import flet as ft

class CountDisplay(ft.UserControl):

    def __init__(self, value: str = "0", label: str = "label"):
        super().__init__()
        self.value = value
        self.label = label

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(
                    self.value,
                    size=22,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    self.label,
                    size=14,
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
