import Game

""" Implements the interaction with the user and starts the game """

def main():
    print("Welcome to Adventure Quest!")
    print("In this game, You will choose a role and face three challeges in the game of quest")
    print("Choose your role: Wizard or Barbarian")
    
    role = input().lower()
    if role not in ["wizard", "barbarian"]:
        print("Invaild role. Choose either Wizard or Barbarian.")
        return
    Game.play_game(role)
    
if __name__ == "__main__":
    main()