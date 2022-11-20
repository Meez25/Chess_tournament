from chess_tournament.view.view import View


class CreatePlayerView(View):
    def ask_player_last_name(self):
        """Ask for the player's name"""
        last_name = input("Nom de famille ? : ")
        return last_name

    def display_empty_last_name_error(self):
        """Error message : player's name not found"""
        print("Désolé, le nom du joueur n'a pas été renseigné.")

    def ask_player_first_name(self):
        """Ask for the player's first name"""
        first_name = input("Prénom ? : ")
        return first_name

    def display_empty_first_name_error(self):
        """Error message : player's name empty"""
        print("Désolé, le prénom du joueur n'a pas été renseigné.")

    def ask_player_birthday(self):
        """Ask for the player's birthday"""
        birthday = input("Date de naissance ? : ")
        return birthday

    def display_empty_birthday_error(self):
        """Error message : player's birthday is empty"""
        print("Désolé, la date de naissance n'a pas été renseigné.")

    def ask_player_sex(self):
        """Ask for the player's sex"""
        sex = input("Sexe ? : ")
        return sex

    def display_empty_sex_error(self):
        """Error message : player's sex is empty"""
        print("Désolé, le sexe n'a pas été renseigné.")

    def ask_player_elo(self):
        """Ask for the player's elo"""
        elo = input("Elo ? : ")
        return elo
