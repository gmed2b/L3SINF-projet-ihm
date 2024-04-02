from flet_route import path
from views.index_view import IndexView
from views.login_view import LoginView
from views.profile_view import ProfileView
from views.change_deck_view import ChangeDeckView
from views.deck_view import DeckView
from views.new_deck_view import NewDeckView
from views.new_card_view import NewCardView
from views.edit_card_view  import EditCardView


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
    path(
        url="/decks/new",
        clear=True,
        view=NewDeckView().view
    ),
    path(
        url="/decks/:deck_id",
        clear=True,
        view=DeckView().view
    ),
    path(
        url="/decks/:deck_id/cards/new",
        clear=True,
        view=NewCardView().view
    ),
    path(
        url="/decks/:deck_id/cards/:card_id",
        clear=True,
        view=EditCardView().view
    ),

]

