import requests
from functions import check_server_status, get_unix_times, login, get_user_info, add_deck, get_all_decks, get_deck, add_card, update_state_card, get_random_card
from api_service import ApiService

def main():
    print("Bienvenue dans le CLI de l'API NotaBene.\n")

    apiService = ApiService()

    # 1 - Se connecter
    print("Veuillez vous connecter.")
    username = input("Entrez votre email : ")
    password = input("Entrez votre mot de passe : ")

    apiService.login(username, password)

    # 2 - Afficher le menu
    while True:
        print("Que souhaitez-vous faire ?")
        print("1. Entraine toi ! ")
        print("2. Récupérer les informations de l'utilisateur")
        print("3. Ajouter un deck")
        print("4. Récupérer l'ensemble de vos decks")
        print("5. Récupérer un deck en particulier")
        print("6. Ajouter une carte à un deck")
        # print("10.A . Modifier l'état d'une carte")
        # print("10.B . Tire une carte aléatoirement")

        choice = input("Entrez le numéro de l'action souhaitée : ")

        if choice == "1":
            check_server_status()
        elif choice == "2":
            get_unix_times()
        elif choice == "3":
            username = input("Entrez votre email : ")
            password = input("Entrez votre mot de passe : ")
            login(username, password)
        elif choice == "4":
            get_user_info()
        elif choice == "5":
            deck_name = input("Entrez le nom du deck à ajouter : ")
            add_deck(deck_name)
        elif choice == "6":
            get_all_decks()
        elif choice == "7":
            deck_id = input("Entrez l'ID du deck à récupérer : ")
            get_deck(deck_id)
        elif choice == "8":
            deck_id = input("Entrez l'ID du deck où ajouter la carte : ")
            front_content = input("Entrez la question de la carte : ")
            back_content = input("Entrez la réponse de la carte : ")
            add_card(deck_id, front_content, back_content)
        elif choice == "9":
            deck_id = input("Entrez l'ID du deck où ajouter la carte : ")
            front_content = input("Entrez la question de la carte : ")
            back_content = input("Entrez la réponse de la carte : ")
            add_card(deck_id, front_content, back_content)
        elif choice == "10":
            card = get_random_card(deck_id)
            print(card.get("front_content"))
            print("Voulez-vous voir la réponse ?")
            response = input("Entrez 'oui' ou 'non' : ")
            if response == "oui":
                print(card.get("back_content"))
                print("La carte a-t-elle été mémorisée ?")
                response = input("Entrez 'not memorized' ou 'in progress' ou 'memorized: ")
                update_state_card(card.get("id"), response)
                print("État de la carte mis à jour avec succès.")
            else:
                print("Choix invalide. Veuillez entrer 'oui ou 'non'.")
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    main()
