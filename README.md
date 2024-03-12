# L3SINF Projet IHM - NotaBene

## Contexte

Dans ce projet, nous devons programmer une application avec une IHM.
Nous avons fait le choix de créer une application de révision basé sur l'auto-évaluation tout en suivant la courbe d'Ebbinghaus.
Notre inspiration se fonde sur l'application Anki, cependant elle est très peu intuitive et la mise en place est conséquente.

## Présentations

Voici les liens vers les différentes présentation montrés en classe :

- [Présentation calculatrice](https://www.canva.com/design/DAF9VJuEL5o/R7Plr9m7-TJSe962BasVXQ/view?utm_content=DAF9VJuEL5o&utm_campaign=designshare&utm_medium=link&utm_source=editor)
- [Présentation du projet - NotaBene](https://www.canva.com/design/DAF82SGmcXM/_xUJKaav0MRmMIPLK7CH1w/view?utm_content=DAF82SGmcXM&utm_campaign=designshare&utm_medium=link&utm_source=editor)

## Diagrammes

Nous avons créer un diagramme de cas d'utilisation pour notre application, la couverture minimal et un MCD ; vous pouvez les retrouver dans le dossier `assets/diagrammmes`.

## Maquettes

Nous avons créer des maquettes pour notre application, UI et UX ; vous pouvez les retrouver dans le dossier `assets/maquettes` ou sur les liens suivants :

- [Maquettes UI](https://www.figma.com/file/5vhr2PmggYpFcI74pYPpqj/UI?type=design&node-id=0%3A1&mode=design&t=CisRsQdiZqw1XuOh-1)
- [Maquettes UX](https://www.figma.com/file/Rn32dijtvrqSgnkOxDwRJ1/UX?type=whiteboard&node-id=0%3A1&t=uRaHr8N8dL72zMmX-1)

## Contributeurs

- Anthony Menghi
- Jacques Battaglini
- Mehdi Ghoulam

## Technologies

- IHM : Flet (Flutter avec Python)
- API : FastAPI (Python)

## Architecture

```bash
.
├── README.md
├── ihm
├── api
├── cli
├── assets
│   ├── diagrammes
│   └── maquettes
├── docker-compose.yml
└── exemple.env
```

- `api` : Dossier contenant l'API
- `cli` : Dossier contenant la CLI
- `assets` : Dossier contenant les assets du projet
  - `diagrammes` : Dossier contenant les diagrammes du projet (cas d'utilisation, couverture minimal et MCD)
  - `maquettes` : Dossier contenant les maquettes du projet (UI, UX)
- `docker-compose.yml` : Fichier de configuration pour Docker
- `exemple.env` : Fichier d'exemple pour les variables d'environnement

## Installation

1. Avoir `docker` et `docker-compose` d'installé sur votre machine.
2. Cloner le projet.
3. Créer un fichier `.env` à la racine du projet en suivant le fichier `exemple.env`
4. Lancer la commande `make run-api` à la racine du projet
5. Lancer l'application flet avec la commande `make run-ihm` à la racine du projet
6. Lancer la CLI `cd cli && python3 main.py`

### Aide 
Nous pouvons tester la connexion à la base de données avec `psql -h localhost -p 5432 -U name_user -d name_db` 

Verifier que vous n'avez pas d'autre service qui utilise le port 5432.