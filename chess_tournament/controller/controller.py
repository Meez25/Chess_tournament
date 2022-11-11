from controller.menu_manager import MenuManager, Main_menu
from controller.tournament_manager import TournamentManager


class Controller:
    def __init__(self, tournament, view) -> None:
        self.tournament = tournament
        self.view = view
        self.menu_manager = MenuManager(Main_menu(view))
        self.tournament_manager = TournamentManager(tournament, view)

    

    def get_menu_running(self):
        while(True):
            self.menu_manager.print_menu()
            user_action = self.menu_manager.get_user_option()
            if user_action == "Create tournament":
                self.tournament_manager.handle_tournament()

    def run(self):

        self.get_menu_running()

        
        
