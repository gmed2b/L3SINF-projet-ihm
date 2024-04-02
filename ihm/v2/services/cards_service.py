import requests, flet as ft
from auth import API_URL, get_auth_header
from enums.CardStatus import CardStatus


def create_card(page: ft.Page, deck_id: int, card_name: str, card_content: str):
    response = requests.post(
        f"{API_URL}/cards",
        headers=get_auth_header(page),
        params={"deck_id": deck_id},
        json={
            "front_content": card_name,
            "back_content": card_content
        }
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la création de la carte")
    else:
        return response.json()


def update_card_status(page: ft.Page, card_id: int, status: CardStatus):
    response = requests.patch(
        f"{API_URL}/cards/{card_id}",
        headers=get_auth_header(page),
        params={"state": status}
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la mise à jour de la carte")
    else:
        return response.json()