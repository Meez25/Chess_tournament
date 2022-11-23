from chess_tournament.view.create_player_view import CreatePlayerView
from chess_tournament.models.models import Player


class CreatePlayer:
    """Class to create a user"""

    def __init__(self) -> None:
        self.create_player_view = CreatePlayerView()

    def create_player(self):
        """Function to create a player (ask the user some information)"""
        last_name = self.get_player_last_name()
        first_name = self.get_player_first_name()
        birthday = self.get_player_birthday()
        sex = self.get_player_sex()
        elo = self.get_player_elo()
        player = Player(last_name, first_name, birthday, sex, int(elo))
        return player

    def get_player_last_name(self):
        """Get the last name of the player"""
        valid_input = 0
        while not valid_input:
            last_name = self.create_player_view.ask_player_last_name()
            if last_name:
                valid_input = 1
                return last_name
            else:
                self.create_player_view.display_empty_last_name_error()

    def get_player_first_name(self):
        """Get the first name of the player"""
        valid_input = 0
        while not valid_input:
            first_name = self.create_player_view.ask_player_first_name()
            if first_name:
                valid_input = 1
                return first_name
            else:
                self.create_player_view.display_empty_first_name_error()

    def get_player_birthday(self):
        """Get the birthday of the player"""
        valid_input = 0
        while not valid_input:
            birthday = self.create_player_view.ask_player_birthday()
            if birthday:
                valid_input = 1
                return birthday
            else:
                self.create_player_view.display_empty_birthday_error()

    def get_player_sex(self):
        """Get the last name of the player"""
        valid_input = 0
        while not valid_input:
            sex = self.create_player_view.ask_player_sex()
            if sex:
                valid_input = 1
                return sex
            else:
                self.create_player_view.display_empty_sex_error()

    def get_player_elo(self):
        """Get the elo of the player"""
        valid_input = 0
        while not valid_input:
            elo = self.create_player_view.ask_player_elo()
            if elo and elo.isdigit():
                valid_input = 1
                return elo
            elif not elo:
                self.create_player_view.display_empty_elo_error()
            elif not elo.isdigit():
                self.create_player_view.display_elo_not_number_error()
            else:
                raise Exception("Error in get_player_elo in CreatePlayer Class")
