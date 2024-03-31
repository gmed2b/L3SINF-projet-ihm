import requests, flet as ft
from auth import API_URL, get_auth_header

def fetch_user_info(page: ft.Page):
    response = requests.get(
        f"{API_URL}/users/me",
        headers=get_auth_header(page)
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la récupération des informations de l'utilisateur")
    else:
        return response.json()


def fetch_random_card(page: ft.Page):
    response = requests.get(
        f"{API_URL}/train/",
        headers=get_auth_header(page)
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la récupération de la carte")
    else:
        return response.json()


def fetch_decks(page: ft.Page):
    response = requests.get(
        f"{API_URL}/decks",
        headers=get_auth_header(page)
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la récupération des decks")
    else:
        return response.json()


def update_active_deck(page: ft.Page, deck_id: int):
    response = requests.patch(
        f"{API_URL}/users/active-deck",
        headers=get_auth_header(page),
        params={
            "deck_id": deck_id
        }
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la mise à jour du deck actif")
    else:
        return response.json()