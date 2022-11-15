import os


class View:
    """Handle the view role"""

    def show_banner(self):
        """Display the banner in the console"""
        print(
            f"{Bcolors.OKBLUE}"
            f"  _____                            _       _ _   __      _               \n"
            f" |_   _|__  _   _ _ __ _ __   ___ (_)   __| ( ) /_/  ___| |__   ___  ___ \n"
            f"   | |/ _ \| | | | '__| '_ \ / _ \| |  / _` |/ / _ \/ __| '_ \ / _ \/ __|\n"
            f"   | | (_) | |_| | |  | | | | (_) | | | (_| | |  __/ (__| | | |  __/ (__ \n"
            f"   |_|\___/ \__,_|_|  |_| |_|\___/|_|  \__,_|  \___|\___|_| |_|\___|\___|\n"
            f"{Bcolors.ENDC}"
        )

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

    def display_empty_elo_error(self):
        """Error message : player's elo is empty"""
        print("Le elo n'a pas été renseigné.")

    def display_elo_not_number_error(self):
        """Error message : player's elo is not number only"""
        print("Le elo doit être composé de chiffre.")

    def ask_start_tournament(self, tournament_name):
        """Ask if ready to start the tournament"""
        ready = input(f"Prêt à démarrer le tournoi {tournament_name} ? o/n ")
        return ready

    def display_yes_or_no_error(self):
        """Generic yes/no error"""
        print("La réponse doit être 'o' ou 'n'")

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

    def tournament_added_successfully(self):
        """Match added successfully"""
        print("\nTournoi ajouté avec succès !")

    def get_user_option(self):
        return input("Entrez votre choix : ")

    def get_index_of_player(self):
        return input("Entrez l'index de votre choix : ")

    def press_enter_to_continue(self):
        input("\nAppuyez sur Entrée pour continuer...\n")

    def clean_console(self):
        os.system("cls" if os.name == "nt" else "clear")

    def get_tournament_name(self):
        name = input("Nom du tournoi ? : ")
        return name

    def get_tournament_location(self):
        tournament_location = input("Lieu ? : ")
        return tournament_location

    def get_tournament_date(self):
        tournament_date = input("Date ? : ")
        return tournament_date

    def get_time_control(self):
        time_control = input("Contrôle du temps ? : ")
        return time_control

    def get_tournament_description(self):
        description = input("Description ? : ")
        return description

    def get_tournament_to_delete(self):
        tournament_to_delete = input(
            "Nom du tournoi à supprimer (Entrée pour annuler): "
        )
        return tournament_to_delete

    def get_tournament_to_select(self):
        tournament_to_select = input("Nom du tournoi à sélectionner : ")
        return tournament_to_select

    def get_player_to_delete_from_tournament(self):
        """ask who to delete from the tournament"""
        player_to_delete = input("[Index] du joueur à supprimer du tournoi: ")
        return player_to_delete

    def get_player_to_modify(self):
        """ask who to modify"""
        player_to_modify = input("[Index] du joueur à modifier du tournoi: ")
        return player_to_modify

    def get_modify_element(self, player):
        """Ask what attribute to modify on the player"""
        print(
            f"Que voulez-vous modifier ?\n\n"
            f"          1 : Nom ({player.get_last_name()})\n"
            f"          2 : Prénom ({player.get_first_name()})\n"
            f"          3 : Date de naissance ({player.get_date_birthday()})\n"
            f"          4 : Sexe ({player.get_sex()})\n"
            f"          5 : Elo ({player.get_elo()})\n"
            f"          6 : Retour\n"
        )
        return input("Entrez votre choix : ")

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

    def player_removed_from_tournament(self, player_to_delete):
        print(f"\nJoueur {player_to_delete} supprimé du tournoi.")

    def player_not_found(self, player):
        print(f'Joueur "{player}" non trouvé')

    def display_tournament_menu(self, current_tournament):
        if not current_tournament:
            print("Aucun tournoi n'est sélectionné\n")
        else:
            print(f'Le tournoi "{current_tournament}" est sélectionné.\n')

        print(
            "Que voulez-vous faire ?\n\n"
            "          1 : Créer un nouveau tournoi\n"
            "          2 : Voir la liste des tournois\n"
            "          3 : Gérer les joueurs du tournoi sélectionné\n"
            "          4 : Sélectionner un autre tournoi\n"
            "          5 : Supprimer un tournoi\n"
            "          6 : Démarrer le tournoi !\n"
            "          7 : Retour\n"
        )

    def display_main_menu(self):
        print(
            "Que voulez-vous faire ?\n\n"
            "          1 : Gestion des tournois\n"
            "          2 : Gérer les joueurs\n"
            "          3 : Rapports\n"
            "          4 : Quitter l'application\n"
        )

    def display_player_menu(self):
        """Display the player menu"""
        print(
            "Que voulez-vous faire ?\n\n"
            "          1 : Ajouter un joueur\n"
            "          2 : Modifier un joueur\n"
            "          3 : Voir la liste des joueurs\n"
            "          4 : Retour\n"
        )

    def display_add_player_to_tournament(self, current_tournament):
        """Display the menu to add a player in the tournament"""
        if not current_tournament:
            print("Aucun tournoi n'est sélectionné\n")
        else:
            print(f'Le tournoi "{current_tournament}" est sélectionné.\n')

        print(
            "Que voulez-vous faire ?\n\n"
            "          1 : Ajouter un nouveau joueur\n"
            "          2 : Ajouter un joueur existant\n"
            "          3 : Afficher la liste des joueurs ajoutés au tournoi\n"
            "          4 : Supprimer un joueur du tournoi\n"
            "          5 : Retour\n"
        )

    def display_no_tournament_selected(self):
        """Display no tournament error"""
        print("Aucun tournoi n'est sélectionné\nVeuillez sélectionner un tournoi.")

    def display_no_player_in_tournament(self):
        """There is no player in the tournament"""
        print("Aucun joueur n'est ajouté au tournoi\nVeuillez ajouter des joueurs")

    def display_no_player_in_database(self):
        """There is no player in the database"""
        print("Aucun joueur n'est ajouté.\nVeuillez ajouter des joueurs")

    def which_player_to_delete(self, list_of_player):
        """Ask which player to delete"""
        print("Quel joueur voulez-vous supprimer ?\n")
        print("[Index] - Nom, Prénom, Elo, Sexe\n")
        for player in list_of_player:
            print(
                f"[{player.get_id()}] - {player.get_last_name()}, "
                f"{player.get_first_name()}, {player.get_elo()}, "
                f"{player.get_sex()}\n"
            )

    def which_player_to_modify(self, list_of_player):
        """Ask which player to modify"""
        print("Quel joueur voulez-vous modifier ?\n")
        print("[Index] - Nom, Prénom, Elo, Sexe\n")
        for player in list_of_player:
            print(
                f"[{player.get_id()}] - {player.get_last_name()}, "
                f"{player.get_first_name()}, {player.get_elo()}, "
                f"{player.get_sex()}\n"
            )

    def player_modified(self):
        print("Joueur modifié")

    def display_existing_player_to_add(self, list_of_player):
        print("Quel joueur voulez-vous ajouter ?\n")
        print("[Index] - Nom, Prénom, Elo, Sexe\n")
        for player in list_of_player:
            print(
                f"[{player.get_id()}] - {player.get_last_name()}, "
                f"{player.get_first_name()}, {player.get_elo()}, "
                f"{player.get_sex()}"
            )
        print("\n")

    def display_list_of_player(self, list_of_player):
        for player in list_of_player:
            print(player)

    def display_no_existing_player(self):
        print("Il n'y a aucun joueur dans le système. Veuillez en ajouter.")

    def player_already_in_tournament(self):
        """Player already in tournament"""
        print("\nLe joueur est déjà dans le tournoi.")

    def player_added_to_tournament(self, player):
        print(
            f"Le joueur {player.get_last_name()} {player.get_first_name()} "
            f"a été ajouté au tournoi."
        )

    def display_list_of_tournament(self, list_of_tournament):
        """Display the list of all tournament"""
        print("Liste des tournois\n")
        if not list_of_tournament:
            print("           La liste est vide")
        else:
            for tournament in list_of_tournament:
                print(f"          - {tournament.name}")
        print("\n")

    def display_selected_tournament(self, selected_tournament):
        """Display the tournament selected by the user"""
        print(f"\nTournoi {selected_tournament} sélectionné")

    def display_deleted_tournament(self, deleted_tournament):
        """Display the tournament deleted by the user"""
        print(f"\nTournoi {deleted_tournament} supprimé")

    def tournament_selected_not_found(self, selected_tournament):
        """Display an error for tournament not found"""
        print(f"Tournoi {selected_tournament} non trouvé")

    def display_need_x_number_of_player(self, number):
        """Print error, not enough or more player"""
        print(
            f"Il n'y a pas le nombre correct de joueur dans le tournoi.\n"
            f"Pour rappel, il en faut {number}"
        )

    def enough_number_of_player(self, number):
        """display there is enough player in the tournament"""
        print(f"Il y a déjà {number} joueurs dans le tournoi.")

    def ask_exit_or_continue(self):
        """Ask if the user wants to continue"""
        self.clean_console()
        self.show_banner()
        print("Voulez-vous démarrer le round suivant ou sauvegarder et quitter ?")
        print("Entrée pour continuer, 'Q' pour sauvegarder et quitter\n")
        return input("Entrez votre choix : ")

    def display_ranking_end_of_tournament(self, ranking):
        """Display the final ranking and end the tournament"""
        self.clean_console()
        self.show_banner()
        print("Voici le classement final de ce tournoi : \n")
        for player in ranking:
            print(f"{player[0]} avec {player[1]} points !")

    def tournament_is_over(self):
        """The tournament is over !"""
        print("Le tournoi est déjà terminé !")

    def no_tournament_error(self):
        """Display an error because there is no tournament"""
        print("Il n'y a aucun tournoi à sélectionner\n")

    def name_cannot_be_empty(self):
        """Display error that the name is empty"""
        print("Le nom ne peut pas être vide")

    def tournament_playing_error(self):
        """The player cannot be changed"""
        print("Les joueurs ne peuvent pas être changé car le tournoi a débuté.")


class Bcolors:
    """class helper for color"""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
