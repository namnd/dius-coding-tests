class Game():

  def __init__(self, p1, p2, tie_break = False):
    self.p1 = p1
    self.p2 = p2
    self.scores = {self.p1: 0, self.p2: 0} # keep track of current game scores
    self.tie_break = tie_break # flag for tie break game as it has different rule


  def point_won_by(self, player):
    self.scores[player] = self.scores[player] + 1
    if self.has_winner():
      return player


  def has_winner(self):
    threshold = 7 if self.tie_break else 4
    return max(self.scores.values()) >= threshold and abs(self.scores[self.p1] - self.scores[self.p2]) >= 2


  def __str__(self):
    if max(self.scores.values()) > 0:
      if self.tie_break:
        return ', {}-{}'.format(self.scores[self.p1], self.scores[self.p2])
      else:
        if min(self.scores.values()) >= 3:
          if self.scores[self.p1] == self.scores[self.p2]:
            return ', Deuce'
          else:
            return ', Advantage {}'.format(self.p1 if self.scores[self.p1] > self.scores[self.p2] else self.p2)
        else:
          points = {0:0, 1:15, 2:30, 3: 40}
          return ', {}-{}'.format(points[self.scores[self.p1]], points[self.scores[self.p2]])

    return ""


  def __repr__(self):
    return '{}{}'.format(type(self),self.__dict__)
