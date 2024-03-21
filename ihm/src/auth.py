import flet as ft

API_URL = "http://gelk.fr:8090"

def get_auth_header(page: ft.Page):
    token = page.client_storage.get("token")
    return {
        "Authorization": f"Bearer {token}"
    }