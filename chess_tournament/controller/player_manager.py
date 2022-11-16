from models.models import Player  # type:ignore


class PlayerManager:
    def __init__(self, view) -> None:
        self.view = view
        self.list_of_player = []

    def create_player(self):
        """Create a player"""
        last_name = self.get_player_last_name()
        first_name = self.get_player_first_name()
        birthday = self.get_player_birthday()
        sex = self.get_player_sex()
        elo = self.get_player_elo()
        player = Player(last_name, first_name, birthday, sex, int(elo))
        self.list_of_player.append(player)
        self.view.press_enter_to_continue()
        self.view.clean_console()
        self.view.show_banner()
        return player

    def display_all_players(self):
        """Display the list of all players"""
        if not self.list_of_player:
            self.view.display_no_existing_player()
        else:
            self.view.display_list_of_player(self.list_of_player)
        self.view.press_enter_to_continue()
        self.view.clean_console()
        self.view.show_banner()

    def get_player_last_name(self):
        """Get the last name of the player"""
        valid_input = 0
        while not valid_input:
            last_name = self.view.ask_player_last_name()
            if last_name:
                valid_input = 1
                return last_name
            else:
                self.view.display_empty_last_name_error()

    def get_player_first_name(self):
        """Get the first name of the player"""
        valid_input = 0
        while not valid_input:
            first_name = self.view.ask_player_first_name()
            if first_name:
                valid_input = 1
                return first_name
            else:
                self.view.display_empty_first_name_error()

    def get_player_birthday(self):
        """Get the birthday of the player"""
        valid_input = 0
        while not valid_input:
            birthday = self.view.ask_player_birthday()
            if birthday:
                valid_input = 1
                return birthday
            else:
                self.view.display_empty_birthday_error()

    def get_player_sex(self):
        """Get the last name of the player"""
        valid_input = 0
        while not valid_input:
            sex = self.view.ask_player_sex()
            if sex:
                valid_input = 1
                return sex
            else:
                self.view.display_empty_sex_error()

    def get_player_elo(self):
        """Get the elo of the player"""
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

    def modify_player(self):
        """Modify a player"""
        if not self.list_of_player:
            self.view.display_no_player_in_database()
            self.view.press_enter_to_continue()
        else:
            self.view.which_player_to_modify(self.list_of_player)
            player_to_modify = self.view.get_player_to_modify().strip()
            self.view.clean_console()
            self.view.show_banner()
            found = False
            for player in self.list_of_player:
                if int(player_to_modify) == player.id:
                    found = True
                    attribute_to_change = self.view.get_modify_element(player)
                    if attribute_to_change == "1":
                        player.last_name = self.view.get_new_last_name()
                        self.view.player_modified()
                        self.view.press_enter_to_continue()
                    elif attribute_to_change == "2":
                        player.first_name = self.view.get_new_first_name()
                        self.view.player_modified()
                        self.view.press_enter_to_continue()
                    elif attribute_to_change == "3":
                        player.date_of_birth = self.view.get_new_birthday()
                        self.view.player_modified()
                        self.view.press_enter_to_continue()
                    elif attribute_to_change == "4":
                        player.sex = self.view.get_new_sex()
                        self.view.player_modified()
                        self.view.press_enter_to_continue()
                    elif attribute_to_change == "5":
                        new_elo = self.view.get_new_elo()
                        try:
                            new_elo_int = int(new_elo)
                            player.elo = new_elo_int
                            self.view.player_modified()
                            self.view.press_enter_to_continue()
                        except ValueError:
                            self.view.display_elo_not_number_error()
                            self.view.press_enter_to_continue()

                    else:
                        pass
            if not found:
                self.view.player_not_found(player_to_modify)
                self.view.press_enter_to_continue()
