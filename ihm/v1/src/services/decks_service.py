import requests, flet as ft
from src.auth import API_URL, get_auth_header


def fetch_active_deck(page: ft.page):
    response = requests.get(
        f"{API_URL}/users/active-deck",
        headers=get_auth_header(page)
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la récupération du deck actif")
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


def fetch_deck(page: ft.Page, deck_id: int):
    response = requests.get(
        f"{API_URL}/decks/{deck_id}",
        headers=get_auth_header(page)
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la récupération du deck")
    else:
        return response.json()


def update_deck(page: ft.Page, deck_id: int, deck: dict):
    response = requests.put(
        f"{API_URL}/decks/{deck_id}",
        headers=get_auth_header(page),
        json=deck
    )

    if response.status_code != 200:
        raise Exception("Erreur lors de la mise à jour du deck")
    else:
        return response.json()