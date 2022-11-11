from abc import ABC, abstractclassmethod
import sys

class View:

    _state = None

    def __init__(self, state):
        self.setState(state)

    def setState(self, state):
        self._state = state
        self._state.view = self

    def presentState(self):
        return self._state

    def print_menu(self):
        self._state.print_menu()

    def get_user_option(self):
        self._state.get_user_option()

    def show_welcome_message(self):
        print(f"{bcolors.OKBLUE}"
        f"  _____                            _       _ _   __      _               \n"
        f" |_   _|__  _   _ _ __ _ __   ___ (_)   __| ( ) /_/  ___| |__   ___  ___ \n"
        f"   | |/ _ \| | | | '__| '_ \ / _ \| |  / _` |/ / _ \/ __| '_ \ / _ \/ __|\n"
        f"   | | (_) | |_| | |  | | | | (_) | | | (_| | |  __/ (__| | | |  __/ (__ \n"
        f"   |_|\___/ \__,_|_|  |_| |_|\___/|_|  \__,_|  \___|\___|_| |_|\___|\___|\n"
        f"{bcolors.ENDC}")

    def ask_player_last_name(self):
        last_name = input("Nom de famille ? : ")
        return last_name

    def display_empty_last_name_error(self):
        print("Désolé, le nom du joueur n'a pas été renseigné.")

    def ask_player_first_name(self):
        first_name = input("Prénom ? : ")
        return first_name

    def display_empty_first_name_error(self):
        print("Désolé, le prénom du joueur n'a pas été renseigné.")

    def ask_player_birthday(self):
        birthday = input("Date de naissance ? : ")
        return birthday

    def display_empty_birthday_error(self):
        print("Désolé, la date de naissance n'a pas été renseigné.")

    def ask_player_sex(self):
        sex = input("Sexe ? : ")
        return sex

    def display_empty_sex_error(self):
        print("Désolé, le sexe n'a pas été renseigné.")

    def ask_player_elo(self):
        elo = input("Elo ? : ")
        return elo

    def display_empty_elo_error(self):
        print("Le elo n'a pas été renseigné.")

    def display_elo_not_number_error(self):
        print("Le elo doit être composé de chiffre.")

    def ask_start_tournament(self, tournament_name):
        ready = input(f"Prêt à démarrer le tournoi {tournament_name} ? o/n ")
        return ready

    def display_yes_or_no_error(self):
        print("La réponse doit être 'o' ou 'n'")

    def announce_matches(self):
        print("Voici la liste des matchs à jouer : ")

    def display_nth_round_games(self, player1, player2):
        print(f"{player1.last_name} {player1.first_name} contre "
        f"{player2.last_name} {player2.first_name}")

    def ask_results(self, player):
        score_player = input(f"Quel est le résultat de"
        f" {player.last_name} {player.first_name} ? (0, 0.5, 1) ")
        return score_player

    def display_score_error(self):
        print(f"Le score ne peut être que 0, 0,5 ou 1.")
        

class State(ABC):
    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, view):
        self._view = view

    @abstractclassmethod
    def print_menu(self):
        pass

    @abstractclassmethod
    def get_user_option(self):
        pass

class main_menu(State):
    def print_menu(self):
        print(f"Que voulez-vous faire ? \n"
        f"          1 : Créer un nouveau tournoi\n"
        f"          2 : Ajouter des nouveaux joueurs\n"
        f"          3 : Quitter\n")

    def get_user_option(self):
        user_option = input("Entrez votre choix : ")
        if user_option == '1':
            self.view.setState(tournament_menu())
        if user_option == '3':
            sys.exit()

class tournament_menu(State):
    def print_menu(self):
        print(f"Que voulez-vous faire ? \n"
        f"          1 : Créer un nouveau tournoi\n"
        f"          2 : Ajouter des nouveaux joueurs\n"
        f"          3 : Retour\n")

    def get_user_option(self):
        user_option = input("Entrez votre choix : ")
        if user_option == '3':
            self.view.setState(main_menu())


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

