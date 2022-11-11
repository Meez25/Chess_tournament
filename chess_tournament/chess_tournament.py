from controller.controller import Controller
from controller.menu_manager import MenuManager, Main_menu, Tournament_menu
from view.view import View
from models.models import Tournament


def main():
    view = View()
    tournament = Tournament(
        "Mon tournoi", "Mulhouse", "09/11/2022", "Rapide", "Description de tournoi"
    )
    menu_manager = MenuManager(Main_menu(view))
    program = Controller(tournament, view, menu_manager)
    program.run()


if __name__ == "__main__":
    main()
