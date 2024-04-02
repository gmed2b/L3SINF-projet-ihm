import requests, flet as ft
from services.cards_service import update_card_status
import services.user_service as us
from enums.CardStatus import CardStatus
from components.Snack import Snack

def FlashCard(page: ft.Page) -> ft.Container:

    def get_random_card():
        try:
            random_picked_card = us.fetch_random_card(page)
            return random_picked_card

        except Exception as e:
            Snack(page, str(e))


    def toggle_card_animation(e):
        CardHolder.content = BackCard if CardHolder.content == FrontCard else FrontCard
        ButtonHolder.content = RevealButton if CardHolder.content == FrontCard else ThumbsRow

        page.update()


    def save_card_state(card_id: int, status: CardStatus):
        try:
            updated_card = update_card_status(page, card_id, status)
            toggle_card_animation(None)

            random_picked_card = get_random_card()
            FrontCardText.value = random_picked_card["front_content"]
            BackCardText.value = random_picked_card["back_content"]
            page.update()

        except Exception as e:
            Snack(page, str(e))
            return False


    random_picked_card = get_random_card()

    # Face recto de la carte
    FrontCardText = ft.Text(
        value=random_picked_card["front_content"],
        size=22, text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD
    )
    FrontCard = ft.Card(
        content=ft.Container(
            content=FrontCardText,
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            width=300,
            height=300,
            border_radius=10,
        ),
    )

    # Face verso de la carte
    BackCardText = ft.Text(
        value=random_picked_card["back_content"],
        size=16
    )
    BackCard = ft.Card(
        content=ft.Container(
            content=BackCardText,
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            width=300,
            height=300,
            border_radius=10,
        ),
    )

    # Conteneur anim des deux faces
    CardHolder = ft.AnimatedSwitcher(
        content=FrontCard,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=500,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    # Bouton pour révéler la carte
    RevealButton = ft.CupertinoButton(
        "Révéler",
        bgcolor=ft.colors.GREEN_ACCENT_700,
        on_click=toggle_card_animation,
    )

    # Variable contenant les boutons "pouce"
    ThumbsRow = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.icons.THUMB_UP,
                icon_color="white",
                bgcolor=ft.colors.GREEN_ACCENT_700,
                on_click=lambda e: save_card_state(random_picked_card["id"], CardStatus.MEMORIZED),
            ),
            ft.IconButton(
                icon=ft.icons.THUMBS_UP_DOWN,
                icon_color="white",
                bgcolor=ft.colors.ORANGE_ACCENT_700,
                on_click=lambda e: save_card_state(random_picked_card["id"], CardStatus.IN_PROGRESS),
            ),
            ft.IconButton(
                icon=ft.icons.THUMB_DOWN,
                icon_color="white",
                bgcolor=ft.colors.RED_ACCENT_700,
                on_click=lambda e: save_card_state(random_picked_card["id"], CardStatus.NOT_MEMORIZED),
            ),
        ],
    )

    # Variable de gestion des boutons
    ButtonHolder = ft.Container(
        content=RevealButton,
    )

    return ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            controls=[
                CardHolder, # Carte
                ButtonHolder, # Bouton(s)
            ],
        ),
    )
