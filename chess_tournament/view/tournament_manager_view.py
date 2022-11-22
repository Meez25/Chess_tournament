from chess_tournament.view.view import View


class TournamentManagerView(View):
    """Class for the play of the tournament actions"""

    def which_player_to_delete(self, list_of_player):
        """Ask which player to delete"""
        print("Quel joueur voulez-vous supprimer ?\n")
        print("[Index] - Nom, Prénom, Elo, Sexe\n")
        for player in list_of_player:
            print(
                f"[{player.id}] - {player.last_name}, "
                f"{player.first_name}, {player.elo}, "
                f"{player.sex}\n"
            )

    def tournament_added_successfully(self):
        """Match added successfully"""
        print("\nTournoi ajouté avec succès !")

    def enough_number_of_player(self, number):
        """display there is enough player in the tournament"""
        print(f"Il y a déjà {number} joueurs dans le tournoi.")

    def display_existing_player_to_add(self, list_of_player):
        print("Quel joueur voulez-vous ajouter ?\n")
        print("[Index] - Nom, Prénom, Elo, Sexe\n")
        for player in list_of_player:
            print(
                f"[{player.id}] - {player.last_name}, "
                f"{player.first_name}, {player.elo}, "
                f"{player.sex}"
            )
        print("\n")

    def get_index_of_player(self):
        return input("Entrez l'index de votre choix : ")

    def player_added_to_tournament(self, player):
        print(
            f"Le joueur {player.last_name} {player.first_name} "
            f"a été ajouté au tournoi."
        )

    def tournament_selected_not_found(self, selected_tournament):
        """Display an error for tournament not found"""
        print(f"Tournoi {selected_tournament} non trouvé")

    def get_tournament_to_delete(self):
        tournament_to_delete = input(
            "Nom du tournoi à supprimer (Entrée pour annuler): "
        )
        return tournament_to_delete

    def display_deleted_tournament(self, deleted_tournament):
        """Display the tournament deleted by the user"""
        print(f"\nTournoi {deleted_tournament} supprimé")

    def display_no_player_in_tournament(self):
        """There is no player in the tournament"""
        print("Aucun joueur n'est ajouté au tournoi\nVeuillez ajouter des joueurs")

    def get_player_to_delete_from_tournament(self):
        """ask who to delete from the tournament"""
        player_to_delete = input("[Index] du joueur à supprimer du tournoi: ")
        return player_to_delete

    def player_removed_from_tournament(self, player_to_delete):
        print(f"\nJoueur {player_to_delete} supprimé du tournoi.")

    def player_not_found(self, player):
        print(f'Joueur "{player}" non trouvé')

    def ask_exit_or_continue(self):
        """Ask if the user wants to continue"""
        print("Voulez-vous démarrer le round suivant ou sauvegarder et quitter ?")
        print("Entrée pour continuer, 'Q' pour sauvegarder et quitter\n")
        return input("Entrez votre choix : ")

    def display_need_x_number_of_player(self, number):
        """Print error, not enough or more player"""
        print(
            f"Il n'y a pas le nombre correct de joueur dans le tournoi.\n"
            f"Pour rappel, il en faut {number}"
        )

    def tournament_is_over(self):
        """The tournament is over !"""
        print("Le tournoi est déjà terminé !")

    def display_ranking_end_of_tournament(self, ranking):
        """Display the final ranking and end the tournament"""
        self.clean_console()
        self.show_banner()
        print("Voici le classement final de ce tournoi : \n")
        for player in ranking:
            print(f"{player[0]} avec {player[1]} points !")

    def display_ranking(self, ranking):
        """Display the ranking of the tournament"""
        self.clean_console()
        self.show_banner()
        print("Voici le classement actuel : \n")
        for player in ranking:
            print(f"{player[0]} avec {player[1]} points !")
        print()

    def announce_matches(self):
        """Introduces match to play"""
        print("Voici la liste des matchs à jouer : \n")

    def display_nth_round_games(self, player1, player2):
        """Introduce matches generated"""
        print(
            f"{player1.last_name} {player1.first_name} contre "
            f"{player2.last_name} {player2.first_name}"
        )

    def ask_results(self, player):
        """Ask for match results"""
        score_player = input(
            f"Quel est le résultat de"
            f" {player.last_name} {player.first_name} ? (0, 0.5, 1) "
        )
        return score_player

    def display_score_error(self):
        """Match result input error"""
        print("Le score ne peut être que 0, 0,5 ou 1.")

    def no_round(self):
        """Display no round error"""
        print("\nIl n'y a pas encore de tours dans le tournoi.\n")

    def no_matchs(self):
        """Display no round error"""
        print("\nIl n'y a pas encore de matchs dans le tournoi.\n")

    def display_matchs(self, matchs):
        """Display the list of matchs"""
        print("Voici la liste des matchs :\n")
        print("\n".join(f"{match.get_result_formatted()}" for match in matchs))

    def display_no_player_in_database(self):
        """There is no player in the database"""
        print("Aucun joueur n'est ajouté.\nVeuillez ajouter des joueurs")

    def finished_adding_player(self):
        """Ask if the user is done adding player"""
        return input("Entrée pour continuer, q pour quitter")

    def must_be_a_number(self):
        """Error, the input must be a number"""
        print("Veuillez entrer un chiffre")
