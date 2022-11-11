from controller.controller import Controller
from view.view import View
from models.models import Tournament


def main():
    view = View()
    tournament = Tournament(
        "Mon tournoi", "Mulhouse", "09/11/2022", "Rapide", "Description de tournoi"
    )

    program = Controller(tournament, view)
    program.run()


if __name__ == "__main__":
    main()
