""" Package: tennis """
from .game import Game


class Set:
    """
    Set model
    """

    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2
        self.games = {self.p_1: 0, self.p_2: 0}  # keep track of winning games
        self.winner = None  # end the game if winner is determined
        self.game = Game(p_1, p_2)

    def game_won_by(self, player):
        """
        Increase a winning game for a player
        If the winner is not found, play a new game
        """
        self.games[player] += 1
        if self.has_winner():
            self.winner = player
        else:
            self.game = Game(self.p_1, self.p_2, tie_break=self.is_tie_break())

    def has_winner(self):
        """
        A player wins a set by winning at least 6 games and
        at least 2 games more than the opponent.
        Or
        if the game is tie break and win by margin of 1 game
        """
        has_winner = False
        if max(self.games.values()) >= 6 and abs(self.games[self.p_1] - self.games[self.p_2]) >= 2:
            has_winner = True
        elif max(self.games.values()) >= 7 and self.games[self.p_1] != self.games[self.p_2]:
            has_winner = True
        return has_winner

    def is_tie_break(self):
        """
        The set is in tie break mode
        if both players win more than 6 games and have same winning games
        """
        return self.games[self.p_1] == self.games[self.p_2] and self.games[self.p_1] >= 6

    def __str__(self):
        output = ""
        if self.winner is None:
            game_output = ', {}'.format(self.game.__str__()) if self.game.is_started() else ""
            output = '{}-{}{}'.format(self.games[self.p_1], self.games[self.p_2], game_output)
        else:
            output = '{} is the winner'.format(self.winner)

        return output
