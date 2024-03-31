import requests, flet as ft
from auth import API_URL, get_auth_header
from interfaces.CardStatus import CardStatus


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