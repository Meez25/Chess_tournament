from models.models import Player, Match, Round, Tournament, Progress
from datetime import datetime


class TournamentManager:
    def __init__(self, view, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_list = []
        # self.tournament = ""

        # Add test data
        self.tournament = Tournament("Mulhouse", "", "", "", "")
        self.tournament_list.append(self.tournament)
        for player in self.player_manager.get_all_players():
            self.tournament.add_player_in_list(player)

    def create_tournament(self):
        """Create a tournament by calling the view and adding
        it to the list of tournament"""
        tournament_name = self.get_tournament_name()
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
        self.tournament_list.append(self.tournament)
        self.view.tournament_added_successfully()
        self.view.press_enter_to_continue()

    def get_tournament(self):
        """Get the current tournament"""
        if not self.tournament:
            return ""
        else:
            return self.tournament.get_tournament_name()

    def add_player_to_tournament(self, player):
        """Add a player to the current tournament"""
        if (
            len(self.tournament.list_of_players)
            < self.tournament.get_number_of_player()
        ):
            self.tournament.add_player_in_list(player)
        else:
            self.view.enough_number_of_player(self.tournament.get_number_of_player())
            self.view.press_enter_to_continue()

    def get_tournament_name(self):
        """Get the current tournament's name"""
        tournament_name = self.view.get_tournament_name()
        return tournament_name

    def get_tournament_location(self):
        """Get the current tournament location"""
        tournament_location = self.view.get_tournament_location()
        return tournament_location

    def get_tournament_date(self):
        """Get the current tournament date"""
        tournament_date = self.view.get_tournament_date()
        return tournament_date

    def get_time_control(self):
        """Get the current tournament time control"""
        time_control = self.view.get_time_control()
        return time_control

    def get_tournament_description(self):
        """Get the current tournament description"""
        tournament_description = self.view.get_tournament_description()
        return tournament_description

    def add_existing_player_to_tournament(self):
        """Add an existing player to the current tournament"""
        # If there is no player in the "database, send error message"
        if not self.player_manager.get_all_players():

            self.view.display_no_existing_player()
            self.view.press_enter_to_continue()
        else:
            # Display the list of all players so the user can select
            list_of_all_players = self.player_manager.get_all_players()
            self.view.display_existing_player_to_add(list_of_all_players)

            list_of_tournament_player = self.tournament.get_list_of_player()

            # Get the choice of the user
            player_index = self.view.get_index_of_player()
            for player in list_of_all_players:
                if player.get_id() == int(player_index):
                    # If the player is not already in the tournament
                    # Add the player to tournament
                    if player not in list_of_tournament_player:
                        self.tournament.add_player_in_list(player)
                        self.view.player_added_to_tournament(player)
                        self.view.press_enter_to_continue()
                    else:
                        self.view.player_already_in_tournament()
                        self.view.press_enter_to_continue()

    def change_selected_tournament(self):
        """Change the tournament currently selected"""
        self.view.display_list_of_tournament(self.tournament_list)
        if self.tournament_list:

            tournament_to_select = self.view.get_tournament_to_select().strip()
            found = 0
            for tournament in self.tournament_list:
                if tournament.name.lower() == tournament_to_select.lower():
                    self.tournament = tournament
                    self.view.display_selected_tournament(tournament_to_select)
                    self.view.press_enter_to_continue()
                    found = 1
                    break
            if not found:
                self.view.tournament_selected_not_found(tournament_to_select)
                self.view.press_enter_to_continue()

    def display_all_tournament(self):
        """Display the list of all tournament"""
        self.view.display_list_of_tournament(self.tournament_list)
        self.view.press_enter_to_continue()

    def delete_tournament(self):
        """Ask the user which tournament to delete"""
        self.view.display_list_of_tournament(self.tournament_list)
        if self.tournament_list:
            tournament_to_delete = self.view.get_tournament_to_delete().strip()
            found = 0
            for tournament in self.tournament_list:
                if tournament.name.lower() == tournament_to_delete.lower():
                    self.tournament_list.remove(tournament)
                    self.view.display_deleted_tournament(tournament_to_delete)
                    if self.tournament == tournament:
                        self.tournament = ""
                    self.view.press_enter_to_continue()
                    found = 1
                    break
                elif tournament_to_delete == "":
                    found = 1
                    break
            if not found:
                self.view.tournament_selected_not_found(tournament_to_delete)
                self.view.press_enter_to_continue()

    def display_tournament_players(self):
        """Display the list of player in the tournament"""
        if not self.tournament.get_list_of_player():
            self.view.display_no_player_in_tournament()
        else:
            self.view.display_list_of_player(self.tournament.get_list_of_player())
        self.view.press_enter_to_continue()

    def remove_player_from_tournament(self):
        """Remove a player from the tournament"""

        if not self.tournament.get_list_of_player():
            self.view.display_no_player_in_tournament()
            self.view.press_enter_to_continue()
        else:
            self.view.which_player_to_delete(self.tournament.get_list_of_player())
            player_to_delete = self.view.get_player_to_delete_from_tournament().strip()
            for player in self.tournament.get_list_of_player():
                if int(player_to_delete) == player.get_id():
                    self.tournament.remove_player_in_list(player)
                    self.view.player_removed_from_tournament(int(player_to_delete))
                    self.view.press_enter_to_continue()
                else:
                    self.view.player_not_found(player_to_delete)
                    self.view.press_enter_to_continue()

    def ask_exit_or_continue(self):
        start_next_round = self.view.ask_exit_or_continue()
        if not start_next_round:
            wants_to_continue = True
        else:
            wants_to_continue = False
        return wants_to_continue

    def do_first_round(self):
        self.tournament.set_progression(Progress.FIRST_ROUND)
        self.create_first_round()

        # Display the matchs to play
        self.show_nth_round(0)

        # Ask for results
        self.get_match_results(0)

    def do_a_round(self, n_round):

        self.tournament.set_progression(Progress(n_round))
        # Create the upcoming matches
        self.create_nth_round(n_round)
        # Display the list of generated matches
        self.show_nth_round(n_round)
        # Ask for the results
        self.get_match_results(n_round)

    def handle_tournament(self):

        """Start the tournament"""
        if not self.tournament:
            self.view.display_no_tournament_selected()
            self.view.press_enter_to_continue()
        else:
            if (
                not len(self.tournament.list_of_players)
                == self.tournament.get_number_of_player()
            ):
                self.view.display_need_x_number_of_player(
                    self.tournament.get_number_of_player()
                )
                self.view.press_enter_to_continue()
            else:

                self.do_first_round()

                for i in range(1, 4):
                    wants_to_continue = self.ask_exit_or_continue()
                    if wants_to_continue:
                        self.do_a_round(i)
                    else:
                        break
                    #
                    if self.tournament.get_progression() == Progress.FOURTH_ROUND:
                        # End of tournament
                        ranking = self.sort_player()
                        for player in ranking:
                            print(player[0])

                        self.view.press_enter_to_continue()

    def get_player_last_name(self):
        """Get the player last name"""
        valid_input = 0
        while not valid_input:
            last_name = self.view.ask_player_last_name()
            if last_name:
                valid_input = 1
                return last_name
            else:
                self.view.display_empty_last_name_error()

    def get_player_first_name(self):
        """Get the player first name"""
        valid_input = 0
        while not valid_input:
            first_name = self.view.ask_player_first_name()
            if first_name:
                valid_input = 1
                return first_name
            else:
                self.view.display_empty_first_name_error()

    def get_player_birthday(self):
        """Get the player birthday"""
        valid_input = 0
        while not valid_input:
            birthday = self.view.ask_player_birthday()
            if birthday:
                valid_input = 1
                return birthday
            else:
                self.view.display_empty_birthday_error()

    def get_player_sex(self):
        """Get the player sex"""
        valid_input = 0
        while not valid_input:
            sex = self.view.ask_player_sex()
            if sex:
                valid_input = 1
                return sex
            else:
                self.view.display_empty_sex_error()

    def get_player_elo(self):
        """Get the player elo"""
        valid_input = 0
        while not valid_input:
            elo = self.view.ask_player_elo()
            if elo and elo.isdigit():
                valid_input = 1
                return elo
            elif not elo:
                self.view.display_empty_elo_error()
            elif not elo.isdigit():
                self.view.display_elo_not_number_error()
            else:
                print("Erreur dans get_player_elo")

    def create_first_round(self):
        """Create the first round"""
        # Create first round
        first_round = Round("Round 1", datetime.now())
        self.tournament.add_round(first_round)

        # Sort player by Elo
        self.tournament.get_list_of_player().sort(key=lambda x: x.elo)

        # Split the list in 2 groups
        middle_index = int(len(self.tournament.get_list_of_player()) / 2)
        high_elo = self.tournament.get_list_of_player()[:middle_index]
        low_elo = self.tournament.get_list_of_player()[middle_index:]

        # Create 4 matches for the first round
        for i in range(int(self.tournament.get_number_of_player() / 2)):
            first_round.add_game(Match(high_elo[i], low_elo[i]))

    def show_nth_round(self, n):
        """Show the nth round"""
        self.view.clean_console()
        self.view.show_banner()
        self.view.announce_matches()
        n_round = self.tournament.get_list_of_rounds()[n]
        game_list = n_round.get_list_of_match()
        for game in game_list:
            player1, player2 = game.show_players()
            self.view.display_nth_round_games(player1, player2)

    def get_match_results(self, n):
        """Ask 8 times for the results of matches"""
        for i in range(int(self.tournament.get_number_of_player() / 2)):
            self.enter_match_results(n, i)

    def enter_match_results(self, nth_round, nth_match):
        """Get the result for the nth match of the nth round"""

        n_round = self.tournament.get_list_of_rounds()[nth_round]
        # Match is considered over so we get the time
        n_round.set_end_date(datetime.now())
        game = n_round.get_list_of_match()[nth_match]
        players = game.get_players()
        # Add the already played player to the player

        for i, player in enumerate(players):
            if i == 0:
                valid_input = 0
                while not valid_input:
                    score = self.view.ask_results(player)
                    if score == "0" or score == "0,5" or score == "0.5" or score == "1":
                        if "," in score:
                            score = score.replace(",", ".")
                        valid_input = 1
                        self.tournament.get_list_of_rounds()[
                            nth_round
                        ].get_list_of_match()[nth_match].set_result(
                            player, float(score)
                        )

                    else:
                        self.view.display_score_error()
            elif i == 1:
                valid_input = 0
                while not valid_input:
                    score = self.view.ask_results(player)
                    if score == "0" or score == "0,5" or score == "0.5" or score == "1":
                        if "," in score:
                            score = score.replace(",", ".")
                        valid_input = 1
                        self.tournament.get_list_of_rounds()[
                            nth_round
                        ].get_list_of_match()[nth_match].set_result(
                            player, float(score)
                        )

                    else:
                        self.view.display_score_error()

    def sort_player(self):
        """Get the result of the previous rounds per player and make a sorted list"""
        previous_round = []
        for player in self.tournament.get_list_of_player():
            player_point = 0
            for round in self.tournament.get_list_of_rounds():
                for match in round.get_list_of_match():
                    match_result = match.get_result()
                    if player == match_result[0][0]:
                        player_point = player_point + match_result[0][1]
                    elif player == match_result[1][0]:
                        player_point = player_point + match_result[1][1]
            previous_round.append([player, player_point])
        previous_round.sort(key=lambda x: (x[1], x[0].get_elo()), reverse=True)
        return previous_round

    def get_list_already_played(self, player):
        """Returns a list of player and their already played opponents"""
        played_played = []
        # Loop through last round except current one to see already played players
        for round in self.tournament.get_list_of_rounds()[:-1]:
            for match in round.get_list_of_match():
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
        for i in range(int(self.tournament.get_number_of_player() / 2)):
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
