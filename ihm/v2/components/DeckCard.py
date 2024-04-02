import requests, flet as ft
from services.cards_service import update_card_status
import services.user_service as us
import services.decks_service as ds
from enums.CardStatus import CardStatus
from components.Snack import Snack


def DeckCard(page: ft.Page, deck: dict) -> ft.Container:

    def on_deck_click(e):
        page.go(f"/decks/{e.control.data}")


    return ft.Container(
        data=deck["id"],
        on_click=lambda e: on_deck_click(e),
        content=ft.Card(
            color=deck["color"],
            content=ft.Container(
                padding=ft.padding.all(10),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row([
                            VisibilityBadge(deck["visibility"]),
                        ]),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    value=deck["name"],
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ]
                        ),
                        ft.Row([
                            ft.Text(
                                f"{len(deck['cards'])} carte{'s' if len(deck['cards']) > 1 else ''}",
                                size=16
                            )
                        ]),
                    ]
                )
            ),
        )
    )


def VisibilityBadge(text: str):
    return ft.Card(
        content=ft.Container(
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            content=ft.Row(
                spacing=5,
                controls=[
                    VisibilityIcon(text),
                    ft.Text(text.capitalize())
                ]
            )
        )
    )


def VisibilityIcon(text: str):
    VIcons = ft.icons.LOCK
    if text == "public":
        VIcons = ft.icons.PUBLIC
    elif text == "friends":
        VIcons = ft.icons.PEOPLE_OUTLINE

    return ft.Icon(
        name=VIcons,
        color=ft.colors.GREY_500,
        size=18,
    )