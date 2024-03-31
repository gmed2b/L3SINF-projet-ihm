import flet as ft

def Snack(page: ft.Page, message: str, bgcolor=ft.colors.RED_400, duration=2000):
    page.snack_bar = ft.SnackBar(
        ft.Text(message),
        behavior=ft.SnackBarBehavior.FLOATING,
        bgcolor=bgcolor,
        duration=duration
    )
    page.snack_bar.open = True
    page.update()
