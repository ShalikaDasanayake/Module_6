# The program where the dice roll function takes the number of sides as a parameter. 

import random

def roll_dice(sides):
    # Returns a random number between 1 and 6. like rolling a dice
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    max_number = sides
    result = 0
    while result != max_number:
        result = roll_dice(sides)
        print("Rolled:", result)

if __name__ == "__main__":
    main()