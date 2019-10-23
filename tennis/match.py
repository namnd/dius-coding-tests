from .set import Set

class Match():

  def __init__(self, p1, p2):
    self.set = Set(p1, p2)


  def point_won_by(self, player):
    game_winner = self.set.game.point_won_by(player)
    if game_winner == player:
      self.set.game_won_by(player)


  def __str__(self):
    return self.set.__str__()


  def __repr__(self):
    return '{}{}'.format(type(self), self.__dict__)


  def score(self):
    print(self)
