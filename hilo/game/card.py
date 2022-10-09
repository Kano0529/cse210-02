import random


class Card:

    def __init__(self):
        self.deck = []


# creating a deck of a card with the suit
        counter = 1
        while counter < 5:
            if counter == 1:
                suit = '♥'
            elif counter == 2:
                suit = '♠'
            elif counter == 3:
                suit = '♦'
            elif counter == 4:
                suit = '♣'

            # creating a card looking like '♥1' and append it to the list called deck
            for i in range(1, 14):
                self.deck.append(suit + str(i))

            counter += 1


    def draw_card(self):

        # draw a card randomly from the deck
        self.card = random.choice(self.deck)
        #print(self.card)
        return self.card


if __name__ == '__main__':
    my_deck = Card()
    my_card = my_deck.draw_card()
    print(my_deck.deck)
    print(my_card)
