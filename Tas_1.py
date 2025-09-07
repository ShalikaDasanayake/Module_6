# The function that returns a random dice roll between 1 and 6.

import random

def roll_dice():
    # Returns a random number between 1 and 6. like rolling a dice
    return random.randint(1, 6)

def main():
    result = 0
    while result !=6:
        result = roll_dice()
        print("Rolled:", result)

if __name__ == "__main__":
    main()