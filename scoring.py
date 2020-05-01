class Score:
    """Inherits roll result from turn and defines functions for detecting and scoring roll results. Contains algorithms for each scoring category
    to either award points or grant 0 points if a roll does not meet the requirements"""

    def __init__(self, roll_result, board):
        """Takes the roll result from Yahtzee.py and uses it for scoring and defines dicts for filtering and applying singleScores and 
        for detecting transferring user category selection into the callables list of functions. Also sets up the board to be used as a class parameter"""
        self.roll_result = roll_result
        self.singles = {
            "ones": 1,
            "twos": 2,
            "threes": 3,
            "fours": 4,
            "fives": 5,
            "sixes": 6,
        }
        self.callables = {
            "ones": self.singlesScore,
            "twos": self.singlesScore,
            "threes": self.singlesScore,
            "fours": self.singlesScore,
            "fives": self.singlesScore,
            "sixes": self.singlesScore,
            "three of a kind": self.toak,
            "four of a kind": self.foak,
            "full house": self.fullH,
            "small straight": self.smallStrt,
            "large straight": self.largeStrt,
            "yahtzee": self.yathzee,
            "chance": self.chance,
        }
        self.board = board

    def scoreRoll(self):
        """Displays the currently attained scores. Then asks user for which category to score roll
        and gives lowercase selection to score filter"""
        print("It's time to score your roll!")
        self.board.display_active_cats()
        self.board.display_available_cats()
        self.selection = input("For which category would you like to score?\n").lower()
        self.scoreFilter(self.selection)

    def scoreFilter(self, selection):
        """Maps the user selection to the dictionary key to feed value of class functions to be called for scoring eligibility"""
        if (self.selection in self.callables.keys()) and self.board.scoresTaken[
            f"{self.selection}"
        ] == None:
            self.board.scoresTaken[f"{self.selection}"] = self.callables[
                f"{self.selection}"
            ]()
        else:
            print("This selection has been taken already")
            self.scoreRoll()

    def singlesScore(self):
        """Parses singles dict then adds sum of the singles roll result to the scoring dictionary"""
        if self.selection in self.singles:
            score = sum(
                i for i in self.roll_result if i == self.singles[self.selection]
            )
            return score
        else:
            score = 0
            return score
        return score

    def toak(self):
        """Algorithm to detect at least three dice the same"""
        self.roll_result.sort()
        if (
            self.roll_result[0] == self.roll_result[2]
            or self.roll_result[1] == self.roll_result[3]
            or self.roll_result[2] == self.roll_result[4]
        ):
            score = sum(i for i in self.roll_result)
            return score
        else:
            score = 0
            return score

    def foak(self):
        """Algorithm to detect at least four dice the same"""
        self.roll_result.sort()
        if (
            self.roll_result[0] == self.roll_result[3]
            or self.roll_result[1] == self.roll_result[4]
        ):
            score = sum(i for i in self.roll_result)
            return score
        else:
            score = 0
            return score

    def fullH(self):
        """Algorithm to detect three of one number and two of another"""
        self.roll_result.sort()
        if len(set(self.roll_result)) != 2:
            score = 0
            return score
        elif (
            self.roll_result[0] != self.roll_result[3]
            or self.roll_result[1] != self.roll_result[4]
        ):
            score = 25
            return score

    def smallStrt(self):
        """Algorithm to detect four sequential dice"""
        self.roll_result.sort()
        if len(set(self.roll_result)) < 4:
            score = 0
            return score
        elif (
            (len(set([1, 2, 3, 4]).intersection(set(self.roll_result))) == 4)
            or (len(set([2, 3, 4, 5]).intersection(set(self.roll_result))) == 4)
            or (len(set([3, 4, 5, 6]).intersection(set(self.roll_result))) == 4)
        ):
            score = 30
            return score
        else:
            score = 0
            return score

    def largeStrt(self):
        """Algorithm to detect five sequential dice"""
        self.roll_result.sort()
        if len(set(self.roll_result)) < 5:
            score = 0
            return score
        elif (len(set([1, 2, 3, 4, 5]).intersection(set(self.roll_result))) == 5) or (
            len(set([2, 3, 4, 5, 6]).intersection(set(self.roll_result))) == 5
        ):
            score = 40
            return score
        else:
            score = 0
            return score

    def yathzee(self):
        """Algorithm to detect that all five dice are the same"""
        if len(set(self.roll_result)) == 1:
            if (
                self.board.scoresTaken["yahtzee"] != None
                and self.board.scoresTaken["yahtzee"] != 0
            ):
                self.board.scoresTaken["yahtzee bonus"] += 100
                return
            else:
                score = 50
                return score
        else:
            score = 0
            return score

    def chance(self):
        """Algorithm to compute any combination of roll result"""
        score = sum(self.roll_result)
        return score
