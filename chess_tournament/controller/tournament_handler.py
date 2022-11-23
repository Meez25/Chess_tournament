from datetime import datetime

from chess_tournament.models.models import Progress, Round, Match


class TournamentHandler:
    """Class that handle the tournament"""

    def __init__(self, tournament, tournament_view, save_data) -> None:
        self.tournament = tournament
        self.tournament_manager_view = tournament_view
        self.save_data = save_data

    def handle_tournament(self):

        """Start the tournament"""
        wants_to_continue = True
        if self.tournament.progression == Progress.FIRST_ROUND:
            self.do_first_round()
            self.save_data.insert_tournament()
            self.tournament_manager_view.display_ranking(self.tournament.sort_player())
            wants_to_continue = self.ask_exit_or_continue()

        for i in range(self.tournament.progression.value, 4):
            if wants_to_continue:
                self.do_a_round(i)
                self.save_data.insert_tournament()
                if self.tournament.progression.value < 4:
                    self.tournament_manager_view.display_ranking(
                        self.tournament.sort_player()
                    )
                    wants_to_continue = self.ask_exit_or_continue()
            else:
                break

            if self.tournament.progression == Progress.TOURNAMENT_OVER:
                # End of tournament
                ranking = self.tournament.sort_player()
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
        """Create the nth round"""
        round = Round(f"Round {nround+1}", datetime.now())
        self.tournament.add_round(round)

        # Sort player by Elo
        sorted_list = self.tournament.sort_player()

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
        """Check if the user wants to continue"""
        start_next_round = self.tournament_manager_view.ask_exit_or_continue()
        if not start_next_round:
            wants_to_continue = True
        else:
            wants_to_continue = False
        return wants_to_continue

    def do_first_round(self):
        """Do the first round"""
        self.tournament.progression = Progress.FIRST_ROUND
        self.create_first_round()

        # Display the matchs to play
        self.show_nth_round(0)

        # Ask for results
        self.get_match_results(0)
        self.tournament.progression = Progress.SECOND_ROUND

    def do_a_round(self, n_round):
        """Do next rounds"""
        self.tournament.progression = Progress(n_round + 1)
        # Create the upcoming matches
        self.create_nth_round(n_round)
        # Display the list of generated matches
        self.show_nth_round(n_round)
        # Ask for the results
        self.get_match_results(n_round)
