from chess_tournament.models.models import Player  # type:ignore
from chess_tournament.controller.data_manager import SaveData
from chess_tournament.controller.create_player import CreatePlayer
from chess_tournament.controller.modify_player import ModifyPlayer


class PlayerManager:
    """Class that manage the players"""

    def __init__(self, controller, view) -> None:
        self.view = view
        self.controller = controller
        self.list_of_player = []
        self.save_data = SaveData(player_manager=self)

    def create_player(self):
        """Create a player"""
        player = CreatePlayer().create_player()
        self.list_of_player.append(player)
        self.save_data.insert_player()
        self.view.press_enter_to_continue()
        self.view.clean_console()
        self.view.show_banner()
        return player

    def modify_player(self):
        """Modify a player"""
        modify_player = ModifyPlayer(self.list_of_player, self.controller)
        modify_player.modify_player()
        self.save_data.insert_player()

    def display_all_players(self):
        """Display the list of all players"""
        if not self.list_of_player:
            self.view.display_no_existing_player()
        else:
            self.view.display_list_of_player(self.list_of_player)
        self.view.press_enter_to_continue()
        self.view.clean_console()
        self.view.show_banner()

    def insert_player(self, last_name, first_name, birthday, sex, elo):
        """Insert player (used to restore the database)"""
        self.list_of_player.append(Player(last_name, first_name, birthday, sex, elo))

    def reset_player_list(self):
        self.list_of_player = []
