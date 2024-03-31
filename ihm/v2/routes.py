from flet_route import path
from middlewares.url_middleware import UrlBasedMiddleware
from views.index_view import IndexView
from views.login_view import LoginView
from views.profile_view import ProfileView
from views.change_deck_view import ChangeDeckView
from views.next_view import NextView


app_routes = [
    path(
        url="/",
        clear=True,
        view=IndexView().view
    ),
    path(
        url="/login",
        clear=False,
        view=LoginView().view,
    ),
    path(
        url="/profile",
        clear=True,
        view=ProfileView().view
    ),
    path(
        url="/change-deck/:current_deck_id",
        clear=True,
        view=ChangeDeckView().view
    ),

]

