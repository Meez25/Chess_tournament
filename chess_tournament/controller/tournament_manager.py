from datetime import datetime

from chess_tournament.models.models import (
    Match,
    Round,
    Tournament,
    Progress,
    Player,
)  # type:ignore
from chess_tournament.controller.player_manager import CreatePlayer
from chess_tournament.view.tournament_manager_view import TournamentManagerView
from chess_tournament.view.create_tournament_view import CreateTournamentView


class CreateTournament:
    def __init__(self) -> None:
        self.modify_player_view = CreateTournamentView()

    def create_tournament(self):
        """Create a tournament by calling the view and adding
        it to the list of tournament"""
        tournament_name = self.get_tournament_name_from_view()
        tournament_location = self.get_tournament_location()
        tournament_date = self.get_tournament_date()
        time_control = self.get_time_control()
        tournament_description = self.get_tournament_description()
        self.tournament = Tournament(
            tournament_name,
            tournament_location,
            tournament_date,
            time_control,
            tournament_description,
        )
        return self.tournament

    def get_tournament_name_from_view(self):
        """Get the current tournament's name"""
        while True:
            tournament_name = self.modify_player_view.get_tournament_name()
            if not tournament_name:
                self.modify_player_view.name_cannot_be_empty()
                continue
            else:
                break
        return tournament_name

    def get_tournament_location(self):
        """Get the current tournament location"""
        tournament_location = self.modify_player_view.get_tournament_location()
        return tournament_location

    def get_tournament_date(self):
        """Get the current tournament date"""
        tournament_date = self.modify_player_view.get_tournament_date()
        return tournament_date

    def get_time_control(self):
        """Get the current tournament time control"""
        time_control = self.modify_player_view.get_time_control()
        return time_control

    def get_tournament_description(self):
        """Get the current tournament description"""
        tournament_description = self.modify_player_view.get_tournament_description()
        return tournament_description


class PlayerInsertor:
    def __init__(self, view, list_of_all_player, tournament=None) -> None:
        self.tournament = tournament
        self.view = view
        self.all_players = list_of_all_player

    def add_player_to_tournament(self):
        """Add a player to the current tournament"""
        if not self.tournament.is_full():
            self.tournament.add_player_in_list(CreatePlayer().create_player())
        else:
            self.view.enough_number_of_player(self.tournament.NUMBER_OF_PLAYER)
            self.view.press_enter_to_continue()

    def add_existing_player_to_tournament(self):
        """Add an existing player to the current tournament"""
        # If there is no player in the "database", send error message

        if self.tournament.is_full():
            self.view.enough_number_of_player(self.tournament.NUMBER_OF_PLAYER)
            self.view.press_enter_to_continue()
        else:
            # Display the list of all players so the user can select
            self.view.display_existing_player_to_add(self.all_players)

            # Get the tournament import to avoid duplicates
            list_of_tournament_player = self.tournament.list_of_players

            # Get the choice of the user
            player_index = self.view.get_index_of_player()
            for player in self.all_players:
                if player.id == int(player_index):
                    # If the player is not already in the tournament
                    # Add the player to tournament
                    if player not in list_of_tournament_player:
                        self.tournament.add_player_in_list(player)
                        self.view.player_added_to_tournament(player)
                        self.view.press_enter_to_continue()
                    else:
                        self.view.player_already_in_tournament()
                        self.view.press_enter_to_continue()


class TournamentManager:
    def __init__(self, view, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_list = []
        self.tournament = None
        self.tournament_manager_view = TournamentManagerView()

    def clear_tournament(self):
        self.tournament_list = []

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
            end_date = round["end_date"]
            round_to_add = Round(round["name"], round["start_date"])
            round_to_add.end_date = end_date
            for match in round["list_of_match"]:

                player1 = match["player1"]
                last_name = (player1["last_name"],)
                first_name = (player1["first_name"],)
                birthday = (player1["date_of_birth"],)
                sex = (player1["sex"],)
                elo = (player1["elo"],)
                id = player1["id"]
                player1_to_add = Player(last_name, first_name, birthday, sex, elo, id)

                player1_score = match["result"]["0"]["1"]

                player2 = match["player2"]
                last_name = (player2["last_name"],)
                first_name = (player2["first_name"],)
                birthday = (player2["date_of_birth"],)
                sex = (player2["sex"],)
                elo = (player2["elo"],)
                id = player2["id"]
                player2_to_add = Player(last_name, first_name, birthday, sex, elo, id)

                player2_score = match["result"]["1"]["1"]

                match_to_add = Match(player1_to_add, player2_to_add)
                match_to_add.set_result(player1_to_add, player1_score)
                match_to_add.set_result(player2_to_add, player2_score)

                round_to_add.add_game(match_to_add)

            tournament_to_add.add_round(round_to_add)
            tournament_to_add.progression = Progress(progression)

        self.tournament_list.append(tournament_to_add)

        for player in list_of_player:
            player_to_add = Player(
                player["last_name"],
                player["first_name"],
                player["date_of_birth"],
                player["sex"],
                player["elo"],
                player["id"],
            )
            tournament_to_add.add_player_in_list(player_to_add)

    def create_tournament(self):
        tournament = CreateTournament().create_tournament()
        self.tournament_list.append(tournament)
        self.tournament = tournament
        self.tournament_manager_view.tournament_added_successfully()
        self.tournament_manager_view.press_enter_to_continue()

    def add_existing_player_to_tournament(self):
        if not self.player_manager.list_of_player:
            self.tournament_manager_view.display_no_existing_player()
            self.tournament_manager_view.press_enter_to_continue()
        else:
            player_insertor = PlayerInsertor(
                self.tournament_manager_view,
                self.player_manager.list_of_player,
                self.tournament,
            )
            player_insertor.add_existing_player_to_tournament()

    def add_player_to_tournament(self):
        """Add a player to the current tournament"""
        player_insertor = PlayerInsertor(
            self.tournament_manager_view,
            self.player_manager.list_of_player,
            self.tournament,
        )
        player_insertor.add_player_to_tournament()

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
            self.tournament_manager_view.which_player_to_delete(
                self.tournament.list_of_players
            )
            player_to_delete = (
                self.tournament_manager_view.get_player_to_delete_from_tournament().strip()
            )
            for player in self.tournament.list_of_players:
                if int(player_to_delete) == player.id:
                    self.tournament.remove_player_in_list(player)
                    self.tournament_manager_view.player_removed_from_tournament(
                        int(player_to_delete)
                    )
                    self.tournament_manager_view.press_enter_to_continue()
                else:
                    self.tournament_manager_view.player_not_found(player_to_delete)
                    self.tournament_manager_view.press_enter_to_continue()

    def check_if_tournament_selected(self):
        if not self.tournament:
            self.tournament_manager_view.display_no_tournament_selected()
            self.tournament_manager_view.press_enter_to_continue()
            return False
        else:
            return True

    def handle_tournament(self):
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
            self.tournament_manager_view.press_enter_to_continue()
            return

        tournament_handler = TournamentHandler(
            self.tournament, self.tournament_manager_view
        )
        tournament_handler.handle_tournament()


class TournamentHandler:
    def __init__(self, tournament, tournament_view) -> None:
        self.tournament = tournament
        self.tournament_manager_view = tournament_view

    def handle_tournament(self):

        """Start the tournament"""
        wants_to_continue = True
        if self.tournament.progression == Progress.FIRST_ROUND:
            self.do_first_round()
            wants_to_continue = self.ask_exit_or_continue()

        for i in range(self.tournament.progression.value, 4):
            if wants_to_continue:
                self.do_a_round(i)
                if self.tournament.progression.value < 4:
                    wants_to_continue = self.ask_exit_or_continue()
            else:
                break

            if self.tournament.progression == Progress.TOURNAMENT_OVER:
                # End of tournament
                ranking = self.sort_player()
                self.tournament_manager_view.display_ranking_end_of_tournament(ranking)
                self.tournament_manager_view.press_enter_to_continue()

    def create_first_round(self):
        """Create the first round"""

        first_round = Round("Round 1", datetime.now())
        self.tournament.add_round(first_round)

        # Sort player by Elo
        self.tournament.list_of_players.sort(key=lambda x: x.elo)

        # Split the list in 2 groups
        middle_index = int(len(self.tournament.list_of_players) / 2)
        high_elo = self.tournament.list_of_players[:middle_index]
        low_elo = self.tournament.list_of_players[middle_index:]

        # Create 4 matches for the first round
        for i in range(int(self.tournament.NUMBER_OF_PLAYER / 2)):
            first_round.add_game(Match(high_elo[i], low_elo[i]))

    def show_nth_round(self, n):
        """Show the nth round"""
        self.tournament_manager_view.clean_console()
        self.tournament_manager_view.show_banner()
        self.tournament_manager_view.announce_matches()
        n_round = self.tournament.list_of_rounds[n]
        game_list = n_round.list_of_match
        for game in game_list:
            player1, player2 = game.get_players()
            self.tournament_manager_view.display_nth_round_games(player1, player2)

    def get_match_results(self, n):
        """Ask 8 times for the results of matches"""
        for i in range(int(self.tournament.NUMBER_OF_PLAYER / 2)):
            self.enter_match_results(n, i)

    def enter_match_results(self, nth_round, nth_match):
        """Get the result for the nth match of the nth round"""

        n_round = self.tournament.list_of_rounds[nth_round]
        # Match is considered over so we get the time
        n_round.end_date = datetime.now()
        game = n_round.list_of_match[nth_match]
        players = game.get_players()
        # Add the already played player to the player

        for i, player in enumerate(players):
            if i == 0:
                valid_input = 0
                while not valid_input:
                    score = self.tournament_manager_view.ask_results(player)
                    if score == "0" or score == "0,5" or score == "0.5" or score == "1":
                        if "," in score:
                            score = score.replace(",", ".")
                        valid_input = 1
                        self.tournament.list_of_rounds[nth_round].list_of_match[
                            nth_match
                        ].set_result(player, float(score))

                    else:
                        self.tournament_manager_view.display_score_error()
            elif i == 1:
                valid_input = 0
                while not valid_input:
                    score = self.tournament_manager_view.ask_results(player)
                    if score == "0" or score == "0,5" or score == "0.5" or score == "1":
                        if "," in score:
                            score = score.replace(",", ".")
                        valid_input = 1
                        self.tournament.list_of_rounds[nth_round].list_of_match[
                            nth_match
                        ].set_result(player, float(score))

                    else:
                        self.tournament_manager_view.display_score_error()

    def sort_player(self):
        """Get the result of the previous rounds per player and make a sorted list"""
        previous_round = []
        for player in self.tournament.list_of_players:
            player_point = 0
            for round in self.tournament.list_of_rounds:
                for match in round.list_of_match:
                    match_result = match.get_result()
                    if player == match_result[0][0]:
                        player_point = player_point + match_result[0][1]
                    elif player == match_result[1][0]:
                        player_point = player_point + match_result[1][1]
            previous_round.append([player, player_point])
        previous_round.sort(key=lambda x: (x[1], x[0].elo), reverse=True)
        return previous_round

    def get_list_already_played(self, player):
        """Returns a list of player and their already played opponents"""
        played_played = []
        # Loop through last round except current one to see already played players
        for round in self.tournament.list_of_rounds[:-1]:
            for match in round.list_of_match:
                match_result = match.get_result()
                if player == match_result[0][0]:
                    played_played.append(match_result[1][0])
                elif player == match_result[1][0]:
                    played_played.append(match_result[0][1])
        return played_played

    def create_nth_round(self, nround):
        # Create first round
        round = Round(f"Round {nround+1}", datetime.now())
        self.tournament.add_round(round)

        # Sort player by Elo
        sorted_list = self.sort_player()

        # Create 4 matches for the nth round
        for _ in range(int(self.tournament.NUMBER_OF_PLAYER / 2)):
            found = False
            j = 1
            if not sorted_list:
                found = True
            while not found:
                player = sorted_list[0][0]
                if sorted_list[j][0] not in self.get_list_already_played(player):
                    found = True
                    round.add_game(Match(player, sorted_list[j][0]))
                    del sorted_list[0]
                    del sorted_list[j - 1]
                else:
                    j = j + 1

    def ask_exit_or_continue(self):
        start_next_round = self.tournament_manager_view.ask_exit_or_continue()
        if not start_next_round:
            wants_to_continue = True
        else:
            wants_to_continue = False
        return wants_to_continue

    def do_first_round(self):
        self.tournament.progression = Progress.FIRST_ROUND
        self.create_first_round()

        # Display the matchs to play
        self.show_nth_round(0)

        # Ask for results
        self.get_match_results(0)
        self.tournament.progression = Progress.SECOND_ROUND

    def do_a_round(self, n_round):
        self.tournament.progression = Progress(n_round + 1)
        # Create the upcoming matches
        self.create_nth_round(n_round)
        # Display the list of generated matches
        self.show_nth_round(n_round)
        # Ask for the results
        self.get_match_results(n_round)
