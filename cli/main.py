import requests

API_BASE_URL = "http://127.0.0.1:8000" 


def check_server_status():
    response = requests.get(f"{API_BASE_URL}/")
    if response.status_code == 200:
        print("Le serveur est en ligne.")
    else:
        print("Le serveur est hors ligne.")


def get_unix_times():
    response = requests.get(f"{API_BASE_URL}/unixTimes")
    if response.status_code == 200:
        unix_times = response.json()
        print("Temps UNIX:", unix_times)
    else:
        print("Impossible de récupérer le temps UNIX.")

def main():
    print("Bienvenue dans le CLI de l'API NotaBene.")
    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Vérifier l'état du serveur")
        print("2. Récupérer les temps UNIX")

        choice = input("Entrez le numéro de l'action souhaitée : ")

        if choice == "1":
            check_server_status()
        elif choice == "2":
            get_unix_times()
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    main()
