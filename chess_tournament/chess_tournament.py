from controller.controller import Controller
from view.view import View
from models.models import Tournament, Player_Database


def main():
    view = View()
    player_database = Player_Database()
    tournament = Tournament(
        "Mon tournoi", "Mulhouse", "09/11/2022", "Rapide", "Description de tournoi"
    )

    program = Controller(tournament, view, player_database)
    program.run()


if __name__ == "__main__":
    main()
