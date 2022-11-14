from models.models import Player


class PlayerManager:
    def __init__(self, view) -> None:
        self.view = view
        self._list_of_player = []

        # Add test data
        test_data = [
            ["last_name_1", "first_name_1", "birthday_1", "sex_1", "100"],
            ["last_name_2", "first_name_2", "birthday_2", "sex_2", "200"],
            ["last_name_3", "first_name_3", "birthday_3", "sex_3", "300"],
            ["last_name_4", "first_name_4", "birthday_4", "sex_4", "400"],
            ["last_name_5", "first_name_5", "birthday_5", "sex_5", "500"],
            ["last_name_6", "first_name_6", "birthday_6", "sex_6", "600"],
            ["last_name_7", "first_name_7", "birthday_7", "sex_7", "700"],
            ["last_name_8", "first_name_8", "birthday_8", "sex_8", "800"],
        ]

        for player in test_data:
            last_name = player[0]
            first_name = player[1]
            birthday = player[2]
            sex = player[3]
            elo = int(player[4])
            player = Player(last_name, first_name, birthday, sex, elo)
            self._list_of_player.append(player)

    def create_player(self):
        """Create a player"""
        last_name = self.get_player_last_name()
        first_name = self.get_player_first_name()
        birthday = self.get_player_birthday()
        sex = self.get_player_sex()
        elo = self.get_player_elo()
        player = Player(last_name, first_name, birthday, sex, int(elo))
        self._list_of_player.append(player)
        self.view.press_enter_to_continue()
        self.view.clean_console()
        self.view.show_banner()
        return player

    def get_all_players(self):
        """return the list of all player"""
        return self._list_of_player

    def display_all_players(self):
        """Display the list of all players"""
        if not self._list_of_player:
            self.view.display_no_existing_player()
        else:
            self.view.display_list_of_player(self._list_of_player)
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
        if not self.get_all_players():
            self.view.display_no_player_in_database()
            self.view.press_enter_to_continue()
        else:
            self.view.which_player_to_modify(self.get_all_players())
            player_to_modify = self.view.get_player_to_modify().strip()
            self.view.clean_console()
            self.view.show_banner()
            found = False
            for player in self.get_all_players():
                if int(player_to_modify) == player.get_id():
                    found = True
                    attribute_to_change = self.view.get_modify_element(player)
                    if attribute_to_change == "1":
                        player.set_last_name(self.view.get_new_last_name())
                        self.view.player_modified()
                        self.view.press_enter_to_continue()
                    elif attribute_to_change == "2":
                        player.set_first_name(self.view.get_new_first_name())
                        self.view.player_modified()
                        self.view.press_enter_to_continue()
                    elif attribute_to_change == "3":
                        player.set_date_of_birth(self.view.get_new_birthday())
                        self.view.player_modified()
                        self.view.press_enter_to_continue()
                    elif attribute_to_change == "4":
                        player.set_sex(self.view.get_new_sex())
                        self.view.player_modified()
                        self.view.press_enter_to_continue()
                    elif attribute_to_change == "5":
                        new_elo = self.view.get_new_elo()
                        try:
                            new_elo_int = int(new_elo)
                            player.set_elo(new_elo_int)
                            self.view.player_modified()
                            self.view.press_enter_to_continue()
                        except ValueError:
                            self.view.display_elo_not_number_error()
                            self.view.press_enter_to_continue()

                    else:
                        pass
            if found == False:
                self.view.player_not_found(player_to_modify)
                self.view.press_enter_to_continue()
