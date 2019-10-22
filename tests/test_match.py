import unittest, sys
sys.path.append('.')
from classes.match import Match

class MatchTest(unittest.TestCase):

  def test_point_won_by_normal(self):
    match = Match('p1', 'p2')
    match.point_won_by('p1')
    self.assertEqual(match.__str__(), '0-0, 15-0')
    match.point_won_by('p1')
    self.assertEqual(match.__str__(), '0-0, 30-0')
    match.point_won_by('p1')
    self.assertEqual(match.__str__(), '0-0, 40-0')
    match.point_won_by('p2')
    self.assertEqual(match.__str__(), '0-0, 40-15')
    match.point_won_by('p2')
    self.assertEqual(match.__str__(), '0-0, 40-30')
    match.point_won_by('p1')
    self.assertEqual(match.__str__(), '1-0')


  def test_point_won_by_advantage(self):
    match = Match('p1', 'p2')
    match.point_won_by('p1')
    match.point_won_by('p1')
    match.point_won_by('p1')
    match.point_won_by('p2')
    match.point_won_by('p2')
    match.point_won_by('p2')
    self.assertEqual(match.__str__(), '0-0, Deuce')
    match.point_won_by('p1')
    self.assertEqual(match.__str__(), '0-0, Advantage p1')
    match.point_won_by('p2')
    self.assertEqual(match.__str__(), '0-0, Deuce')
    match.point_won_by('p2')
    match.point_won_by('p2')
    self.assertEqual(match.__str__(), '0-1')


if __name__ == '__main__':
  unittest.main()
