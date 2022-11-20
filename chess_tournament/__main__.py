from chess_tournament.controller.controller import Controller
from chess_tournament.view.menu_view import MenuView  # type:ignore


def main():
    """Start the main program"""
    view = MenuView()
    program = Controller(view)
    program.run()


if __name__ == "__main__":
    main()
