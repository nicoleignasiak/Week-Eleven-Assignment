# Basic Structure for a Random Walk simulation
# Nicole Ignasiak
'''

You flip a coin.
If it comes up heads, you take a step forward;
tails means to take a step backward.
Repeat this n times.
Calculate distance from start

Repeat this process a large number of times.
Calculate and print the average for a given value of n
Start with 100 to 1000, step 10
'''

import random

# Define ranges here
startRange = 0
endRange = 100
stepRange = 10

def main():
    printHeader()
    for n in range(startRange,endRange,stepRange):
        averageDistance = getRandomWalk(n)
        print("For {} steps, the average distance is: {}".format(n,averageDistance))


def printHeader():
    print("Some informative text")

def getRandomWalk(steps):
    # Calculate a random walk of given steps
    distance = 0
# loops thorugh number of steps
    for i in range(steps):
# randomly chooses heads or tails
        flip = random.randint(1,2)
        if flip == 1:
# steps forward
            distance += 1
        else:
# steps backwards
            distance -= 1

    return distance # replace with actual average

if __name__ == "__main__":
    main()