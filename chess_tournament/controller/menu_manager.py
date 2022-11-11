from abc import ABC, abstractmethod


class MenuManager:
    _state = None

    def __init__(self, state, view) -> None:
        self.transition_to(state)
        self.view = view
        self.view.show_welcome_message()

    def transition_to(self, state):
        print(f"MenuManager: Transition to {type(state).__name__}")
        self._state = state
        self._state.menu_manager = self
        

    def print_menu(self):
        self._state.print_menu()

    def get_user_option(self):
        self._state.get_user_option()

class State(ABC):
    @property
    def menu_manager(self) -> MenuManager:
        return self._menu_manager

    @menu_manager.setter
    def menu_manager(self, menu_manager: MenuManager) -> None:
        self._menu_manager = menu_manager

    @abstractmethod
    def print_menu(self) -> None:
        pass

    @abstractmethod
    def get_user_option(self) -> None:
        pass

class Main_menu(State):

    def __init__(self, view) -> None:
        self.view = view

    def print_menu(self) -> None:
        self.view.print("Je suis le main menu")
        
    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == '1':
            self.menu_manager.transition_to(Tournament_menu(self.view))

class Tournament_menu(State):

    def __init__(self, view) -> None:
        self.view = view

    def print_menu(self) -> None:
        self.view.print("Je suis le tournament menu")

    def get_user_option(self) -> None:
        user_option = self.view.get_user_option()
        if user_option == '1':
            self.menu_manager.transition_to(Main_menu(self.view))