import random

# ... Definitions
def choose_dice(dice_type):
    """Takes user input and selects which dice type they want to roll with.
    """
    dice_type = []
    if dice_type = 1:
        dice = random.randint(1,2)
        dice_type.append(dice)

    elif dice_type = 2:
        dice = random.randint(1,4)
        dice_type.append(dice)
    elif dice_type = 3:
        dice = random.randint(1,6)
        dice_type.append(dice)
    elif dice_type = 4:
        dice = random.randint(1,8)
        dice_type.append(dice)
    elif dice_type = 5:
        dice = random.randint(1,10)
        dice_type.append(dice)
    elif dice_type = 6:
        dice = random.randint(1,12)
        dice_type.append(dice)
    elif dice_type = 7:
        dice = random.randint(1,20)
        dice_type.append(dice)
    elif dice_type = 8:
        dice = random.randint(1,100)
        dice_type.append(dice)
def parse_dice_input(dice_input_string):
    """Return `dice_input_string` as an integer between 1 and 8.
    Check if `dice_input_string` is an integer number between 1 and 8. If so, return an integer with the same value. Otherwise, tell the user to enter a valid number and quit the program.
    """
    if dice_input_string.strip() in {"1,", "2", "3", "4", "5", "6", "7", "8"}
        return int(dice_input_string)
    else:
        print("Please enter a number from 1 to 8.")
        raise SystemExit(1)
def parse_roll_input(roll_input_string):
    """return  `roll_input_string` as an intger between 1 and 6
    
    Check if `roll_input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell the user to enter a valid number and quit the program.
    """
    if roll_input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(roll_input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)
        """ Input a fallback to ask the question again. So to avoid the user having to redo the entire process."""
def roll_dice(num_dice):
    """Call which dice that user wants to use.

    Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between 1 and the chose dice type, inlusive.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = dice
        roll_results.append(roll)
    return roll_results
        
# ~~~ Main code block ~~~
# 1. Get and validate user's input for type of dice
dice_type_input = input("Which dice do you want to roll? [D2, D4, D6, D8, D10, D12, D20, D100] ")
dice_type = parse_dice_input(dice_type_input)

# 2. Get and Validate user's input for number of dice
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_roll_input(num_dice)

print(roll_results)