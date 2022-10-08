from game.card import Card


class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): whether or not the game is being played.
        score (int): score for the game.
        guess (str): a player's choice of whether the new card being higher or lower.
        current_card (int): a number of the current card (1-13).
        new_card (int): a number of the second card (1-13).
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self(Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        self.guess = ''
        self.new_card = ''
        self.card = Card()
        self.current_card = self.card.draw_card()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing and self.score > 0:
            self.get_input()
            self.do_updates()
            self.do_outputs()

    def get_input(self):
        """Prints out the current card and asks the player to guess
        whether the next card has a higher or lower number than the current card.
        
        Args:
            self (Director): an instance of Director
        """
        print(f"The card is {self.current_card}")
        self.guess = input("Higher or Lower? [h/l]: ")

        # Input validation.
        # Continue asking for another input until the user gives the right word.
        while (self.guess != 'h') and (self.guess != 'l'):
            print("Oops! Wrong input. Please try again.")
            self.guess = input("Higher or Lower? [h/l]: ")

    def do_updates(self):
        """Draws a new card and determines if the player guessed correctly on
        whether the card is higher or lower in number. Add 100 to `self.score`
        if guessed correctly. Substract 75 if guessed incorrectly.

        Args:
            self(Director): an instance of Director
        """
        # Draw a new card.
        self.new_card = self.card.draw_card()
        # If `new_card` == `current_card`, 
        # draw a card again until `new_card` != `current_card`.
        while self.new_card == self.current_card:
            self.new_card = self.card.draw_card()

        # Determine the answer of the correct guess.
        if self.current_card < self.new_card:
            answer = "h"
        elif self.current_card > self.new_card:
            answer = 'l'

        # If the user input is the same as the correct answer,
        # add 100 to `score`, otherwise subtract 75.
        if self.guess == answer:
            self.score += 100
        else:
            self.score -= 75

    def do_outputs(self):
        """Displays the score of the player and continues the game if the score
        is higher than zero.

        Args:
            self(Director): an instance of Director
        
        """
        print(f"Next card was: {self.new_card}")
        print(f"Your score is: {self.score}")

        # The score is checked to see if it's over 0.
        # If it is, the player is asked whether to continue or not.
        if self.score > 0:
            play_again = input("Play again? [y/n]: ")

            # Input validation.
            while (play_again != 'y') and (play_again != 'n'):
                print("Oops! Wrong input. Please try again.")
                play_again = input("Play again? [y/n]: ")

            # Setting the flag for the main routine.
            if play_again == 'y':
                self.is_playing = True
            else:
                self.is_playing = False
        print()

        # Set the new card to be the current card for the next round.
        self.current_card = self.new_card  