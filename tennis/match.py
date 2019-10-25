""" Package: tennis """

from .set import Set


class Match:
    """
    Match model
    """

    def __init__(self, p1, p2):
        self.set = Set(p1, p2)

    def point_won_by(self, player):
        """
        If a point won by a player, update the game scores
        If the game has winner, update the winning games
        """
        game_winner = self.set.game.point_won_by(player)
        if game_winner == player:
            self.set.game_won_by(player)

    def score(self):
        """
        Output current winning games/scores
        """
        print(self)

    def __str__(self):
        return self.set.__str__()

    def __repr__(self):
        return '{}{}'.format(type(self), self.__dict__)
