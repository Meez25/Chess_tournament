from models.models import Player, Match, Round, Tournament
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
        if len(self.tournament.list_of_players) < self.tournament.NUMBER_OF_PLAYER:
            self.tournament.add_player_in_list(player)
        else:
            self.view.enough_number_of_player(self.tournament.NUMBER_OF_PLAYER)
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

    def handle_tournament(self):
        """Start the tournament"""
        if not len(self.tournament.list_of_players) == self.tournament.NUMBER_OF_PLAYER:
            self.view.display_need_x_number_of_player(self.tournament.NUMBER_OF_PLAYER)
            self.view.press_enter_to_continue()
        else:

            self.create_first_round()

            # Introduce the upcoming list of matchs
            self.display_list_match()

            # Display the matchs to play
            self.show_nth_round(0)

            # Ask for results
            self.get_match_results(0)

            self.give_points_to_players_from_match(0)

            self.create_nth_round(1)
            self.display_list_match()
            self.show_nth_round(1)
            self.get_match_results(1)
            self.give_points_to_players_from_match(1)

            self.create_nth_round(2)
            self.display_list_match()
            self.show_nth_round(2)
            self.get_match_results(2)
            self.give_points_to_players_from_match(2)

            self.create_nth_round(3)
            self.display_list_match()
            self.show_nth_round(3)
            self.get_match_results(3)
            self.give_points_to_players_from_match(3)

            self.sort_player()
            for player in self.tournament.get_list_of_player():
                print(player)

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
        high_elo = self.tournament.get_list_of_player()[0:4]
        low_elo = self.tournament.get_list_of_player()[4:8]

        # Create 4 matches for the first round
        for i in range(int(self.tournament.NUMBER_OF_PLAYER / 2)):
            first_round.add_game(Match(high_elo[i], low_elo[i]))

    def show_nth_round(self, n):
        """Show the nth round"""
        n_round = self.tournament.get_list_of_rounds()[n]
        game_list = n_round.get_list_of_match()
        for game in game_list:
            player1, player2 = game.show_players()
            self.view.display_nth_round_games(player1, player2)

    def display_list_match(self):
        """Introduce the list of matches"""
        self.view.announce_matches()

    def get_match_results(self, n):
        """Ask 8 times for the results of matches"""
        for i in range(int(self.tournament.NUMBER_OF_PLAYER / 2)):
            self.enter_match_results(n, i)

    def enter_match_results(self, nth_round, nth_match):
        """Get the result for the nth match of the nth round"""

        n_round = self.tournament.get_list_of_rounds()[nth_round]
        # Match is considered over so we get the time
        n_round.set_end_date(datetime.now())
        game = n_round.get_list_of_match()[nth_match]
        players = game.get_players()
        # Add the already played player to the player
        self.add_already_played(players)

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

    def give_points_to_players_from_match(self, nth_round):
        list_of_match = self.tournament.get_list_of_rounds()[
            nth_round
        ].get_list_of_match()
        for match in list_of_match:
            match.add_score_to_players()

    def add_already_played(self, players):
        player1 = players[0]
        player2 = players[1]
        player1.add_already_played(player2)
        player2.add_already_played(player1)

    def sort_player(self, nround):
        """Get the result of the previous round"""
        previous_round = []
        for match in self.tournament.get_list_of_rounds()[
            nround - 1
        ].get_list_of_match():
            previous_round.append(match.get_result())
        self.tournament.get_list_of_player().sort(
            key=lambda x: (x.score, x.elo), reverse=True
        )

    def create_nth_round(self, nround):
        # Create first round
        round = Round(f"Round {nround+1}", datetime.now())
        self.tournament.add_round(round)

        # Sort player by Elo
        self.sort_player(nround)
        list_of_player = self.tournament.get_list_of_player()
        copy_of_list_of_player = list_of_player.copy()

        # Create 4 matches for the nth round
        for i in range(int(self.tournament.NUMBER_OF_PLAYER / 2)):
            found = False
            j = 1
            if not copy_of_list_of_player:
                found = True
            while not found:

                player = copy_of_list_of_player[0]
                if copy_of_list_of_player[j] not in player.get_already_played():
                    found = True
                    round.add_game(Match(player, copy_of_list_of_player[j]))
                    del copy_of_list_of_player[0]
                    del copy_of_list_of_player[j - 1]
                else:
                    j = j + 1
