import random


class Card:

    def __init__(self):
        self.card = ''

    def draw_card(self):
        self.card = random.randint(1, 13)

        return self.card
