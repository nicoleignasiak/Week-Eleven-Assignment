# Nicole Ignasiak
# Dr. Neumann
# CIS 125
# Week Eleven
# Nov 18, 2015

from BowlingGame import Game

# open file
scores = open("testscores.txt", "r")

# loop through scores
for line in scores:
# strip scores to take out punctuation
    line = line.strip()
# split scores into a list
    listScore = line.split(",")
# makes the scores integers
    listScore = [int(i) for i in listScore]
# makes the final score the last value on list
    finalScore = listScore.pop()
    game = Game()
# loops through listScore
    for roll in listScore:
        game.roll(roll)
# gets the score
    score = game.score()
    print("Calculated score is {}, and the score in the file is {}".format(score,  finalScore))
# sees if scores are the same
    if score == finalScore:
        print("The score was right!")
# if the scores aren't the same
    else:
        print("The score was wrong and should be", score)

# close file
scores.close()