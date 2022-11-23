from chess_tournament.models.models import Player  # type:ignore
from chess_tournament.view.create_player_view import CreatePlayerView
from chess_tournament.view.modify_player_view import ModifyPlayerView
from chess_tournament.controller.data_manager import SaveData


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

    def insert_player(self, last_name, first_name, birthday, sex, elo, id):
        """Insert player (used to restore the database)"""
        self.list_of_player.append(
            Player(last_name, first_name, birthday, sex, elo, id)
        )

    def reset_player_list(self):
        self.list_of_player = []


class ModifyPlayer:
    """Class dedicated to the modification of a player"""

    def __init__(self, list_of_player, controller) -> None:
        self.list_of_player = list_of_player
        self.controller = controller
        self.modify_player_view = ModifyPlayerView()

    def modify_player(self):
        """Modify a player"""
        if not self.check_if_player():
            return
        player_to_modify = self.get_player_to_change()
        if not self.check_if_player_exist(player_to_modify):
            self.modify_player_view.player_not_found(player_to_modify)
            self.modify_player_view.press_enter_to_continue()
            return
        player_object = self.check_if_player_exist(player_to_modify)
        self.get_attribute_to_change(player_object)

    def check_if_player(self):
        """Check if there is at least a player"""
        if not self.list_of_player:
            self.modify_player_view.display_no_player_in_database()
            self.modify_player_view.press_enter_to_continue()
            return False
        else:
            return True

    def get_player_to_change(self):
        """Ask which player to change"""
        # Ask what is the player to change
        self.modify_player_view.which_player_to_modify(self.list_of_player)
        player_to_modify = self.modify_player_view.get_player_to_modify().strip()
        self.modify_player_view.clean_console()
        self.modify_player_view.show_banner()
        return player_to_modify

    def check_if_player_exist(self, asked_player):
        """Check if the player chosen by the user exist"""
        # Check if the number entered by the user match a real player
        for player in self.list_of_player:
            if asked_player.isdigit():
                if int(asked_player) == player.id:
                    return player
            else:
                self.modify_player_view.player_not_found()

        return False

    def get_attribute_to_change(self, player):
        """Ask what to change about the player"""
        attribute_to_change = self.modify_player_view.get_modify_element(player)
        if attribute_to_change == "1":
            player.last_name = self.modify_player_view.get_new_last_name()
            self.modify_player_view.player_modified()

        elif attribute_to_change == "2":
            player.first_name = self.modify_player_view.get_new_first_name()
            self.modify_player_view.player_modified()

        elif attribute_to_change == "3":
            player.date_of_birth = self.modify_player_view.get_new_birthday()
            self.modify_player_view.player_modified()

        elif attribute_to_change == "4":
            player.sex = self.modify_player_view.get_new_sex()
            self.modify_player_view.player_modified()

        elif attribute_to_change == "5":
            new_elo = self.modify_player_view.get_new_elo()
            try:
                new_elo_int = int(new_elo)
                player.elo = new_elo_int
                self.modify_player_view.player_modified()

            except ValueError:
                self.modify_player_view.display_elo_not_number_error()

        self.modify_player_view.press_enter_to_continue()
