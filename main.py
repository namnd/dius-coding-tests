from tennis.match import Match

match = Match("player 1", "player 2")
match.point_won_by("player 1")
match.point_won_by("player 2")
# this will return "0-0, 15-15"

match.point_won_by("player 1")
match.point_won_by("player 1")
# this will return "0-0, 40-15"
match.score()

match.point_won_by("player 2")
match.point_won_by("player 2")
# this will return "0-0, Deuce"
match.score()

match.point_won_by("player 1")
# this will return "0-0, Advantage player 1"
match.score()

match.point_won_by("player 1")
# this will return "1-0"
match.score()
