from models.models import Player
import os


class PlayerManager:
    def __init__(self, player_database, view) -> None:
        self.player_database = player_database
        self.view = view
        self._list_of_player = []

    
    def create_player(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.view.show_banner()

        last_name = self.get_player_last_name()
        first_name = self.get_player_first_name()
        birthday = self.get_player_birthday()
        sex = self.get_player_sex()
        elo = self.get_player_elo()
        player = Player(last_name, first_name, birthday, sex, int(elo))
        self._list_of_player.append(player)

    
    def display_all_players(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.view.show_banner()

        for player in self._list_of_player:
            print(player)

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

