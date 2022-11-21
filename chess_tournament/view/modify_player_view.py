from chess_tournament.view.view import View


class ModifyPlayerView(View):
    def which_player_to_modify(self, list_of_player):
        """Ask which player to modify"""
        print("Quel joueur voulez-vous modifier ?\n")
        print("[Index] - Nom, Prénom, Elo, Sexe\n")
        for player in list_of_player:
            print(
                f"[{player.id}] - {player.last_name}, "
                f"{player.first_name}, {player.elo}, "
                f"{player.sex}\n"
            )

    def player_modified(self):
        print("Joueur modifié")

    def get_modify_element(self, player):
        """Ask what attribute to modify on the player"""
        print(
            f"Que voulez-vous modifier ?\n\n"
            f"          1 : Nom ({player.last_name})\n"
            f"          2 : Prénom ({player.first_name})\n"
            f"          3 : Date de naissance ({player.date_of_birth})\n"
            f"          4 : Sexe ({player.sex})\n"
            f"          5 : Elo ({player.elo})\n"
            f"          6 : Retour\n"
        )
        return input("Entrez votre choix : ")

    def get_player_to_modify(self):
        """ask who to modify"""
        player_to_modify = input("[Index] du joueur à modifier du tournoi: ")
        return player_to_modify

    def get_new_last_name(self):
        return input("Nouveau nom : ")

    def get_new_first_name(self):
        return input("Nouveau prénom : ")

    def get_new_birthday(self):
        return input("Nouvelle date de naissance : ")

    def get_new_sex(self):
        return input("Nouveau sexe : ")

    def get_new_elo(self):
        return input("Nouvel elo : ")

    def display_empty_elo_error(self):
        """Error message : player's elo is empty"""
        print("Le elo n'a pas été renseigné.")

    def display_elo_not_number_error(self):
        """Error message : player's elo is not number only"""
        print("Le elo doit être composé de chiffre.")

    def player_not_found(self, player):
        print(f'Joueur "{player}" non trouvé')
