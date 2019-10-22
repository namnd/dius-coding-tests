from .game import Game

class Set():

  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.games = {self.p1: 0, self.p2: 0} # keep track of winning games
    self.tie_break = False # flag for tie break set as it has different rule
    self.winner = None # end the game if winner is determined
    self.game = Game(p1, p2)


  def game_won_by(self, player):
    self.games[player] = self.games[player] + 1

    if max(self.games.values()) >= 6:
      if self.tie_break and self.games[self.p1] != self.games[self.p2]:
        self.winner = player
      elif abs(self.games[self.p1] - self.games[self.p2]) >= 2:
        self.winner = player
      elif self.games[self.p1] == self.games[self.p2]:
        self.tie_break = True

    if self.winner is None:
      self.game = Game(self.p1, self.p2, tie_break = self.tie_break)


  def __str__(self):
    if self.winner is None:
      return '{}-{}{}'.format(self.games[self.p1], self.games[self.p2], self.game.__str__())
    else:
      return '{} is the winner'.format(self.winner)


  def __repr__(self):
    return '{}{}'.format(type(self),self.__dict__)
