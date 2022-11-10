from controller.controller import Controller
from view.view import View, main_menu, second_menu
from models.models import Tournament


def main():
    view = View(main_menu())
    tournament = Tournament(
        "Mon tournoi", "Mulhouse", "09/11/2022", "Blitz", "Description de tournoi"
    )
    program = Controller(tournament, view)
    program.run()


if __name__ == "__main__":
    main()
