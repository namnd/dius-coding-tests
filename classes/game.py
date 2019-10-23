class Game():

  def __init__(self, p1, p2, tie_break = False):
    self.p1 = p1
    self.p2 = p2
    self.scores = {self.p1: 0, self.p2: 0} # keep track of current game scores
    self.tie_break = tie_break # flag for tie break game as it has different rule


  def point_won_by(self, player):
    """
    Increase a point for a player
    Return the winner (the player just won the point) of the game if found
    """
    self.scores[player] += 1
    if self.has_winner():
      return player


  def has_winner(self):
    """
    A game is won by the first player to have won at least 4 points in total
    and at least 2 points more than the opponent.
    However, for tie-break game, it continues until one player wins 7 points
    by a margin of 2 or more points
    """
    threshold = 7 if self.tie_break else 4
    return max(self.scores.values()) >= threshold and abs(self.scores[self.p1] - self.scores[self.p2]) >= 2


  def is_deuce(self):
    """
    If at least 3 points have been scored by each player,
    and the scores are equal, the score is "deuce".
    """
    return self.scores[self.p1] == self.scores[self.p2] and self.scores[self.p1] >= 3


  def has_advantage(self):
    """
    If at least 3 points have been scored by each side
    and a player has one more point than his opponent,
    the score of the game is "advantage" for the player in the lead.
    """
    if min(self.scores.values()) >= 3:
      return self.p1 if self.scores[self.p1] > self.scores[self.p2] else self.p2


  def is_started(self):
    """
    Check if the game has started
    """
    return max(self.scores.values()) > 0


  def __str__(self):
    if self.is_started():
      if self.tie_break:
        return ', {}-{}'.format(self.scores[self.p1], self.scores[self.p2])
      elif self.is_deuce():
        return ', Deuce'
      else:
        advantage_player = self.has_advantage()
        if advantage_player is not None:
          return ', Advantage {}'.format(advantage_player)
        else:
          points = {0:0, 1:15, 2:30, 3: 40}
          return ', {}-{}'.format(points[self.scores[self.p1]], points[self.scores[self.p2]])

    return ""


  def __repr__(self):
    return '{}{}'.format(type(self),self.__dict__)
