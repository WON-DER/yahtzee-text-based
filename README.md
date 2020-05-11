# yahtzee-text-based
Recreating Yahtzee in a text-based fashion. This is my first personal python project and has helped tie together what I've been practicing and reading about relating to OOP, Classes, inheritance as well as importing my own modules.
This project starts from the yahtzee.py file and first asks the user how many players are there (1 or 2) at the moment.
A player's turn consists of 3 rolls and the chance to keep any number of die into the following roll. 
For keeping die between rolls, the game takes player input (currently as space separated values of indexes 1-5). 
After the 3rd roll, the game takes player input for which category to score the roll under. 
If the category is already scored, it prompts for an unused category. 
The currently scored categories are shown during this time and the available choices for those that remain as well. 
After players are given turns for choosing each category, the total score including bonuses are calculated and displayed before the end of the game.
