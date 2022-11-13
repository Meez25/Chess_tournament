from abc import ABC, abstractmethod
import sys
import os


class MenuManager:
    _state = None

    def __init__(self, state) -> None:
        self.transition_to(state)
        self.view = state.view
        self.view.clean_console()
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
    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager

    def print_menu(self) -> None:
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_main_menu()

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.menu_manager.transition_to(Tournament_menu(self.view, self.tournament_manager, self.player_manager))
        elif user_option == "2":
            self.menu_manager.transition_to(Player_menu(self.view, self.player_manager, self.tournament_manager))
        elif user_option == "3":
            self.go_back()
        self.view.clean_console()
        self.view.show_banner()

    def go_back(self) -> None:
        sys.exit()


class Tournament_menu(State):
    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager

    def print_menu(self) -> None:
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_tournament_menu(self.tournament_manager.get_tournament())

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.view.clean_console()
            self.view.show_banner()
            self.tournament_manager.create_tournament()
        if user_option == "2":
            self.view.clean_console()
            self.view.show_banner()
            self.tournament_manager.display_all_tournament()
        if user_option == "3":
            self.view.clean_console()
            self.view.show_banner()
            if not self.tournament_manager.get_tournament():
                self.view.display_no_tournament_selected()
                self.view.press_enter_to_continue()
            else:
                self.menu_manager.transition_to(Add_player_to_tournament(self.view, self.tournament_manager, self.player_manager))
        if user_option == "4":
            self.view.clean_console()
            self.view.show_banner()
            self.tournament_manager.change_selected_tournament()
        if user_option == "5":
            self.view.clean_console()
            self.view.show_banner()
            self.tournament_manager.delete_tournament()
        if user_option == "6":
            self.view.clean_console()
            self.view.show_banner()
            self.tournament_manager.handle_tournament()
        elif user_option == "7":
            self.go_back()
        self.view.clean_console()
        self.view.show_banner()

    def go_back(self) -> None:
        self.menu_manager.transition_to(Main_menu(self.view, self.tournament_manager, self.player_manager))


class Player_menu(State):
    def __init__(self, view, player_manager, tournament_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_player_menu()

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.view.clean_console()
            self.view.show_banner()
            self.player_manager.create_player()
        if user_option == "2":
            self.view.clean_console()
            self.view.show_banner()
            self.player_manager.display_all_players()
        elif user_option == "3":
            self.go_back()
        

    def go_back(self) -> None:
        self.menu_manager.transition_to(Main_menu(self.view, self.tournament_manager, self.player_manager))

    
class Add_player_to_tournament(State):
    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_add_player_to_tournament(self.tournament_manager.get_tournament())

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.view.clean_console()
            self.view.show_banner()
            player = self.player_manager.create_player()
            self.tournament_manager.add_player_to_tournament(player)
            print("worked ?")
        elif user_option == "2":
            self.view.clean_console()
            self.view.show_banner()
            self.tournament_manager.add_existing_player_to_tournament()
        elif user_option == "3":
            self.view.clean_console()
            self.view.show_banner()
            self.tournament_manager.display_tournament_players()
        elif user_option == "4":
            self.view.clean_console()
            self.view.show_banner()
            self.tournament_manager.remove_player_from_tournament()
        elif user_option == "5":
            self.go_back()
        

    def go_back(self) -> None:
        self.menu_manager.transition_to(Tournament_menu(self.view, self.tournament_manager, self.player_manager))
