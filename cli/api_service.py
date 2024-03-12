import requests

class ApiService:
    """
    Cette classe permet de gérer les appels à l'API
    """

    def __init__(self):
        self.API_BASE_URL = "http://127.0.0.1:8000"
        self.HEADER = {"Content-Type": "application/json"}
        self.ACCESS_TOKEN = ""

        if (self.load_previous_session()):
            print("Session précédente chargée.")


    def set_access_token(self, access_token):
        """
        Modifie l'attribut ACCESS_TOKEN et HEADER. Enregistre le token dans un fichier.
        """
        self.ACCESS_TOKEN = access_token
        self.HEADER["Authorization"] = f"Bearer {self.ACCESS_TOKEN}"
        self.save_access_token()


    def save_access_token(self):
        """
        Enregistre le token dans un fichier.
        """
        try:
            with open("token.txt", "w") as file:
                file.write(self.ACCESS_TOKEN)
        except Exception as e:
            print("Impossible d'enregistrer le token.", e)


    def load_previous_session(self):
        """
        Charge si possible le token de la session précédente.
        Renvoie True si le token a été chargé, False sinon.
        @return: bool
        """
        try:
            with open("token.txt", "r") as file:
                readed_token = file.read()
                if readed_token:
                    self.set_access_token(readed_token)
                    return True
            return False
        except Exception as e:
            print("Impossible de charger la session précédente.")


    def login(self, username, password):
        """
        Authentifie l'utilisateur et enregistre le token.
        @param username: str
        @param password: str
        @return: None
        """
        response = requests.post(
            f"{self.API_BASE_URL}/token",
            data={"username": username, "password": password}
        )
        if response.status_code == 200:
            access_token = response.json()["access_token"]
            self.set_access_token(access_token)
            print("Authentification réussie.")
            print("Votre token est:", access_token)
        else:
            print("Authentification échouée.")