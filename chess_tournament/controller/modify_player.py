from chess_tournament.view.modify_player_view import ModifyPlayerView


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
        player_object = self.get_player_to_change()
        if not player_object:
            self.modify_player_view.player_not_found()
            self.modify_player_view.press_enter_to_continue()
            return
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
        player_to_modify = self.modify_player_view.which_player_to_modify(
            self.list_of_player
        )
        self.modify_player_view.clean_console()
        self.modify_player_view.show_banner()
        if not player_to_modify:
            return
        if not player_to_modify.isdigit():
            return
        if not int(player_to_modify) > -1 and int(player_to_modify) < len(
            self.list_of_player
        ):
            return
        try:
            player_object_to_modify = self.list_of_player[int(player_to_modify)]
        except Exception:
            player_object_to_modify = ""
        return player_object_to_modify

    def get_attribute_to_change(self, player):
        """Ask what to change about the player"""
        attribute_to_change = self.modify_player_view.get_modify_element(player)
        if attribute_to_change == "1":
            player.date_of_birth = self.modify_player_view.get_new_birthday()
            self.modify_player_view.player_modified()

        elif attribute_to_change == "2":
            player.sex = self.modify_player_view.get_new_sex()
            self.modify_player_view.player_modified()

        elif attribute_to_change == "3":
            new_elo = self.modify_player_view.get_new_elo()
            try:
                new_elo_int = int(new_elo)
                player.elo = new_elo_int
                self.modify_player_view.player_modified()

            except ValueError:
                self.modify_player_view.display_elo_not_number_error()

        self.modify_player_view.press_enter_to_continue()
