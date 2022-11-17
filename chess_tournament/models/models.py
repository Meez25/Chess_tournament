from dataclasses import dataclass, field
from enum import Enum
from itertools import count


class Match:
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2
        self.result = {}

    def serialize(self):
        return {
            "player1": self.player1.serialize(),
            "player2": self.player2.serialize(),
            "result": {
                "0": {"0": self.result[0][0].serialize(), "1": self.result[0][1]},
                "1": {"0": self.result[1][0].serialize(), "1": self.result[1][1]},
            },
        }

    def get_players(self):
        return [self.player1, self.player2]

    def set_result(self, player, score):
        self.result = list(self.result)
        self.result.append([player, score])
        self.result = tuple(self.result)

    def get_result(self):
        """Get the result of the game"""
        return self.result

    def __str__(self):
        return f"{self.player1.last_name} contre {self.player2.last_name}"

    def __repr__(self):
        return f"{self.player1.last_name} contre {self.player2.last_name}"


@dataclass
class Player:
    last_name: str
    first_name: str
    date_of_birth: str
    sex: str
    elo: int
    id: int = field(default_factory=count().__next__, init=False)

    def __str__(self) -> str:
        return (
            f"Nom et prénom : {self.last_name} {self.first_name}, "
            f"Date de naissance : {self.date_of_birth}, "
            f"Elo : {self.elo}"
        )

    def __repr__(self):
        """Representation of the object"""
        return self.last_name

    def serialize(self):
        return self.__dict__


class Round:
    def __init__(self, name, start_date) -> None:
        self.start_date = start_date
        self.name = name
        self.list_of_match = []
        self.end_date = None

    def add_game(self, game):
        self.list_of_match.append(game)

    def format_date(self, date):
        return date.strftime("%d/%m/%y %H:%M")

    def serialize(self) -> dict:
        output = {}
        output["name"] = self.name
        output["start_date"] = self.format_date(self.start_date)
        output["end_date"] = self.format_date(self.end_date)
        list_of_match = []
        [list_of_match.append(match.serialize()) for match in self.list_of_match]
        output["list_of_match"] = list_of_match
        return output


class Tournament:
    def __init__(self, name, location, date, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.description = description
        self.list_of_players = []
        self.list_of_rounds = []
        self.progression = Progress.FIRST_ROUND

        self.NUMBER_OF_ROUNDS = 4
        self.NUMBER_OF_PLAYER = 8

    def serialize(self):
        output = {}
        output["name"] = self.name
        output["location"] = self.location
        output["date"] = self.date
        output["time_control"] = self.time_control
        output["description"] = self.description
        list_of_player = []
        [list_of_player.append(player.serialize()) for player in self.list_of_players]
        output["list_of_player"] = list_of_player
        list_of_round = []
        [list_of_round.append(round.serialize()) for round in self.list_of_rounds]
        output["list_of_round"] = list_of_round
        output["progression"] = self.progression.value
        return output

    def add_round(self, nround):
        self.list_of_rounds.append(nround)

    def add_player_in_list(self, player):
        self.list_of_players.append(player)

    def remove_player_in_list(self, player):
        self.list_of_players.remove(player)

    def __str__(self) -> str:
        return (
            f"Nom du tournoi : {self.name}\n"
            f"Lieu : {self.location}\n"
            f"Date : {self.date}\n"
            f"Contrôle du temps : {self.time_control}\n"
            f"Description : {self.description}"
        )

    def is_full(self) -> bool:
        if len(self.list_of_players) == 8:
            return True
        else:
            return False

    def is_empty(self) -> bool:
        if len(self.list_of_players) == 0:
            return True
        else:
            return False


class Progress(Enum):
    FIRST_ROUND = 0
    SECOND_ROUND = 1
    THIRD_ROUND = 2
    FOURTH_ROUND = 3
    TOURNAMENT_OVER = 4
