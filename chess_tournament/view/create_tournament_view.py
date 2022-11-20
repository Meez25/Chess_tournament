from chess_tournament.view.view import View


class CreateTournamentView(View):
    def name_cannot_be_empty(self):
        """Display error that the name is empty"""
        print("Le nom ne peut pas être vide")

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
