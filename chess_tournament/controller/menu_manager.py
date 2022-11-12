from abc import ABC, abstractmethod
import sys
import os


class MenuManager:
    _state = None

    def __init__(self, state) -> None:
        self.transition_to(state)
        self.view = state.view
        os.system("cls" if os.name == "nt" else "clear")
        self.view.show_banner()

    def transition_to(self, state):
        self._state = state
        self._state.menu_manager = self

    def print_menu(self):
        self._state.print_menu()

    def get_user_option(self):
        return self._state.get_user_option()

    def go_back(self):
        self._state.go_back()


class State(ABC):
    @property
    def menu_manager(self) -> MenuManager:
        return self._menu_manager

    @menu_manager.setter
    def menu_manager(self, menu_manager: MenuManager) -> None:
        self._menu_manager = menu_manager

    @abstractmethod
    def go_back(self) -> None:
        pass


class Main_menu(State):
    def __init__(self, view) -> None:
        self.view = view

    def print_menu(self) -> None:
        self.view.print(
            f"Que voulez-vous faire ?\n\n"
            f"          1 : Créer un tournoi\n"
            f"          2 : Gérer les joueurs\n"
            f"          3 : Quitter l'application\n"
        )

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.menu_manager.transition_to(Tournament_menu(self.view))
        elif user_option == "2":
            self.menu_manager.transition_to(Player_menu(self.view))
        elif user_option == "3":
            self.go_back()
        os.system("cls" if os.name == "nt" else "clear")
        self.view.show_banner()

    def go_back(self) -> None:
        sys.exit()


class Tournament_menu(State):
    def __init__(self, view) -> None:
        self.view = view

    def print_menu(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        self.view.show_banner()
        self.view.print(
            f"Que voulez-vous faire ?\n\n"
            f"          1 : Créer un tournoi\n"
            f"          2 : Retour\n"
        )

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            return "Create tournament"
        elif user_option == "2":
            self.menu_manager.transition_to(Main_menu(self.view))
        os.system("cls" if os.name == "nt" else "clear")
        self.view.show_banner()

    def go_back(self) -> None:
        self.menu_manager.transition_to(Main_menu(self.view))


class Player_menu(State):
    def __init__(self, view) -> None:
        self.view = view

    def print_menu(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        self.view.show_banner()
        self.view.print(
            f"Que voulez-vous faire ?\n\n"
            f"          1 : Ajouter un joueur\n"
            f"          2 : Voir la liste des joueurs\n"
            f"          3 : Retour\n"
        )

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            return f"Add a player"
        if user_option == "2":
            return f"See list of players"
        elif user_option == "3":
            self.menu_manager.transition_to(Main_menu(self.view))
        

    def go_back(self) -> None:
        self.menu_manager.transition_to(Main_menu(self.view))

    
