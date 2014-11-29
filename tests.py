import unittest
from BowlingGame import BowlingGame

# Given_When_Then

class BowlingTest(unittest.TestCase):
    """Tests pour le jeu Bowling"""
    def setUp(self):
        pass

    def new_game(self):
        return BowlingGame()

    def test_GivenFirstRollWhen0PinsThenScore0(self):
        bg = self.new_game()
        bg.roll(0)
        self.assertEqual(bg.score(), 0)

    def test_GivenRollingWhenDropsNotNilThenScoreChanges(self):
        bg = self.new_game()
        before = bg.score()
        bg.roll(1)
        bg.roll(2)
        self.assertFalse(bg.score() == before, "The score did not change even though some pins dropped! (score incremented by " + str(bg.score() - before) + ")")

    def test_GivenRollWhen2KnocksDownThenScoreIncrementBy2(self):
        bg = self.new_game()
        before = bg.score()
        bg.roll(2)
        bg.roll(0)
        print "YOLO" + str(bg.score() - before)
        self.assertFalse(bg.score() != before + 2, "The score has not been incremented by two!")

    def test_GiveneRollWhen2KnocksDownThenScoreIncrementBy2(self):
        bg = self.new_game()
        before = bg.score()
        bg.roll(10)
        bg.roll(2)
        bg.roll(0)
        self.assertEqual(bg.score(), before + 14, "The score has not been incremented by 14! (score incremented by " + str(bg.score() - before) + ")")

    def test_GivenRollWhenTwoConsecutiveStrikesThenScoreIncBy30AndCurrentKnocks(self):
        bg = self.new_game()
        before = bg.score()
        bg.roll(10)        
        bg.roll(10)        
        bg.roll(2)
        bg.roll(0)
        inc = 34
        self.assertEqual(bg.score(), before + inc, "The score has not been incremented by " + str(inc) + "! (score incremented by " + str(bg.score() - before) + ")")
    
    def test_GivenRollWhenTwoConsecutiveStrikesThenScoreIncBy30AndCurrentKnocks(self):
        bg = self.new_game()
        before = bg.score()
        bg.roll(10)        
        bg.roll(2)        
        bg.roll(2)
        inc = 18
        self.assertEqual(bg.score(), before + inc, "The score has not been incremented by " + str(inc) + "! (score incremented by " + str(bg.score() - before) + ")")
        


if __name__ == '__main__':
    unittest.main()