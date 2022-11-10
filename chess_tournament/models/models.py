class Match:
    def __init__(self, player1, player2) -> None:
        self.score1 = 0
        self.score2 = 0
        self.player1 = player1
        self.player2 = player2
        
    def set_score_player_1(self, new_score):
        self.score1 = new_score

    def set_score_player_2(self, new_score):
        self.score2 = new_score

    def get_result(self):
        return {[self.player1, self.score1],[self.player2, self.score2]}

    def show_players(self) -> str:
        return([self.player1, self.player2])

    def get_players(self):
        return([self.player1, self.player2])

    def add_score_to_players(self):
        self.player1.set_score(self.player1.get_score() + self.score1)
        self.player2.set_score(self.player2.get_score() + self.score2)

    def __str__(self):
        return f"{self.player1.last_name} contre {self.player2.last_name}"

    def __repr__(self):
        return f"{self.player1.last_name} contre {self.player2.last_name}"

"""
pair of player
result


get score()
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant deux éléments : 
une référence à une instance de joueur et un score. Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour. 

"""


class Player:
    def __init__(self, last_name, first_name, date_of_birth, sex, elo) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.elo = elo
        self.score = 0
        self.already_played = []

    
    def __str__(self) -> str:
        return (
            f"Nom de famille : {self.last_name}\n"
            f"Prénom : {self.first_name}\n"
            f"Date de naissance : {self.date_of_birth}\n"
            f"Sexe : {self.sex}\n"
            f"Elo : {self.elo}\n"
            f"Score : {self.score}\n"
            f"Already played : {self.already_played}"
        )

    def __repr__(self):
        return self.last_name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def add_already_played(self, player):
        self.already_played.append(player)

    def get_already_played(self):
        return self.already_played

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name



class Round:
    def __init__(self, name, start_date) -> None:
        self.start_date = start_date
        self.name = name
        self.list_of_match = []

    def add_game(self, game):
        self.list_of_match.append(game)

    def get_list_of_match(self):
        return self.list_of_match


"""
List of match
Name of round (Round 1, Round 2, etc)
Date and hour of start (automatic at creation of round)
Date and hour of end (automatic at round finished)
"""


class Tournament:
    def __init__(self, name, location, date, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.description = description
        self.list_of_players = []
        self.list_of_rounds = []

        self.NUMBER_OF_ROUNDS = 4
        self.NUMBER_OF_PLAYER = 8

    def add_round(self, round):
        self.list_of_rounds.append(round)

    def get_list_of_rounds(self):
        return self.list_of_rounds

    def get_list_of_player(self):
        return self.list_of_players

    def add_player_in_list(self, player):
        self.list_of_players.append(player)

    """
    @classmethod
    def get(cls):
        name = input("Nom du tournoi ? : ")
        location = input("Lieu ? : ")
        date = input("Date ? : ")
        time_control = input("Contrôle du temps ? : ")
        description = input("Description ? : ")
        return cls(name, location, date, time_control, description)
    """

    def __str__(self) -> str:
        return (
            f"Nom du tournoi : {self.name}\n"
            f"Lieu : {self.location}\n"
            f"Date : {self.date}\n"
            f"Contrôle du temps : {self.time_control}\n"
            f"Description : {self.description}"
        )

    """
    def get_list_of_players(self):
        for i in range(self.NUMBER_OF_PLAYER):
            self.list_of_players.append(Player.get())
    """
