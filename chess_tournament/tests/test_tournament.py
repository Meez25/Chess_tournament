from chess_tournament.models.models import Tournament, Player, Round
from datetime import datetime


def test_sorting() -> None:
    tournament = create_test_data()
    output = []
    for player in tournament.list_of_players:
        output.append(player.last_name)

    expected_result = [
        "last_name_1",
        "last_name_2",
        "last_name_3",
        "last_name_4",
        "last_name_5",
        "last_name_6",
        "last_name_7",
        "last_name_8",
    ]
    assert output == expected_result


def create_test_data():
    """Added test data for test purpose"""
    tournament = Tournament("Mulhouse", "", "", "", "")
    test_data = [
        ["last_name_5", "first_name_5", "birthday_5", "sex_5", "500"],
        ["last_name_2", "first_name_2", "birthday_2", "sex_2", "200"],
        ["last_name_3", "first_name_3", "birthday_3", "sex_3", "300"],
        ["last_name_6", "first_name_6", "birthday_6", "sex_6", "600"],
        ["last_name_4", "first_name_4", "birthday_4", "sex_4", "400"],
        ["last_name_8", "first_name_8", "birthday_8", "sex_8", "800"],
        ["last_name_1", "first_name_1", "birthday_1", "sex_1", "100"],
        ["last_name_7", "first_name_7", "birthday_7", "sex_7", "700"],
    ]

    for player in test_data:
        last_name = player[0]
        first_name = player[1]
        birthday = player[2]
        sex = player[3]
        elo = int(player[4])
        player_object: Player = Player(last_name, first_name, birthday, sex, elo)
        tournament.add_player_in_list(player_object)

    first_round = Round("Round 1", datetime.now())
    tournament.add_round(first_round)
    # Add test data
    return tournament


if __name__ == "__main__":
    test_sorting()
