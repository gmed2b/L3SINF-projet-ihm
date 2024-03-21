import flet as ft

class AddcardPage(ft.View):

    def __init__(self, page: ft.Page):
        super(AddcardPage, self).__init__()
        self.page = page
        self.page.title = "Addcard page"

        self.controls = [
            ft.Container(
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                    width=500,
                    controls=[
                        ft.Text("Créer une carte", size=30),
                        ft.CupertinoTextField(
                            placeholder_text="Nom de la carte",
                        ),
                        ft.CupertinoTextField(
                            placeholder_text="Description",
                            multiline=True,
                            min_lines=5,
                        ),
                        ft.ElevatedButton("Créer"),
                    ],
                ),
            ),
        ]