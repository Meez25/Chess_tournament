from abc import ABC, abstractclassmethod

class View:

    _state = None

    def __init__(self, state):
        self.setState(state)

    def setState(self, state):
        self._state = state
        self._state.view = self

    def presentState(self):
        print(f"View is in {type(self._state).__name__}")

    def method_one(self):
        self._state.method_one()

    def method_two(self):
        self._state.method_two()

    def show_welcome_message(self):
        print("Welcome !")

    def show_main_menu(self):
        print("1. Créer un tournoi")
        return input("Que voulez-vous faire ? ")

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
    def method_one(self):
        pass

    @abstractclassmethod
    def method_two(self):
        pass

class main_menu(State):
    def method_one(self):
        print("main_menu method one")

    def method_two(self):
        print("main_menu method two")

class second_menu(State):
    def method_one(self):
        print("second_menu method one")

    def method_two(self):
        print("second_menu method two")

