from chess_tournament.controller.menu_manager import MenuManager  # type:ignore
from chess_tournament.controller.tournament_manager import (
    TournamentManager,
)  # type:ignore
from chess_tournament.controller.player_manager import PlayerManager  # type:ignore
from chess_tournament.models.models import Player, Tournament


class Controller:
    def __init__(self, view) -> None:
        self.view = view
        self.player_manager = PlayerManager(self.view)
        self.tournament_manager = TournamentManager(self.view, self.player_manager)
        self.menu_manager = MenuManager(
            self.view, self.tournament_manager, self.player_manager
        )
        # self.create_test_data()

    def get_menu_running(self):
        while True:
            self.menu_manager.print_menu()
            self.menu_manager.get_user_option()

    def run(self):
        self.get_menu_running()

    def create_test_data(self):
        # Add test data
        test_data = [
            ["last_name_1", "first_name_1", "birthday_1", "sex_1", "100"],
            ["last_name_2", "first_name_2", "birthday_2", "sex_2", "200"],
            ["last_name_3", "first_name_3", "birthday_3", "sex_3", "300"],
            ["last_name_4", "first_name_4", "birthday_4", "sex_4", "400"],
            ["last_name_5", "first_name_5", "birthday_5", "sex_5", "500"],
            ["last_name_6", "first_name_6", "birthday_6", "sex_6", "600"],
            ["last_name_7", "first_name_7", "birthday_7", "sex_7", "700"],
            ["last_name_8", "first_name_8", "birthday_8", "sex_8", "800"],
        ]

        for player in test_data:
            last_name = player[0]
            first_name = player[1]
            birthday = player[2]
            sex = player[3]
            elo = int(player[4])
            player_object: Player = Player(last_name, first_name, birthday, sex, elo)
            self.player_manager.list_of_player.append(player_object)

        # Add test data
        self.tournament = Tournament("Mulhouse", "", "", "", "")
        self.tournament_manager.tournament_list.append(self.tournament)
        for player in self.player_manager.list_of_player:
            self.tournament.add_player_in_list(player)
        self.tournament_manager.tournament = self.tournament
