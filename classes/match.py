class Match():

  points = {0:0, 1:15, 2:30, 3: 40}
  scores = {} # keep track of current game scores
  sets = {} # keep track of winning games

  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.sets[self.p1] = 0
    self.sets[self.p2] = 0
    self.__start_new_game()


  def __str__(self):
    scores_str = ""
    if min(self.scores.values()) >= 3:
      if self.scores[self.p1] == self.scores[self.p2]:
        scores_str = ", Deuce"
      else:
        scores_str = ', Advantage {}'.format(self.p1 if self.scores[self.p1] > self.scores[self.p2] else self.p2)
    elif max(self.scores.values()) > 0:
      scores_str = ', {}-{}'.format(self.points[self.scores[self.p1]], self.points[self.scores[self.p2]])


    sets_str = '{}-{}'.format(self.sets[self.p1], self.sets[self.p2])

    return '{}{}'.format(sets_str, scores_str)


  def __repr__(self):
    return '{}{}'.format(type(self),self.__dict__)


  def __start_new_game(self):
    self.scores[self.p1] = 0
    self.scores[self.p2] = 0


  def point_won_by(self, player):
    self.scores[player] = self.scores[player] + 1
    if max(self.scores.values()) >= 4 and abs(self.scores[self.p1] - self.scores[self.p2]) >= 2:
      self.game_won_by(player)


  def game_won_by(self, player):
    self.sets[player] = self.sets[player] + 1
    self.start_new_game()


  def score(self):
    print(self)

