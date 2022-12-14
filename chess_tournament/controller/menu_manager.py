import sys
from abc import ABC, abstractmethod


from chess_tournament.models.models import Progress, Tournament  # type:ignore
from chess_tournament.view.tournament_manager_view import TournamentManagerView


class MenuManager:
    """Class to handle the menus"""

    _state = None

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.view = view
        self.state = MainMenu(self.view, self.tournament_manager, self.player_manager)
        self.transition_to(self.state)
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
                PlayerMenu(self.view, self.tournament_manager, self.player_manager)
            )
        elif user_option == "3":
            self.menu_manager.transition_to(
                ReportMenu(self.view, self.tournament_manager, self.player_manager)
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
        self.view.display_tournament_menu(self.tournament_manager.get_tournament_name())

    def get_user_option(self) -> None:
        """Get the user options"""
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.create_tournament()
        if user_option == "2":
            self.display_all_tournament()
        if user_option == "3":
            self.display_add_player_to_tournament_menu()
        if user_option == "4":
            self.view.clean_console()
            self.view.show_banner()
            if not self.tournament_manager.tournament_list:
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

    def create_tournament(self):
        """Option to create the tournament"""
        self.prepare_display()
        self.tournament_manager.create_tournament()

    def display_all_tournament(self):
        """Option to display all tournaments"""
        self.prepare_display()
        self.tournament_manager.display_all_tournament()

    def check_if_selected_tour(self):
        """Check if there is a selected tour"""
        if not self.tournament_manager.get_tournament_name():
            return False
        else:
            return True

    def check_if_tour_playing(self):
        """Check if the tour is already playing"""
        if self.tournament_manager.tournament.progression == Progress.FIRST_ROUND:
            return False
        else:
            return True

    def display_add_player_to_tournament_menu(self):
        """Option to add a player to a tournament"""
        self.prepare_display()
        if not self.check_if_selected_tour():
            self.view.display_no_tournament_selected()
            self.view.press_enter_to_continue()
        elif self.check_if_tour_playing():
            self.view.tournament_playing_error()
            self.view.press_enter_to_continue()
        else:
            self.menu_manager.transition_to(
                AddPlayerToTournament(
                    self.view, self.tournament_manager, self.player_manager
                )
            )

    def prepare_display(self):
        """Clean the display"""
        self.view.clean_console()
        self.view.show_banner()


class PlayerMenu(State):
    """Menu for the player"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
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
        self.prepare_display()
        self.view.display_add_player_to_tournament(
            self.tournament_manager.get_tournament_name()
        )

    def get_user_option(self) -> None:
        """Get the user options"""
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.create_player()
        elif user_option == "2":
            self.add_player_to_tournament()
        elif user_option == "3":
            self.display_tournament_players()
        elif user_option == "4":
            self.remove_player_from_tournament()
        elif user_option == "5":
            self.go_back()

    def create_player(self):
        """Create a player"""
        self.prepare_display()
        self.tournament_manager.add_player_to_tournament()

    def add_player_to_tournament(self):
        """Add a player to the tournament"""
        self.prepare_display()
        self.tournament_manager.add_existing_player_to_tournament()

    def display_tournament_players(self):
        """Display the player playing in the tournament"""
        self.prepare_display()
        self.tournament_manager.display_tournament_players()

    def remove_player_from_tournament(self):
        """Remove a player from the tournament"""
        self.prepare_display()
        self.tournament_manager.remove_player_from_tournament()

    def prepare_display(self):
        """Prepare the display"""
        self.view.clean_console()
        self.view.show_banner()

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            TournamentMenu(self.view, self.tournament_manager, self.player_manager)
        )


class ReportMenu(State):
    """Menu for the player"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        """Display the player menu by calling the view"""
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_report_menu()

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.view.clean_console()
            self.view.show_banner()
            self.menu_manager.transition_to(
                ReportPlayers(self.view, self.tournament_manager, self.player_manager)
            )
        elif user_option == "2":
            self.view.clean_console()
            self.view.show_banner()
            self.menu_manager.transition_to(
                ReportTournamentPlayer(
                    self.view, self.tournament_manager, self.player_manager
                )
            )
        elif user_option == "3":
            self.view.clean_console()
            self.view.show_banner()
            self.menu_manager.transition_to(
                ReportTournaments(
                    self.view, self.tournament_manager, self.player_manager
                )
            )
        elif user_option == "4":
            self.view.clean_console()
            self.view.show_banner()
            self.menu_manager.transition_to(
                ReportTournamentsRounds(
                    self.view, self.tournament_manager, self.player_manager
                )
            )
        elif user_option == "5":
            self.view.clean_console()
            self.view.show_banner()
            self.menu_manager.transition_to(
                ReportTournamentGames(
                    self.view, self.tournament_manager, self.player_manager
                )
            )
        elif user_option == "6":
            self.go_back()

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            MainMenu(self.view, self.tournament_manager, self.player_manager)
        )


class ReportPlayers(State):
    """Report to display all players"""

    def __init__(
        self, view, tournament_manager, player_manager, list_of_player=None
    ) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        """Display the player menu by calling the view"""
        self.view.clean_console()
        self.view.show_banner()
        self.view.display_all_player_report_options()

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.generate_report("alpha")
        elif user_option == "2":
            self.generate_report("elo")
        else:
            self.go_back()

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            ReportMenu(self.view, self.tournament_manager, self.player_manager)
        )

    def generate_report(self, method="alpha", list_of_player=None):

        if not list_of_player:
            player_list = self.player_manager.list_of_player
        else:
            player_list = list_of_player
        if method == "alpha":
            player_list.sort(key=lambda x: x.last_name)
        elif method == "elo":
            player_list.sort(key=lambda x: x.elo)
        self.view.display_list_of_player(player_list)
        self.view.press_enter_to_continue()


class ReportTournamentPlayer(State):
    """Report to display all the player of a tournament"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        """Display the player menu by calling the view"""
        self.output = self.ask_tournament()

    def get_user_option(self) -> None:
        if not self.output:
            self.go_back()
            return
        user_option = self.view.get_user_option()
        if user_option == "1":
            self.generate_report("alpha")
            self.menu_manager.transition_to(
                ReportMenu(self.view, self.tournament_manager, self.player_manager)
            )
        elif user_option == "2":
            self.generate_report("elo")
            self.menu_manager.transition_to(
                ReportMenu(self.view, self.tournament_manager, self.player_manager)
            )
        else:
            self.go_back()

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            ReportMenu(self.view, self.tournament_manager, self.player_manager)
        )

    def ask_tournament(self):
        # Ask for which tournament the report is needed
        tournament_asked = None
        tournament_list = self.tournament_manager.tournament_list
        found = 0
        while not found:
            self.view.clean_console()
            self.view.show_banner()
            self.view.display_list_of_tournament(tournament_list)
            if tournament_list:

                tournament_to_select = self.view.get_tournament_to_select().strip()
                for tournament in tournament_list:
                    if tournament.name.lower() == tournament_to_select.lower():
                        tournament_asked = tournament
                        self.view.display_selected_tournament(tournament_to_select)
                        found = 1
                        break
                if not found:
                    self.view.tournament_selected_not_found(tournament_to_select)
                    self.view.press_enter_to_continue()
            else:
                found = 1
                self.view.press_enter_to_continue()
                return False

            if isinstance(tournament_asked, Tournament):
                self.player_in_asked_tournament = tournament_asked.list_of_players
                self.view.display_all_player_report_options()
                return True

    def generate_report(self, method="alpha"):
        player_list = self.player_in_asked_tournament
        if method == "alpha":
            player_list.sort(key=lambda x: x.last_name)
        elif method == "elo":
            player_list.sort(key=lambda x: x.elo)
        self.view.display_list_of_player(player_list)
        self.view.press_enter_to_continue()


class ReportTournaments(State):
    """Report to display all tournament"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def print_menu(self) -> None:
        """Display the player menu by calling the view"""
        self.tournament_manager.display_all_tournament()

    def get_user_option(self) -> None:
        self.menu_manager.transition_to(
            ReportMenu(self.view, self.tournament_manager, self.player_manager)
        )

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            ReportMenu(self.view, self.tournament_manager, self.player_manager)
        )


class ReportTournamentsRounds(State):
    """Report to display all tournament round"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager
        self.tournament_manager_view = TournamentManagerView()

    def print_menu(self) -> None:
        """Display the player menu by calling the view"""
        self.ask_tournament()

    def get_user_option(self) -> None:
        self.menu_manager.transition_to(
            ReportMenu(self.view, self.tournament_manager, self.player_manager)
        )

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            ReportMenu(self.view, self.tournament_manager, self.player_manager)
        )

    def ask_tournament(self):
        # Ask for which tournament the report is needed
        tournament_asked = None
        self.round_in_asked_tournament = None
        tournament_list = self.tournament_manager.tournament_list
        self.tournament_manager_view.display_list_of_tournament(tournament_list)
        if tournament_list:

            tournament_to_select = (
                self.tournament_manager_view.get_tournament_to_select().strip()
            )
            found = 0
            for tournament in tournament_list:
                if tournament.name.lower() == tournament_to_select.lower():
                    tournament_asked = tournament
                    self.tournament_manager_view.display_selected_tournament(
                        tournament_to_select
                    )
                    found = 1
                    break
            if not found:
                self.tournament_manager_view.tournament_selected_not_found(
                    tournament_to_select
                )
                self.tournament_manager_view.press_enter_to_continue()

        if isinstance(tournament_asked, Tournament):
            self.round_in_asked_tournament = tournament_asked.list_of_rounds
            if self.round_in_asked_tournament:
                self.tournament_manager_view.display_rounds(
                    self.round_in_asked_tournament
                )
                self.tournament_manager_view.press_enter_to_continue()
            else:
                self.tournament_manager_view.no_round()
                self.tournament_manager_view.press_enter_to_continue()


class ReportTournamentGames(State):
    """Report to display all games of a tournaments"""

    def __init__(self, view, tournament_manager, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager
        self.tournament_manager_view = TournamentManagerView()

    def print_menu(self) -> None:
        """Display the player menu by calling the view"""
        self.ask_tournament()

    def get_user_option(self) -> None:
        self.menu_manager.transition_to(
            ReportMenu(self.view, self.tournament_manager, self.player_manager)
        )

    def go_back(self) -> None:
        """Go back to previous menu"""
        self.menu_manager.transition_to(
            ReportMenu(self.view, self.tournament_manager, self.player_manager)
        )

    def ask_tournament(self):
        # Ask for which tournament the report is needed
        tournament_asked = None
        match_in_asked_tournament = []
        tournament_list = self.tournament_manager.tournament_list
        self.tournament_manager_view.display_list_of_tournament(tournament_list)
        if tournament_list:

            tournament_to_select = (
                self.tournament_manager_view.get_tournament_to_select().strip()
            )
            found = 0
            for tournament in tournament_list:
                if tournament.name.lower() == tournament_to_select.lower():
                    tournament_asked = tournament
                    self.tournament_manager_view.display_selected_tournament(
                        tournament_to_select
                    )
                    found = 1
                    break
            if not found:
                self.tournament_manager_view.tournament_selected_not_found(
                    tournament_to_select
                )
                self.tournament_manager_view.press_enter_to_continue()

        if isinstance(tournament_asked, Tournament):
            for round in tournament_asked.list_of_rounds:
                for match in round.list_of_match:
                    match_in_asked_tournament.append(match)
            if match_in_asked_tournament:
                self.tournament_manager_view.display_matchs(match_in_asked_tournament)
                self.tournament_manager_view.press_enter_to_continue()
            else:
                self.tournament_manager_view.no_matchs()
                self.tournament_manager_view.press_enter_to_continue()
