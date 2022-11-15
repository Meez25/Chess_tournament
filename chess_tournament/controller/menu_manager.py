from abc import ABC, abstractmethod
from models.models import Progress
import sys


class MenuManager:
    """Class to handle the menus"""

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
    """Abstract class for State design pattern"""

    @property
    def menu_manager(self) -> MenuManager:
        return self._menu_manager

    @menu_manager.setter
    def menu_manager(self, menu_manager: MenuManager) -> None:
        self._menu_manager = menu_manager

    @abstractmethod
    def go_back(self) -> None:
        pass


class MainMenu(State):
    """First menu to appear at start of the app"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager

    def print_menu(self) -> None:
        """Display the main menu using the view"""
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_main_menu()

    def get_user_option(self) -> None:
        """Get the user options"""
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.menu_manager.transition_to(
                TournamentMenu(self.view, self.tournament_manager, self.player_manager)
            )
        elif user_option == "2":
            self.menu_manager.transition_to(
                PlayerMenu(self.view, self.player_manager, self.tournament_manager)
            )
        elif user_option == "3":
            self.menu_manager.transition_to(
                RapportMenu(self.view, self.player_manager, self.tournament_manager)
            )
        elif user_option == "4":
            self.go_back()
        self.view.clean_console()
        self.view.show_banner()

    def go_back(self) -> None:
        """Exit the program"""
        sys.exit()


class TournamentMenu(State):
    """Menu that handles the tournament"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager

    def print_menu(self) -> None:
        """Display the tournament menu by calling the view"""
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_tournament_menu(self.tournament_manager.get_tournament())

    def get_user_option(self) -> None:
        """Get the user options"""
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
            elif (
                self.tournament_manager.get_tournament_object().get_progression()
                != Progress.FIRST_ROUND
            ):
                self.view.tournament_playing_error()
                self.view.press_enter_to_continue()
            else:
                self.menu_manager.transition_to(
                    AddPlayerToTournament(
                        self.view, self.tournament_manager, self.player_manager
                    )
                )
        if user_option == "4":
            self.view.clean_console()
            self.view.show_banner()
            if not self.tournament_manager.get_list_of_all_tournament():
                self.view.no_tournament_error()
                self.view.press_enter_to_continue()
            else:
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
        """Go back previous menu"""
        self.menu_manager.transition_to(
            MainMenu(self.view, self.tournament_manager, self.player_manager)
        )


class PlayerMenu(State):
    """Menu for the player"""

    def __init__(self, view, player_manager, tournament_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        """Display the player menu by calling the view"""
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_player_menu()

    def get_user_option(self) -> None:
        """Get the user options"""
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.view.clean_console()
            self.view.show_banner()
            self.player_manager.create_player()
        if user_option == "2":
            self.view.clean_console()
            self.view.show_banner()
            self.player_manager.modify_player()
        if user_option == "3":
            self.view.clean_console()
            self.view.show_banner()
            self.player_manager.display_all_players()
        elif user_option == "4":
            self.go_back()

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            MainMenu(self.view, self.tournament_manager, self.player_manager)
        )


class AddPlayerToTournament(State):
    """Add player menu"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        """Display the menu to add a player"""
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_add_player_to_tournament(
            self.tournament_manager.get_tournament()
        )

    def get_user_option(self) -> None:
        """Get the user options"""
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.view.clean_console()
            self.view.show_banner()
            player = self.player_manager.create_player()
            self.tournament_manager.add_player_to_tournament(player)
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
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            TournamentMenu(self.view, self.tournament_manager, self.player_manager)
        )


class RapportMenu(State):
    """Menu for the player"""

    def __init__(self, view, player_manager, tournament_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        """Display the player menu by calling the view"""
        self.go_back()

    def get_user_option(self) -> None:
        ...

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            MainMenu(self.view, self.tournament_manager, self.player_manager)
        )
