class BowlingGame():
    """docstring for BowlingGame"""
    _score = 0  
    _pending_strikes = 0
    first_roll = True
    score_first_roll = 0

    def roll(self, pins):
        if pins == 10:
            self._pending_strikes += 1
            self.first_roll = True
        elif self.first_roll is False:
            if self._pending_strikes != 0:
                self._score += (self._pending_strikes * 10) * 2 - 10 + (self.score_first_roll + pins) * 2
                self._pending_strikes = 0
            else:
                self._score += pins + self.score_first_roll
            self.first_roll = True
        else:
            self.score_first_roll = pins
            self.first_roll = False
    def score(self):
        return self._score