import flet as ft
from flet_core.control_event import ControlEvent


def main(page: ft.Page):
    page.title = "Simple Calculator"
    page.window_width = 300
    page.window_height = 420
    page.window_min_width = 300
    page.window_min_height = 420
    page.window_max_width = 300
    page.window_max_height = 420
    page.padding = ft.Padding(15, 15, 15, 15)
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed="orange")

    def handle_clear(e: ControlEvent):
        TextResult.value = "0"
        PartialResult.value = ""
        page.update()

    def handle_val(e: ControlEvent):
        if TextResult.value == "0" and e.control.text != ".":
            TextResult.value = e.control.text
        else:
            TextResult.value = TextResult.value + e.control.text
        page.update()

    def handle_equal(e: ControlEvent):
        result = str(eval(str(TextResult.value)))
        TextResult.value = str(result)
        if result == "69":
            PartialResult.value = "send nudes <3"
        page.update()

    PartialResult = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.W_600,
    )
    TextResult = ft.Text(
        value="0",
        size=48,
        weight=ft.FontWeight.BOLD,
        no_wrap=True,
    )

    page.add(
        ft.SafeArea(
            ft.Column(controls=[
                PartialResult,
                TextResult,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("C", width=60, on_click=handle_clear, bgcolor=ft.colors.PRIMARY_CONTAINER),
                        ft.ElevatedButton("/", width=60, on_click=handle_val, bgcolor=ft.colors.PRIMARY_CONTAINER),
                    ],
                    alignment=ft.MainAxisAlignment.END
                ),
                ft.Row(controls=[
                    ft.ElevatedButton("7", width=60, on_click=handle_val),
                    ft.ElevatedButton("8", width=60, on_click=handle_val),
                    ft.ElevatedButton("9", width=60, on_click=handle_val),
                    ft.ElevatedButton("*", width=60, on_click=handle_val, bgcolor=ft.colors.PRIMARY_CONTAINER),
                ]),
                ft.Row(controls=[
                    ft.ElevatedButton("4", width=60, on_click=handle_val),
                    ft.ElevatedButton("5", width=60, on_click=handle_val),
                    ft.ElevatedButton("6", width=60, on_click=handle_val),
                    ft.ElevatedButton("-", width=60, on_click=handle_val, bgcolor=ft.colors.PRIMARY_CONTAINER),
                ]),
                ft.Row(controls=[
                    ft.ElevatedButton("1", width=60, on_click=handle_val),
                    ft.ElevatedButton("2", width=60, on_click=handle_val),
                    ft.ElevatedButton("3", width=60, on_click=handle_val),
                    ft.ElevatedButton("+", width=60, on_click=handle_val, bgcolor=ft.colors.PRIMARY_CONTAINER),
                ]),
                ft.Row(controls=[
                    ft.ElevatedButton("0", width=130, on_click=handle_val),
                    ft.ElevatedButton(".", width=60, on_click=handle_val),
                    ft.ElevatedButton("=", width=60, on_click=handle_equal, bgcolor=ft.colors.PRIMARY_CONTAINER)
                ]),
            ])
        )
    )


ft.app(main)
