import random


class Cell:

    def __init__(self, randomized=True, status=True):
        if randomized:
            self.status = bool(random.getrandbits(1))
        else:
            self.status = status

    def get_status(self):
        return self.status

    def get_short_status(self):
        return str(self.status)[0]

    def set_status(self, new_status):
        self.status = new_status
