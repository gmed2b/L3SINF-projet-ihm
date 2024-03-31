import requests, flet as ft
from auth import API_URL, get_auth_header
from flet_route import Params,Basket

class AppBasedMiddleware:
    def __init__(self):
        ...

    def call_me(self, page:ft.Page, params:Params, basket:Basket):
        self.page = page

        self.verify_token()


    def verify_token(self):
        token = self.page.client_storage.get("access_token")
        if not token:
            self.page.go("/login")
            return

        response = requests.get(
            f"{API_URL}/users/me",
            headers=get_auth_header(self.page)
        )
        if response.status_code != 200:
            self.page.go("/login")
            return
