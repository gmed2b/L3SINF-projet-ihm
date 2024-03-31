import flet as ft

# The BottomNavigationBar component is a simple wrapper around the CupertinoNavigationBar component.
def BottomNavigationBar(page: ft.Page, selected_index: int = 1):

    return ft.CupertinoNavigationBar(
        bgcolor=ft.colors.TRANSPARENT,
        inactive_color=ft.colors.GREY,
        active_color=ft.colors.GREEN_ACCENT,
        selected_index=selected_index,
        on_change=lambda e: on_tab_change(e, page),
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Jouer"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Sac",
            ),
        ],
    )


def on_tab_change(e, page: ft.Page):
    match e.control.selected_index:
        case 0:
            page.go("/explore")
        case 1:
            page.go("/")
        case 2:
            page.go("/profile")
        case _:
            page.go("/")