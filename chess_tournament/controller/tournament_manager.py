from models.models import Player, Match, Round, Tournament
from datetime import datetime


class TournamentManager:
    def __init__(self, view, player_manager) -> None:
        self.view = view
        self.player_manager = player_manager
        self.tournament_list = []
        self.tournament = ""

    def create_tournament(self):
        tournament_name = self.get_tournament_name()
        tournament_location = self.get_tournament_location()
        tournament_date = self.get_tournament_date()
        time_control = self.get_time_control()
        tournament_description = self.get_tournament_description()
        self.tournament = Tournament(tournament_name, tournament_location,
        tournament_date, time_control, tournament_description)
        self.tournament_list.append(self.tournament)
        self.view.tournament_added_successfully()
        self.view.press_enter_to_continue()

    def get_tournament(self):
        if not self.tournament:
            return ""
        else:
            return self.tournament.get_tournament_name()

    def add_player_to_tournament(self, player):
        self.tournament.add_player_in_list(player)

    def get_tournament_name(self):
        tournament_name = self.view.get_tournament_name()
        return tournament_name

    def get_tournament_location(self):
        tournament_location = self.view.get_tournament_location()
        return tournament_location

    def get_tournament_date(self):
        tournament_date = self.view.get_tournament_date()
        return tournament_date

    def get_time_control(self):
        time_control = self.view.get_time_control()
        return time_control

    def get_tournament_description(self):
        tournament_description = self.view.get_tournament_description()
        return tournament_description

    def add_existing_player_to_tournament(self):
        if not self.player_manager.get_all_players():
            self.view.display_no_existing_player()
            self.view.press_enter_to_continue()
        else:
            list_of_all_players = self.player_manager.get_all_players()
            self.view.display_existing_player_to_add(list_of_all_players)
            
            player_index = self.view.get_index_of_player()
            for player in list_of_all_players:
                if player.get_id() == int(player_index):
                    if player not in list_of_all_players:
                        self.tournament.add_player_in_list(player)
                        print(self.tournament.list_of_players)
                    else:
                        self.view.player_already_in_tournament()
                        self.view.press_enter_to_continue()

    def change_selected_tournament(self):
        self.view.print("Liste des tournois\n")
        if not self.tournament_list:
            self.view.print("           La liste est vide")
            self.view.press_enter_to_continue()
        else:
            for tournament in self.tournament_list:
                self.view.print(f"          - {tournament.name}")
            tournament_to_select = self.view.get_tournament_to_select().strip()
            found = 0
            for tournament in self.tournament_list:
                if tournament.name.lower() == tournament_to_select.lower():
                    self.tournament = tournament
                    self.view.print(f"\nTournoi {tournament_to_select} sélectionné")
                    self.view.press_enter_to_continue()
                    found = 1
                    break
            if not found:    
                self.view.print(f"Tournoi {tournament_to_select} non trouvé")
                self.view.press_enter_to_continue()

    def display_all_tournament(self):
        self.view.print("Liste des tournois\n")
        if not self.tournament_list:
            self.view.print("           La liste est vide")
            self.view.press_enter_to_continue()
        else:
            for tournament in self.tournament_list:
                self.view.print(f"          - {tournament.name}")
            self.view.press_enter_to_continue()

    def delete_tournament(self):
        self.view.print("Liste des tournois\n")
        if not self.tournament_list:
            self.view.print("           La liste est vide")
            self.view.press_enter_to_continue()
        else:
            for tournament in self.tournament_list:
                self.view.print(f"          - {tournament.name}\n")
            tournament_to_delete = self.view.get_tournament_to_delete().strip()
            found = 0
            for tournament in self.tournament_list:
                if tournament.name.lower() == tournament_to_delete.lower():
                    self.tournament_list.remove(tournament)
                    self.view.print(f"\nTournoi {tournament_to_delete} supprimé")
                    if self.tournament == tournament:
                        self.tournament = ""
                    self.view.press_enter_to_continue()
                    found = 1
                    break
            if not found:
                self.view.print(f"Tournoi {tournament_to_delete} non trouvé")
                self.view.press_enter_to_continue()

    def display_tournament_players(self):
        if not self.tournament.get_list_of_player():
            self.view.display_no_player_in_tournament()
        else:
            self.view.display_list_of_player(self.tournament.get_list_of_player())
        self.view.press_enter_to_continue()

    def remove_player_from_tournament(self):

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

    def get_players(self):
        """test_data = [
            ["last_name_1", "first_name_1", "birthday_1", "sex_1", "100"],
            ["last_name_2", "first_name_2", "birthday_2", "sex_2", "200"],
            ["last_name_3", "first_name_3", "birthday_3", "sex_3", "300"],
            ["last_name_4", "first_name_4", "birthday_4", "sex_4", "400"],
            ["last_name_5", "first_name_5", "birthday_5", "sex_5", "500"],
            ["last_name_6", "first_name_6", "birthday_6", "sex_6", "600"],
            ["last_name_7", "first_name_7", "birthday_7", "sex_7", "700"],
            ["last_name_8", "first_name_8", "birthday_8", "sex_8", "800"],
        ]"""

        for i in range(self.tournament.NUMBER_OF_PLAYER):
            last_name = self.get_player_last_name()
            first_name = self.get_player_first_name()
            birthday = self.get_player_birthday()
            sex = self.get_player_sex()
            elo = self.get_player_elo()
            player = Player(last_name, first_name, birthday, sex, int(elo))
            
            self.tournament.add_player_in_list(player)
        
        for player in test_data:
            last_name = player[0]
            first_name = player[1]
            birthday = player[2]
            sex = player[3]
            elo = int(player[4])
            player = Player(last_name, first_name, birthday, sex, elo)
            self.tournament.add_player_in_list(player)

    def get_ready(self):
        valid_input = 0
        while not valid_input:
            ready = self.view.ask_start_tournament(self.tournament.name)
            if ready.lower() == "o" or ready.lower() == "n":
                valid_input = 1
                if ready.lower() == "o":
                    return True
                elif ready.lower() == "n":
                    return False
            else:
                self.view.display_yes_or_no_error()

    def get_player_last_name(self):
        valid_input = 0
        while not valid_input:
            last_name = self.view.ask_player_last_name()
            if last_name:
                valid_input = 1
                return last_name
            else:
                self.view.display_empty_last_name_error()

    def get_player_first_name(self):
        valid_input = 0
        while not valid_input:
            first_name = self.view.ask_player_first_name()
            if first_name:
                valid_input = 1
                return first_name
            else:
                self.view.display_empty_first_name_error()

    def get_player_birthday(self):
        valid_input = 0
        while not valid_input:
            birthday = self.view.ask_player_birthday()
            if birthday:
                valid_input = 1
                return birthday
            else:
                self.view.display_empty_birthday_error()

    def get_player_sex(self):
        valid_input = 0
        while not valid_input:
            sex = self.view.ask_player_sex()
            if sex:
                valid_input = 1
                return sex
            else:
                self.view.display_empty_sex_error()

    def get_player_elo(self):
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
        n_round = self.tournament.get_list_of_rounds()[n]
        game_list = n_round.get_list_of_match()
        for game in game_list:
            player1, player2 = game.show_players()
            self.view.display_nth_round_games(player1, player2)

    def display_list_match(self):
        self.view.announce_matches()

    def get_match_results(self, n):
        for i in range(int(self.tournament.NUMBER_OF_PLAYER / 2)):
            self.enter_match_results(n, i)

    def enter_match_results(self, nth_round, nth_match):
        n_round = self.tournament.get_list_of_rounds()[nth_round]
        game = n_round.get_list_of_match()[nth_match]
        players = game.get_players()

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
                        ].get_list_of_match()[nth_match].set_score_player_1(
                            float(score)
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
                        ].get_list_of_match()[nth_match].set_score_player_2(
                            float(score)
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

    def sort_player(self):
        self.tournament.get_list_of_player().sort(
            key=lambda x: (x.score, x.elo), reverse=True
        )

    def create_nth_round(self, n):
        # Create first round
        round = Round(f"Round {n+1}", datetime.now())
        self.tournament.add_round(round)

        # Sort player by Elo
        self.sort_player()
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
