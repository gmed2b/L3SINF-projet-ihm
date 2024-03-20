import requests, json

API_BASE_URL = "http://127.0.0.1:8000"
HEADER = {"Content-Type": "application/json"}


def load_previous_token():
    """
    Charge le token précédemment utilisé.
    """
    try:
        with open("token.txt", "r") as file:
            token = file.read()
            HEADER["Authorization"] = f"Bearer {token}"
            print("Token chargé avec succès.")
    except FileNotFoundError:
        print("Aucun token n'a été trouvé.")


def save_token(token):
    """
    Sauvegarde le token dans un fichier.
    """
    with open("token.txt", "w") as file:
        file.write(token)
        print("Token sauvegardé avec succès.")


def check_server_status():
    """
    Verifie l'état du serveur.
    """
    response = requests.get(f"{API_BASE_URL}/")
    if response.status_code == 200:
        print("Le serveur est en ligne.")
    else:
        print("Le serveur est hors ligne.")


def get_unix_times():
    """
    Réccupère les temps UNIX.
    """
    response = requests.get(f"{API_BASE_URL}/unixTimes")
    if response.status_code == 200:
        unix_times = response.json()
        print("Temps UNIX:", unix_times)
    else:
        print("Impossible de récupérer le temps UNIX.")

def login(username, password):
    """
    Authentifie l'utilisateur et récupère le token, modifie la variable globale TOKEN avec un effet de bord.
    """
    response = requests.post(f"{API_BASE_URL}/token", data={"username": username, "password": password})
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        HEADER["Authorization"] = f"Bearer {access_token}"
        save_token(access_token)

        print("Authentification réussie. \nVotre token est:", access_token)
    else:
        print("Authentification échouée. ", response.json()["detail"])

def get_user_info():
    """
    Récupère les informations de l'utilisateur.
    """
    response = requests.get(f"{API_BASE_URL}/users/me",headers = HEADER)
    if response.status_code == 200:
        user_info = response.json()
        print("Informations de l'utilisateur:", user_info)
    else:
        print("Impossible de récupérer les informations de l'utilisateur.")

def add_deck(deck_name):
    """
    Ajoute un deck.
    """
    response = requests.post(f"{API_BASE_URL}/addDeck", headers = HEADER, json={
        "name": deck_name
    })
    if response.status_code == 200:
        print("Deck ajouté avec succès.")
    else:
        print("Impossible d'ajouter le deck.", response.json())

def get_all_decks():
    """
    Récupère tous les decks de l'utilisateur.
    """
    response = requests.get(f"{API_BASE_URL}/getAllDecks", headers = HEADER)
    if response.status_code == 200:
        decks = response.json()
        print("Decks:", json.dumps(decks, indent=4))
    else:
        print("Impossible de récupérer les decks.")

def get_deck(deck_id):
    """
    Récupère un deck spécifique.
    """
    response = requests.get(f"{API_BASE_URL}/getDeck/{deck_id}", headers = HEADER)
    if response.status_code == 200:
        deck = response.json()
        print("Deck:", json.dumps(deck, indent=4))
    else:
        print("Impossible de récupérer le deck.")

def add_card(deck_id, front_content, back_content):
    """
    Ajoute une carte à un deck.
    """
    response = requests.post(
        f"{API_BASE_URL}/addCard",
        headers = HEADER,
        params={"deck_id": deck_id},
        json={"front_content": front_content, "back_content": back_content}
    )
    if response.status_code == 200:
        print("Carte ajoutée avec succès.")
    else:
        print("Impossible d'ajouter la carte.")

def update_state_card(card_id, new_state):
    """
    Met à jour l'état d'une carte.
    """
    response = requests.put(f"{API_BASE_URL}/updateCard/{card_id}", headers = HEADER, json={"new_state": new_state})
    if response.status_code == 200:
        print("État de la carte mis à jour avec succès.")
    else:
        print("Impossible de mettre à jour l'état de la carte.")

def get_random_card(deck_id):
    """
    Récupère une carte aléatoire.
    """
    response = requests.get(f"{API_BASE_URL}/getRandomCard/{deck_id}", headers = HEADER)
    if response.status_code == 200:
        card = response.json()
        return card
    else:
        print("Impossible de récupérer une carte aléatoire.")
        return None
    