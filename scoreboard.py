class ScoreBoard:
    """This is the class for keeping track of the active scores and the formulation of what the categories are.
    It keeps the algorithms for the upper score bonus, end of game score and displaying the actively entered categories during a given turn"""

    def __init__(self):
        """Initializes the ScoreBoard class to have a dictionary for each scoring category defaulted to None as well as the upperScores tuple"""
        self.scoresTaken = {
            "ones": None,
            "twos": None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
            "three of a kind": None,
            "four of a kind": None,
            "full house": None,
            "small straight": None,
            "large straight": None,
            "yahtzee": None,
            "chance": None,
            "yahtzee bonus": None,
            "upper bonus": None,
        }
        self.upperScores = "ones", "twos", "threes", "fours", "fives", "sixes"

    def bonusTime(self):
        """Computes and updates the dict with the bonus if any and returns 35 or 0 points to the upper bonus dict value"""
        if sum(v for k, v in self.scoresTaken.items() if k in self.upperScores) >= 63:
            self.scoresTaken["upper bonus"] = 35
        else:
            self.scoresTaken["upper bonus"] = 0
        if self.scoresTaken["yahtzee bonus"] == None:
            self.scoresTaken["yahtzee bonus"] = 0

    def end_of_game_score(self):
        """Computes the end of game score including bonus for each player instance call"""
        self.bonusTime()
        self.totalscore = sum(v for k, v in self.scoresTaken.items())
        return self.totalscore

    def display_active_cats(self):
        """Calculates the actively non None scores for each player instance and 
        is called by turn to display when needing to choose a category for scoring"""
        print("You've scored in these categories so far:")
        for k, v in self.scoresTaken.items():
            if v != None:
                print(k.title() + ": " + str(v))
    
    def display_available_cats(self):
        """Computes the remaining available categories to select from and 
        displays them after already scored categories"""
        print("\nChoose from these remaining categories: ")
        for k, v in self.scoresTaken.items():
            if v is None and k not in ["yahtzee bonus", "upper bonus"]:
                print(k.title())
        print()