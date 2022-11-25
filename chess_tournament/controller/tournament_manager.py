from datetime import datetime

from chess_tournament.models.models import (
    Match,
    Round,
    Tournament,
    Progress,
)  # type:ignore
from chess_tournament.view.tournament_manager_view import TournamentManagerView
from chess_tournament.controller.data_manager import SaveData
from chess_tournament.controller.create_tournament import CreateTournament
from chess_tournament.controller.player_insertor import PlayerInsertor
from chess_tournament.controller.tournament_handler import TournamentHandler


class TournamentManager:
    """Class that manager the tournament"""

    def __init__(self, view, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_list = []
        self.tournament = None
        self.tournament_manager_view = TournamentManagerView()
        self.save_data = SaveData(
            tournament_manager=self, player_manager=self.player_manager
        )

    def clear_tournament(self):
        self.tournament_list = []
        self.tournament = None

    def insert_tournament(
        self,
        name,
        location,
        date,
        time_control,
        description,
        list_of_player,
        list_of_round,
        progression,
    ):
        """Insert tournament (used to restore the database)"""
        # Create the tournament, then create the player,
        # put them in the tournament, create the round, etc
        tournament_to_add = Tournament(
            name,
            location,
            date,
            time_control,
            description,
        )
        for round in list_of_round:
            end_date_as_string = round["end_date"]
            end_date = datetime.strptime(end_date_as_string, "%d/%m/%y %H:%M")
            start_date_as_string = round["start_date"]
            start_date = datetime.strptime(start_date_as_string, "%d/%m/%y %H:%M")
            round_to_add = Round(round["name"], start_date)
            round_to_add.end_date = end_date
            for match in round["list_of_match"]:

                player1 = match["player1"]
                last_name = player1["last_name"]
                first_name = player1["first_name"]

                for player in self.player_manager.list_of_player:
                    if (
                        last_name == player.last_name
                        and first_name == player.first_name
                    ):
                        player1_to_add = player

                player1_score = match["result"]["0"]["1"]

                player2 = match["player2"]
                last_name = player2["last_name"]
                first_name = player2["first_name"]

                for player in self.player_manager.list_of_player:
                    if (
                        last_name == player.last_name
                        and first_name == player.first_name
                    ):
                        player2_to_add = player

                player2_score = match["result"]["1"]["1"]

                match_to_add = Match(player1_to_add, player2_to_add)
                match_to_add.set_result(player1_to_add, player1_score)
                match_to_add.set_result(player2_to_add, player2_score)

                round_to_add.add_game(match_to_add)

            tournament_to_add.add_round(round_to_add)

        tournament_to_add.progression = Progress(progression)

        self.tournament_list.append(tournament_to_add)
        self.tournament = tournament_to_add

        for player in list_of_player:
            for original_player in self.player_manager.list_of_player:
                if (
                    player["first_name"] == original_player.first_name
                    and player["last_name"] == original_player.last_name
                ):
                    tournament_to_add.add_player_in_list(original_player)

    def create_tournament(self):
        tournament = CreateTournament().create_tournament()
        self.tournament_list.append(tournament)
        self.tournament = tournament
        self.tournament_manager_view.tournament_added_successfully()
        self.save_data.insert_tournament()
        self.tournament_manager_view.press_enter_to_continue()

    def add_existing_player_to_tournament(self):
        """Add an existing player to the tournament"""
        if not self.player_manager.list_of_player:
            self.tournament_manager_view.display_no_existing_player()
            self.tournament_manager_view.press_enter_to_continue()
        else:
            player_insertor = PlayerInsertor(
                self.tournament_manager_view,
                self.player_manager,
                tournament=self.tournament,
            )
            output = player_insertor.add_existing_player_to_tournament()
            if not output:
                return
            else:
                self.save_data.insert_tournament()
                self.save_data.insert_player()

    def add_player_to_tournament(self):
        """Add a player to the current tournament"""
        player_insertor = PlayerInsertor(
            self.tournament_manager_view,
            self.player_manager,
            tournament=self.tournament,
        )
        player_insertor.add_player_to_tournament()
        self.save_data.insert_tournament()
        self.save_data.insert_player()

    def get_tournament_name(self):
        """Get the current tournament"""
        if not self.tournament:
            return ""
        else:
            return self.tournament.name

    def change_selected_tournament(self):
        """Change the tournament currently selected"""
        self.tournament_manager_view.display_list_of_tournament(self.tournament_list)
        if self.tournament_list:

            tournament_to_select = (
                self.tournament_manager_view.get_tournament_to_select().strip()
            )
            found = 0
            for tournament in self.tournament_list:
                if tournament.name.lower() == tournament_to_select.lower():
                    self.tournament = tournament
                    self.tournament_manager_view.display_selected_tournament(
                        tournament_to_select
                    )
                    self.tournament_manager_view.press_enter_to_continue()
                    found = 1
                    break
            if not found:
                self.tournament_manager_view.tournament_selected_not_found(
                    tournament_to_select
                )
                self.tournament_manager_view.press_enter_to_continue()

    def display_all_tournament(self):
        """Display the list of all tournament"""
        self.tournament_manager_view.display_list_of_tournament(self.tournament_list)
        self.tournament_manager_view.press_enter_to_continue()

    def get_player(self, mode=None):
        """Ask which player"""

        if mode == "delete":
            player_index = self.tournament_manager_view.which_player_to_delete(
                self.tournament.list_of_players
            )
        else:
            player_index = self.tournament_manager_view.display_existing_player_to_add(
                self.tournament.list_of_players
            )

        self.tournament_manager_view.clean_console()
        self.tournament_manager_view.show_banner()
        if not player_index:
            return
        if not player_index.isdigit():
            return
        if not int(player_index) > -1 and int(player_index) < len(
            self.tournament.list_of_player
        ):
            return
        try:
            player_object_to_modify = self.tournament.list_of_players[int(player_index)]
        except Exception:
            print(Exception)
        return player_object_to_modify

    def delete_tournament(self):
        """Ask the user which tournament to delete"""
        self.tournament_manager_view.display_list_of_tournament(self.tournament_list)
        if self.tournament_list:
            tournament_to_delete = (
                self.tournament_manager_view.get_tournament_to_delete().strip()
            )
            found = 0
            for tournament in self.tournament_list:
                if tournament.name.lower() == tournament_to_delete.lower():
                    self.tournament_list.remove(tournament)
                    self.save_data.insert_tournament()
                    self.tournament_manager_view.display_deleted_tournament(
                        tournament_to_delete
                    )
                    if self.tournament == tournament:
                        self.tournament = ""
                    self.tournament_manager_view.press_enter_to_continue()
                    found = 1
                    break
                elif tournament_to_delete == "":
                    found = 1
                    break
            if not found:
                self.tournament_manager_view.tournament_selected_not_found(
                    tournament_to_delete
                )
                self.tournament_manager_view.press_enter_to_continue()

    def display_tournament_players(self):
        """Display the list of player in the tournament"""
        if not self.tournament.list_of_players:
            self.tournament_manager_view.display_no_player_in_tournament()
        else:
            self.tournament_manager_view.display_list_of_player(
                self.tournament.list_of_players
            )
        self.tournament_manager_view.press_enter_to_continue()

    def remove_player_from_tournament(self):
        """Remove a player from the tournament"""

        if self.tournament.is_empty():
            # Check if there is at least a player to delete
            self.tournament_manager_view.display_no_player_in_tournament()
            self.tournament_manager_view.press_enter_to_continue()

        else:

            player_to_delete = self.get_player(mode="delete")

            found = False
            if player_to_delete in self.tournament.list_of_players:
                found = True
                self.tournament.remove_player_in_list(player_to_delete)
                self.tournament_manager_view.player_removed_from_tournament()
                self.save_data.insert_tournament()
                self.tournament_manager_view.press_enter_to_continue()
            if not found:
                self.tournament_manager_view.player_not_found(player_to_delete)
                self.tournament_manager_view.press_enter_to_continue()

    def check_if_tournament_selected(self):
        """Check if a tournament is selected"""
        if not self.tournament:
            self.tournament_manager_view.display_no_tournament_selected()
            self.tournament_manager_view.press_enter_to_continue()
            return False
        else:
            return True

    def handle_tournament(self):
        """Function that handle the tournament (round, etc)"""
        if not self.check_if_tournament_selected():
            return
        if not self.tournament.is_full():
            self.tournament_manager_view.display_need_x_number_of_player(
                self.tournament.NUMBER_OF_PLAYER
            )
            self.tournament_manager_view.press_enter_to_continue()
            return
        if self.tournament.progression == Progress.TOURNAMENT_OVER:
            self.tournament_manager_view.tournament_is_over()

            ranking = self.tournament.sort_player()
            self.tournament_manager_view.display_ranking_end_of_tournament(ranking)
            self.tournament_manager_view.press_enter_to_continue()
            return

        tournament_handler = TournamentHandler(
            self.tournament, self.tournament_manager_view, self.save_data
        )
        tournament_handler.handle_tournament()
