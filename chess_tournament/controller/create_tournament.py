from chess_tournament.view.create_tournament_view import CreateTournamentView
from chess_tournament.models.models import Tournament


class CreateTournament:
    """Class that create the tournament"""

    def __init__(self) -> None:
        self.modify_player_view = CreateTournamentView()

    def create_tournament(self):
        """Create a tournament by calling the view and adding
        it to the list of tournament"""
        tournament_name = self.get_tournament_name_from_view()
        tournament_location = self.get_tournament_location()
        tournament_date = self.get_tournament_date()
        time_control = self.get_time_control()
        tournament_description = self.get_tournament_description()
        self.tournament = Tournament(
            tournament_name,
            tournament_location,
            tournament_date,
            time_control,
            tournament_description,
        )
        return self.tournament

    def get_tournament_name_from_view(self):
        """Get the current tournament's name"""
        while True:
            tournament_name = self.modify_player_view.get_tournament_name()
            if not tournament_name:
                self.modify_player_view.name_cannot_be_empty()
                continue
            else:
                break
        return tournament_name

    def get_tournament_location(self):
        """Get the current tournament location"""
        tournament_location = self.modify_player_view.get_tournament_location()
        return tournament_location

    def get_tournament_date(self):
        """Get the current tournament date"""
        tournament_date = self.modify_player_view.get_tournament_date()
        return tournament_date

    def get_time_control(self):
        """Get the current tournament time control"""
        time_control = self.modify_player_view.get_time_control()
        return time_control

    def get_tournament_description(self):
        """Get the current tournament description"""
        tournament_description = self.modify_player_view.get_tournament_description()
        return tournament_description
