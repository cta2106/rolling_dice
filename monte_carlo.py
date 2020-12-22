from game import Game


class MonteCarlo:
    def __init__(self, n_sim):
        self.game = None
        self.n_sim = n_sim
        self.p1_win = 0
        self.p2_win = 0

    def run_simulation(self):
        self.game = Game()

        for _ in range(self.n_sim):
            self.game.play()

            if self.game.winner == "p1":
                self.p1_win += 1

            elif self.game.winner == "p2":
                self.p2_win += 1
