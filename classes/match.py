class Match():

  points = {0:0, 1:15, 2:30, 3: 40}
  scores = {} # keep track of current game scores
  sets = {} # keep track of winning games
  tie_break = False
  winner = None

  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.sets[self.p1] = 0
    self.sets[self.p2] = 0
    self.__start_new_game()


  def __start_new_game(self):
    self.scores[self.p1] = 0
    self.scores[self.p2] = 0


  def point_won_by(self, player):
    self.scores[player] = self.scores[player] + 1
    # If tie break, player need to reach 7 points
    threshold = 7 if self.tie_break else 4
    if max(self.scores.values()) >= threshold and abs(self.scores[self.p1] - self.scores[self.p2]) >= 2:
      self.game_won_by(player)


  def game_won_by(self, player):
    self.sets[player] = self.sets[player] + 1
    if max(self.sets.values()) >= 6:
      if self.tie_break and self.sets[self.p1] != self.sets[self.p2]:
        self.winner = player
      elif abs(self.sets[self.p1] - self.sets[self.p2]) >= 2:
        self.winner = player
      elif self.sets[self.p1] == self.sets[self.p2]:
        self.tie_break = True


    self.__start_new_game()


  def __str__(self):
    scores_str = ""
    if self.tie_break:
      if max(self.scores.values()) > 0:
        scores_str = ', {}-{}'.format(self.scores[self.p1], self.scores[self.p2])
    else:
      if min(self.scores.values()) >= 3:
        if self.scores[self.p1] == self.scores[self.p2]:
          scores_str = ", Deuce"
        else:
          scores_str = ', Advantage {}'.format(self.p1 if self.scores[self.p1] > self.scores[self.p2] else self.p2)
      elif max(self.scores.values()) > 0:
        scores_str = ', {}-{}'.format(self.points[self.scores[self.p1]], self.points[self.scores[self.p2]])


    sets_str = ""
    if self.winner is None:
      sets_str = '{}-{}'.format(self.sets[self.p1], self.sets[self.p2])
    else:
      sets_str = '{} is the winner'.format(self.winner)

    return '{}{}'.format(sets_str, scores_str)


  def __repr__(self):
    return '{}{}'.format(type(self),self.__dict__)


  def score(self):
    print(self)

