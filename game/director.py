from game.card import Card


class Director:

    def __init__(self):
        self.is_playing = True
        self.score = 300
        self.guess = ""
        self.new_card = ""
        self.deck = Card()

        # drawing the first card
        self.current_card = self.deck.draw_card()

    def start_game(self):
        # Main loop 
        while self.is_playing and self.score > 0:
            self.get_input()
            self.do_update()
            self.do_outputs()

    def get_input(self):
        print(f"The card is {self.current_card}")
        self.guess = input("Higher or Lower? [h/l]: ")


    def do_update(self):

        def compare(a, b):
            # comparison of two cards
            result = ""
            # slicing the card to get the number
            card1 = int(a[1:])
            card2 = int(b[1:])

            if card1 > card2:
                result = "l"
            elif card1 < card2:
                result = "h"
            else:
                result = "e"

            return result

        # draws the second card
        self.new_card = self.deck.draw_card()
        print(f"Next card was: {self.new_card}")
        comparison_result = compare(self.current_card, self.new_card)

        # calculating the score
        if comparison_result == self.guess:
            self.score += 100
        else:
            self.score -= 75

    def do_outputs(self):
        print(f"Your score is: {self.score}")

        # checks the score for another round
        if self.score > 0:
            play_again = input("Play again? [y/n]: ")

            # input validation
            while (play_again != 'y') and (play_again != 'n'):
                print("Oops! Wrong input. Please try again.")
                play_again = input("Play again? [y/n]: ")

            if play_again == 'y':
                self.is_playing = True
            else:
                self.is_playing = False

        print()
        self.current_card = self.new_card
