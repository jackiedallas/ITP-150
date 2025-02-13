"""
basketball_game.py
@author: Jackie Johnson-Dallas
"""
import random


class Player:
    """Represents a player in the basketball game."""

    SHOT_TYPES = {
        0: ('Air Ball', 0),
        1: ('Free Throw', 1),
        2: ('Two Pointer', 2),
        3: ('Three Pointer', 3)
    }

    def __init__(self, name):
        self.name = name
        self.score = 0

    def player_shot(self):
        """Simulates a player taking a shot"""
        shot_result = random.randint(0, 3)
        shot_type, shot_value = self.SHOT_TYPES[shot_result]
        self.score += shot_value
        return shot_type, self.score


class BasketballGame:
    """Represents a basketball game simulation."""

    def __init__(self, player1_name, player2_name):
        """Initialize game with two players."""

        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.counter = 0

    def play_game(self):
        """Represents a game being played."""

        for quarter in range(1, 5):
            print('-' * 28, f'Quarter {quarter}', '-' * 28)
            print(f'{" "}{self.player1.name.title():^30}{self.player2.name.title():^40}')

            # processing for the quarters are below
            print(f'{"Shot #":8s}{"Shot":15s}{"Score":15s}{"Shot":15s}{"Score":15s}')

            # we have 12 minutes in each quarter and 60 seconds in a minute
            # there for 720 seconds. We want each player to take a shot in 30
            # second intervals
            for _ in range(24):
                self.counter += 1
                player1_shot, player1_score = self.player1.player_shot()
                player2_shot, player2_score = self.player2.player_shot()
                print(f'{self.counter:<8d}{player1_shot:<15s}{player1_score:<15d}{player2_shot:<15s}{player2_score:<15d}')

        self.display_winner()

    def display_winner(self):
        """Displays the winner of the game."""
        print("\nFinal Scores:")
        print(f"{self.player1.name.title()}: {self.player1.score}")
        print(f"{self.player2.name.title()}: {self.player2.score}")

        if self.player1.score > self.player2.score:
            print(f"\n{self.player1.name.title()} wins the game!")
        elif self.player1.score < self.player2.score:
            print(f"\n{self.player2.name.title()} wins the game!")
        else:
            print("It's a tie!")


player1_name = input('Please enter the name for Player 1:\n')
player2_name = input('Please enter the name for Player 2:\n')

game = BasketballGame(player1_name, player2_name)
game.play_game()
