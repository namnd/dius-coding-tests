""" Unittest Match """
import sys
import unittest

sys.path.append('.')
from tennis.match import Match


class MatchTest(unittest.TestCase):
    """
    Match test cases
    """

    def test_point_won_by_normal(self):
        """
        Normal winning game
        """
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
        """
        Winning game by advantage
        """
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

    def test_point_won_by_sets_6_4(self):
        """
        Normal winning match
        """
        match = Match('p1', 'p2')
        for _ in range(20):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '5-0')

        for _ in range(16):
            match.point_won_by('p2')
        self.assertEqual(match.__str__(), '5-4')

        for _ in range(4):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), 'p1 is the winner')

        match.point_won_by('p1')
        self.assertEqual(match.__str__(), 'p1 is the winner')

    def test_point_won_by_sets_7_5(self):
        """
        Winning match 7-5
        """
        match = Match('p1', 'p2')
        for _ in range(20):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '5-0')

        for _ in range(20):
            match.point_won_by('p2')
        self.assertEqual(match.__str__(), '5-5')

        for _ in range(4):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '6-5')

        for _ in range(4):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), 'p1 is the winner')

    def test_point_won_by_tie_break(self):
        """
        Winning match by tie break point
        """
        match = Match('p1', 'p2')
        for _ in range(20):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '5-0')

        for _ in range(20):
            match.point_won_by('p2')
        self.assertEqual(match.__str__(), '5-5')

        for _ in range(4):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '6-5')

        for _ in range(4):
            match.point_won_by('p2')
        self.assertEqual(match.__str__(), '6-6')

        # Tie break start
        match.point_won_by('p1')
        self.assertEqual(match.__str__(), '6-6, 1-0')
        match.point_won_by('p2')
        self.assertEqual(match.__str__(), '6-6, 1-1')
        match.point_won_by('p2')

        for _ in range(4):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '6-6, 5-2')
        # Match point
        for _ in range(5):
            match.point_won_by('p2')
        self.assertEqual(match.__str__(), 'p2 is the winner')

    def test_point_won_by_tie_break_match_point(self):
        """
        Winning match by tie break point special
        """
        match = Match('p1', 'p2')
        for _ in range(20):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '5-0')

        for _ in range(20):
            match.point_won_by('p2')
        self.assertEqual(match.__str__(), '5-5')

        for _ in range(4):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '6-5')

        for _ in range(4):
            match.point_won_by('p2')
        self.assertEqual(match.__str__(), '6-6')

        # Tie break start
        for _ in range(6):
            match.point_won_by('p1')
        self.assertEqual(match.__str__(), '6-6, 6-0')

        for _ in range(6):
            match.point_won_by('p2')
        self.assertEqual(match.__str__(), '6-6, 6-6')

        match.point_won_by('p1')
        match.point_won_by('p1')
        self.assertEqual(match.__str__(), 'p1 is the winner')


if __name__ == '__main__':
    unittest.main()
