import random 

WIZARD = {"strenght": 0, "dexterity": 2,"intelligence": 2, "health": 1}
BARBARIAN = {"strenght": 2, "dexterity": 1,"intelligence": 0, "health": 2}

def play_game(role):
    if role == "wizard":
        player = WIZARD
    else:
        player = BARBARIAN
    print("You have chosen the role of a {}. ".format(role.capitalize()))
    challenges = [("strength", "Defend against a dragon"),
                  ("dexterity", "Escape a maze"),
                  ("intelligence", "Solve a riddle")]
    for attribute, challenge in challenges:
        print("Challenge: {}".format(challenge))
        print("Roll the dice to start the challenge.")
        
        input("Press enter to roll...")
        dice_roll = random.randint(2, 12)
        print("You rolled a {}.".format(dice_roll))
        result = determine_result(dice_roll, player[attribute])
        print("Result: {}".format(result))
        
        if result == "Critical Loss":
            player[attribute] -= 1
        elif result == "Critical Win":
            player[attribute] += 1
    game_over(sum(player.values()) >= 6)
    
def determine_result(dice_roll, attribute_value):
    if dice_roll <= 3 + attribute_value:
        return "Critical Loss"
    elif dice_roll <= 7 + attribute_value:
        return "Loss"
    elif dice_roll <= 10 + attribute_value:
        return "Win"
    else:
        return "Critical Win"
    
def game_over(is_win):
    if is_win:
        print("Congratulations! You have won the game. ")
    else:
        print("Sorry, Unfortunately you have lost the game.")