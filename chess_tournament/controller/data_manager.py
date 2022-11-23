from tinydb import TinyDB
from abc import ABC, abstractmethod


class SaveData:
    """Class used to save the data in the database"""

    def __init__(self, player_manager=None, tournament_manager=None) -> None:
        self.db = TinyDB("db.json")
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def insert_player(self):
        """Insert the player in the player table"""
        players_table = self.db.table("players")
        players_table.truncate()
        all_players = self.player_manager.list_of_player
        for player in all_players:
            players_table.insert(player.__dict__)

    def insert_tournament(self):
        """Insert the tournament in the tournament table"""
        all_tournament = self.tournament_manager.tournament_list

        tournaments_table = self.db.table("tournaments")
        tournaments_table.truncate()

        for tournament in all_tournament:
            tournaments_table.insert(tournament.serialize())

    def save(self):
        """Insert both player and tournament in the database"""
        self.insert_player()
        self.insert_tournament()


class DataRestorer(ABC):
    """Abstract class that could possibly handle several type of storage"""

    @abstractmethod
    def get_player(self):
        """Get the player table from the storage"""

    def get_tournament(self):
        """Get the tournament table from the storage"""


class RestoreDataTinyDB(DataRestorer):
    """Class that inherite from the abstract class DataRestorer and
    that is using TinyDB"""

    def __init__(self) -> None:
        self.db = TinyDB("db.json")
        self.player_manager = None
        self.tournament_manager = None

    def get_player(self):
        """Get the player table from the Tiny DB"""
        players_table = self.db.table("players")

        serialized_players = players_table.all()
        return serialized_players

    def get_tournament(self):
        """Get the tournament table from the Tiny DB"""

        tournaments_table = self.db.table("tournaments")

        list_of_tournament = []
        for item in tournaments_table:
            list_of_tournament.append(item)

        return list_of_tournament


class RestoreData:
    """This class recreate all objects from a dict"""

    def __init__(self, r: DataRestorer, player_manager, tournament_manager) -> None:
        self.data_restorer = r
        self.serialized_players = self.data_restorer.get_player()
        self.serialized_tournaments = self.data_restorer.get_tournament()
        self.player_manager = player_manager
        self.tournament_manager = tournament_manager

    def recreate_players(self):
        """From the database, recreate the player objects"""
        self.player_manager.reset_player_list()
        for player in self.serialized_players:
            self.player_manager.insert_player(
                player["last_name"],
                player["first_name"],
                player["date_of_birth"],
                player["sex"],
                player["elo"],
            )

    def recreate_tournament(self):
        """From the database, recreate the tournament objects"""
        self.tournament_manager.clear_tournament()
        for tournament in self.serialized_tournaments:

            self.tournament_manager.insert_tournament(
                tournament["name"],
                tournament["location"],
                tournament["date"],
                tournament["time_control"],
                tournament["description"],
                tournament["list_of_player"],
                tournament["list_of_round"],
                tournament["progression"],
            )
