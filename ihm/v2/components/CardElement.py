import requests, flet as ft
from services.cards_service import update_card_status
import services.user_service as us
import services.decks_service as ds
from interfaces.CardStatus import CardStatus
from components.Snack import Snack


def CardElement(page: ft.Page, card: dict, on_card_click=None) -> ft.Container:

    return ft.Container(
        data=card["id"],
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text(
                                        value=card["front_content"],
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    StateBadge(card["state"]),
                                ]
                            ),
                            ft.Text(
                                value=card["back_content"],
                                size=14,
                                color=ft.colors.GREY_600,
                            ),
                        ],
                    ),
                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                    bgcolor=ft.colors.GREY_100,
                    border_radius=ft.border_radius.all(10),
                    expand=True,
                ),

                ft.Card(
                    color=ft.colors.AMBER,
                    content=ft.IconButton(
                        icon=ft.icons.EDIT,
                        icon_color=ft.colors.WHITE,
                        on_click=lambda _: on_card_click and on_card_click(card),
                    ),
                )
            ]
        )
    )


def StateBadge(state: CardStatus):
    bgcolor = ft.colors.RED
    if state == CardStatus.IN_PROGRESS:
        bgcolor = ft.colors.BLUE
    elif state == CardStatus.MEMORIZED:
        bgcolor = ft.colors.GREEN

    return ft.Card(
        color=bgcolor,
        content=ft.Container(
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            content=ft.Row(
                spacing=5,
                controls=[
                    StateIcon(state),
                ]
            )
        )
    )


def StateIcon(state: CardStatus):
    VIcons = ft.icons.THUMB_DOWN
    if state == CardStatus.IN_PROGRESS:
        VIcons = ft.icons.THUMBS_UP_DOWN
    elif state == CardStatus.MEMORIZED:
        VIcons = ft.icons.THUMB_UP

    return ft.Icon(
        name=VIcons,
        color=ft.colors.WHITE,
        size=22,
    )