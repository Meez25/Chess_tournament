from chess_tournament.view.view import View


class MenuView(View):
    """Class that handle the menus"""

    def get_user_option(self):
        return input("Entrez votre choix : ")

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

    def no_tournament_error(self):
        """Display an error because there is no tournament"""
        print("Il n'y a aucun tournoi à sélectionner\n")

    def tournament_playing_error(self):
        """The player cannot be changed"""
        print("Les joueurs ne peuvent pas être changé car le tournoi a débuté.")

    def display_report_menu(self):
        """Display the report menu"""
        print(
            "Que voulez-vous voir ?\n\n"
            "          1 : Tous les joueurs\n"
            "          2 : Tous les joueurs d'un tournoi\n"
            "          3 : Tous les tournois\n"
            "          4 : Tous les tours d'un tournoi\n"
            "          5 : Tous les matchs d'un tournoi\n"
            "          6 : Retour\n"
        )

    def display_all_player_report_options(self):
        """Display all option for the player report"""
        print(
            "Comment voulez-vous voir le rapport ?\n\n"
            "          1 : Ordre alphabétique\n"
            "          2 : Par elo\n"
            "          3 : Retour\n"
        )
