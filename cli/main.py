import requests
from functions import check_server_status, get_unix_times

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
