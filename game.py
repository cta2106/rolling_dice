from player import Player


class Game:
    def __init__(self):
        self.winner = None
        self.p1 = None
        self.p2 = None

    def play(self):
        self.p1 = Player(stand_threshold=8)
        self.p1.play()

        p2_thresh = 8 if self.p1.n_rolls == 2 else 9
        self.p2 = Player(stand_threshold=p2_thresh)
        self.p2.play()

        if self.p1.last_result.sum() > self.p2.last_result.sum():
            self.winner = "p1"

        elif self.p2.last_result.sum() > self.p1.last_result.sum():
            self.winner = "p2"

        else:
            self.winner = "tie"
