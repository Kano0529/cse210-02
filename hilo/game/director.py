from game.card import Card


class Director:
    """A person who directs the game.
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        is_playing(boolean): whether or not the game is being played.
        score(int): score for the game.
        guess(str): a player's choice of whether the new card being higher or lower.
        current_card(int): a number of the current card(1-13)
        new_card(int): a number of the second card(1-13)
    """

    def __init__(self):
        """Constructor for the Director.
        
        Args:
            self(Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        self.guess = ""
        self.new_card = ""
        self.card = Card()

        # the first card is drawn
        self.current_card = self.card.draw_card()

    def start_game(self):
        """starts the game by running the main game loop.
        
        Args:
            self(Director): an instance of Director
        """

        # Main loop of the game
        while self.is_playing and self.score > 0:
            self.get_input()
            self.do_updates()
            self.do_outputs()

    def get_input(self):
        """prints out the current card to show the user the number.
        The user then gives an input of higher or lower than that card.
        Args:
            self(Director): an instance of Director
        """

        # prints out the current card
        print(f"The card is {self.current_card}")

        # input choice of the user
        self.guess = input("Higher or Lower? [h/l]: ")

        # input validation
        # continue asking for another input until the user gives the right word
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
        valid_card = False
        while not valid_card:
            if self.new_card == self.current_card:
                self.new_card = self.card.draw_card()
            else:
                valid_card = True

        # Determine the answer of the correct guess.
        if self.current_card < self.new_card:
            answer = "h"
        elif self.current_card > self.new_card:
            answer = 'l'

        # If the user input is the same as the correct answer,
        # add 100 to `score`, otherwise, subtract 75.
        if self.guess == answer:
            self.score += 100
        else:
            self.score -= 75

    def do_outputs(self):
        """displays the score of the player, and setting a stage for the next round
        of the game by checking to see if the score is over 0. If it is over 0, it
        asks the player if he/she would like to play again.
        Args:
            self(Director): an instance of Director
        
        """
        print(f"Next card was: {self.new_card}")
        # display the score
        print(f"Your score is: {self.score}")

        # the score is checked to see if it's over 0
        # If it is, the player is asked to play another round.
        if self.score > 0:
            play_again = input("Play again? [y/n]: ")

            # input validation
            while (play_again != 'y') and (play_again != 'n'):
                print("Oops! Wrong input. Please try again.")
                play_again = input("Play again? [y/n]: ")

            # setting the flag for the main routine
            if play_again == 'y':
                self.is_playing = True
            else:
                self.is_playing = False

        print()
        # set the new card to be the current card for the next round.
        self.current_card = self.new_card
        