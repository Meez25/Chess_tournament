from controller.menu_manager import MenuManager  # type:ignore
from controller.menu_manager import MainMenu  # type:ignore
from controller.tournament_manager import TournamentManager  # type:ignore
from controller.player_manager import PlayerManager  # type:ignore
from view.view import View  # type:ignore


class Controller:
    def __init__(self) -> None:
        self.view = View()
        self.player_manager = PlayerManager(self.view)
        self.tournament_manager = TournamentManager(self.view, self.player_manager)
        self.menu_manager = MenuManager(
            MainMenu(self.view, self.tournament_manager, self.player_manager)
        )

    def get_menu_running(self):
        while True:
            self.menu_manager.print_menu()
            self.menu_manager.get_user_option()

    def run(self):
        self.get_menu_running()
