from controller.menu_manager import MenuManager, Main_menu
from controller.tournament_manager import TournamentManager
from controller.player_manager import PlayerManager


class Controller:
    def __init__(self, tournament, view, player_database) -> None:
        self.tournament = tournament
        self.view = view
        self.menu_manager = MenuManager(Main_menu(view))
        self.tournament_manager = TournamentManager(tournament, view)
        self.player_manager = PlayerManager(player_database, view)

    def get_menu_running(self):
        while True:
            self.menu_manager.print_menu()
            user_action = self.menu_manager.get_user_option()
            if user_action == "Create tournament":
                self.tournament_manager.handle_tournament()
            elif user_action == "Add a player":
                self.player_manager.create_player()
            elif user_action == "See list of players":
                self.player_manager.display_all_players()

    def run(self):

        self.get_menu_running()
