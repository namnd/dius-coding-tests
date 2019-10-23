from .game import Game

class Set():

  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.games = {self.p1: 0, self.p2: 0} # keep track of winning games
    self.winner = None # end the game if winner is determined
    self.game = Game(p1, p2)


  def game_won_by(self, player):
    """
    Increase a winning game for a player
    If the winner is not found, play a new game
    """
    self.games[player] += 1
    if self.has_winner():
      self.winner = player
    else:
      self.game = Game(self.p1, self.p2, tie_break = self.is_tie_break())


  def has_winner(self):
    """
    A player wins a set by winning at least 6 games and
    at least 2 games more than the opponent.
    Or
    if the game is tie break and win by margin of 1 game
    """
    if max(self.games.values()) >= 6 and abs(self.games[self.p1] - self.games[self.p2]) >= 2:
      return True
    elif max(self.games.values()) >= 7 and self.games[self.p1] != self.games[self.p2]:
      return True
    else:
      return False


  def is_tie_break(self):
    """
    The set is in tie break mode
    if both players win more than 6 games and have same winning games
    """
    return self.games[self.p1] == self.games[self.p2] and self.games[self.p1] >= 6


  def __str__(self):
    if self.winner is None:
      return '{}-{}{}'.format(self.games[self.p1], self.games[self.p2], self.game.__str__())
    else:
      return '{} is the winner'.format(self.winner)


  def __repr__(self):
    return '{}{}'.format(type(self),self.__dict__)
