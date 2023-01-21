from random import randrange
from collections import namedtuple
#==============================================================================
""" Team photo day - 1. - [EPI:13.10]. """


class Team:
    Player = namedtuple('Player', ('height'))

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]

    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0, team1):
        t1 = sorted(team0._players)
        t2 = sorted(team1._players)
        return all(a < b for a, b in zip(t1, t1))


# NOT IMPLEMENTED PROPERLY !!
def _test_team():
    for _ in range(1000):
        T1_height = [randrange(60, 70) for _ in range(11)]
        T2_height = [randrange(70, 80) for _ in range(11)]
        team1 = Team(T1_height)
        team2 = Team(T2_height)
        is_possible = Team.valid_placement_exists(team1, team2)
        if is_possible:
            print(sorted(T1_height), sorted(T2_height))
        # print("team1 can be placed in front of team2: ", is_possible)


def main():
    pass


if __name__ == '__main__':
    main()
