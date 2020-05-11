import os
from turn import TurnTaker
from calculate_score import Scorer
from scoreboard import ScoreKeeper

game_over = False
print("------------------")
print("Welcome to Yahtzee")
print("------------------")
print()


def screen_clear():
    os.system("clear")
    os.system("cls")


class Player(TurnTaker, Scorer, ScoreKeeper):
    """Initializes a player instance and gives instance of each other class required to play. Expects TurnTaker Score and ScoreKeeper instance."""

    def __init__(self):
        """Initializes the player class to inherit from the TurnTaker Score and ScoreKeeper classes"""
        TurnTaker.__init__(self)
        Scorer.__init__(self, self.roll_result, self.score_board)
        ScoreKeeper.__init__(self)


player1 = Player()
player2 = Player()


def one_player(game_over, player1):
    """Starts the game for one player functionality. Expects game_over and a player1 instance"""
    screen_clear()
    while not game_over:
        print(f"Turn #{player1.turn_count + 1}")
        player1.roll()
        if player1.turn_count == 13:
            print("-------------")
            print("Final Scores!")
            print("-------------")
            print()
            print(
                f"You ended with a score of {player1.score_board.end_of_game_score()}!"
            )
            enter = input("Thanks for playing!")
            if enter == "":
                game_over = True
                exit()


turn_order = 0


def two_player(game_over, turn_order, player1, player2):
    """Starts the game for two player functionality. Expects game_over, turn_order and two player instances"""
    screen_clear()
    while not game_over:
        if turn_order == 0:
            print(f"Turn #{player1.turn_count + 1} for Player 1")
            player1.roll()
        else:
            print(f"Turn #{player2.turn_count + 1} for Player 2")
            player2.roll()
        if player1.turn_count == 13 and player2.turn_count == 13:
            print("-------------")
            print("Final Scores!")
            print("-------------")
            print()
            print(
                f"Player 1's score is: {player1.score_board.end_of_game_score()}\nPlayer 2's score is: {player2.score_board.end_of_game_score()}"
            )
            enter = input("Thanks for playing!")
            if enter == "":
                game_over = True
                exit()
        turn_order += 1
        turn_order = turn_order % 2


def ask_for_players():
    """Asks how many players are playing and expects an answer of 1 or 2 at the moment. Recalls itself when answer isn't an expected option"""
    try:
        player_count = int(input("How many players are there? Options: 1 or 2\n"))
        if player_count == 1:
            one_player(game_over, player1)
        elif player_count == 2:
            two_player(game_over, turn_order, player1, player2)
        else:
            print("Please enter a valid number of players")
            ask_for_players()
    except ValueError:
        print("You've entered an invalid player count")
        ask_for_players()


ask_for_players()
