import numpy as np


class Player:
    def __init__(self, stand_threshold):
        self.last_result = [0, 0]
        self.stand_threshold = stand_threshold
        self.n_rolls = 0

    def play(self):
        while (sum(self.last_result) < self.stand_threshold) and (self.n_rolls < 2):
            self.__roll_dice()
            self.n_rolls += 1

    def __roll_dice(self):
        self.last_result = np.random.randint(1, 7, 2)
