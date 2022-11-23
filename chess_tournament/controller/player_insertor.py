from chess_tournament.controller.create_player import CreatePlayer


class PlayerInsertor:
    """Class to add a player in a tournament or add an existing player"""

    def __init__(self, view, player_manager, tournament=None) -> None:
        self.tournament = tournament
        self.view = view
        self.player_manager = player_manager

    def add_player_to_tournament(self):
        """Add a player to the current tournament"""
        if not self.tournament.is_full():
            player = CreatePlayer().create_player()
            self.tournament.add_player_in_list(player)
            self.player_manager.list_of_player.append(player)
        else:
            self.view.enough_number_of_player(self.tournament.NUMBER_OF_PLAYER)
            self.view.press_enter_to_continue()

    def get_player(self):
        """Ask which player"""

        player_index = self.view.display_existing_player_to_add(
            self.player_manager.list_of_player
        )

        self.view.clean_console()
        self.view.show_banner()
        if not player_index:
            return
        if not player_index.isdigit():
            return
        if not int(player_index) > -1 and int(player_index) < len(
            self.player_manager.list_of_player
        ):
            return
        player_object_to_modify = ""
        try:
            player_object_to_modify = self.player_manager.list_of_player[
                int(player_index)
            ]
        except Exception:
            print(Exception)
        return player_object_to_modify

    def add_existing_player_to_tournament(self):
        """Add an existing player to the current tournament"""
        # If there is no player in the "database", send error message
        finished_to_add_player = False
        while not finished_to_add_player:
            if self.tournament.is_full():
                self.view.enough_number_of_player(self.tournament.NUMBER_OF_PLAYER)
                self.view.press_enter_to_continue()
                finished_to_add_player = True
            else:
                # Display the list of all players so the user can select

                player_object = self.get_player()

                # Get the tournament import to avoid duplicates
                list_of_tournament_player = self.tournament.list_of_players
                # Get the choice of the user
                if self.tournament.is_full():
                    self.view.enough_number_of_player(self.tournament.NUMBER_OF_PLAYER)
                    self.view.press_enter_to_continue()
                    return

                # If the player is not already in the tournament
                # Add the player to tournament
                if player_object not in list_of_tournament_player:
                    self.tournament.add_player_in_list(player_object)
                    self.view.player_added_to_tournament(player_object)
                    user_reply = self.view.finished_adding_player()
                    if user_reply.lower() == "q":
                        finished_to_add_player = True
                        return

                else:
                    self.view.player_already_in_tournament()
                    self.view.press_enter_to_continue()
                    return
