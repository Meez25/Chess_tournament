from controller.controller import Controller
from view.view import View  # type:ignore


def main():
    """Start the main program"""
    view = View()
    program = Controller(view)
    program.setup()
    program.run()


if __name__ == "__main__":
    main()
