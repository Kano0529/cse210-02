import random

class Card:
    """Create a card class that will have a random value of 1-13"""

    def __init__(self):
        self.value = 0

    def draw_card(self):
        self.value = random.randint(1, 13)
        return self.value