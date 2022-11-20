from chess_tournament.controller.controller import Controller
from chess_tournament.view.view import View  # type:ignore


def main():
    """Start the main program"""
    view = View()
    program = Controller(view)
    program.run()


if __name__ == "__main__":
    main()
