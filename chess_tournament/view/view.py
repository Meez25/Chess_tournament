import os
from datetime import datetime
from chess_tournament.view import ascii


class View:
    """Generic parent view with useful function for the children"""

    def display_selected_tournament(self, selected_tournament):
        """Display the tournament selected by the user"""
        print(f"\nTournoi {selected_tournament} sélectionné")

    def get_tournament_to_select(self):
        print("")
        tournament_to_select = input("Nom du tournoi à sélectionner : ")
        return tournament_to_select

    def show_banner(self):
        ascii.show_banner()

    def display_list_of_tournament(self, list_of_tournament):
        """Display the list of all tournament"""
        print("Liste des tournois\n")
        if not list_of_tournament:
            print("           La liste est vide")
        else:
            for tournament in list_of_tournament:
                print(f"{tournament}")
                print()

    def display_no_existing_player(self):
        print("Il n'y a aucun joueur dans le système. Veuillez en ajouter.")

    def display_no_tournament_selected(self):
        """Display no tournament error"""
        print("Aucun tournoi n'est sélectionné\nVeuillez sélectionner un tournoi.")

    def display_list_of_player(self, list_of_player):
        if not list_of_player:
            print("Il n'y a pas de joueur.")
        else:
            for player in list_of_player:
                print(player)

    def press_enter_to_continue(self):
        input("\nAppuyez sur Entrée pour continuer...\n")

    def clean_console(self):
        os.system("cls" if os.name == "nt" else "clear")

    def player_already_in_tournament(self):
        """Player already in tournament"""
        print("\nLe joueur est déjà dans le tournoi.")

    def format_date(self, date: datetime):
        return date.strftime("%d/%m/%y %H:%M")

    def tournament_selected_not_found(self, selected_tournament):
        """Display an error for tournament not found"""
        print(f"Tournoi {selected_tournament} non trouvé")

    def display_rounds(self, rounds):
        """Display the list of rounds"""
        print("Voici la liste des tours :\n")
        print(
            (
                "\n".join(
                    f"Nom : {round.name}, date de début : "
                    f"{self.format_date(round.start_date)}, date de fin : "
                    f"{self.format_date(round.end_date)}"
                    for round in rounds
                )
            )
        )
