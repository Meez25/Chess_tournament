import os
from datetime import datetime

from chess_tournament.view.bcolors import Bcolors


class View:
    def display_selected_tournament(self, selected_tournament):
        """Display the tournament selected by the user"""
        print(f"\nTournoi {selected_tournament} sélectionné")

    def get_tournament_to_select(self):
        print("")
        tournament_to_select = input("Nom du tournoi à sélectionner : ")
        return tournament_to_select

    def display_list_of_tournament(self, list_of_tournament):
        """Display the list of all tournament"""
        print("Liste des tournois\n")
        if not list_of_tournament:
            print("           La liste est vide")
        else:
            for tournament in list_of_tournament:
                print(f"          - {tournament.name}")

    def display_no_existing_player(self):
        print("Il n'y a aucun joueur dans le système. Veuillez en ajouter.")

    def display_no_tournament_selected(self):
        """Display no tournament error"""
        print("Aucun tournoi n'est sélectionné\nVeuillez sélectionner un tournoi.")

    def display_list_of_player(self, list_of_player):
        for player in list_of_player:
            print(player)

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

    def press_enter_to_continue(self):
        input("\nAppuyez sur Entrée pour continuer...\n")

    def clean_console(self):
        os.system("cls" if os.name == "nt" else "clear")

    def player_already_in_tournament(self):
        """Player already in tournament"""
        print("\nLe joueur est déjà dans le tournoi.")

    def format_date(self, date: datetime):
        return date.strftime("%d/%m/%y %H:%M")

    def display_rounds(self, rounds):
        """Display the list of rounds"""
        print("Voici la liste des tours :\n")
        print(
            (
                "\n".join(
                    f"Nom : {round.name}, date de début : {self.format_date(round.start_date)}, date de fin : {self.format_date(round.end_date)}"
                    for round in rounds
                )
            )
        )
