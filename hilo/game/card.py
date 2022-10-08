import random


class Card:
    """A card pulled from a deck.

    The responsability of Card is to randomly draw a card with a value from 1 to 13.

    Attributes:
        value (int): the number of the card.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def draw_card(self):
        """Draws a new card with a random number ranging from 1 to 13.
        
        Args:
            self (Card): An instance of Card.

        Return:
            value (int): the number of the card.
        """
        self.value = random.randint(1, 13)
        return self.value