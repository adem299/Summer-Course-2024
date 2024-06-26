import random

def roll_dice():
    # Generate a random result for rolling two dice
    return random.randint(1, 6) + random.randint(1, 6)

def get_roll_input():
    while True:
        # Prompt user input
        user_input = input("Type 'roll' to roll the dice: ").strip().lower()
        if user_input == 'roll':
            return roll_dice()
        else:
            print("Invalid input. Type 'roll' to roll the dice.")

def play_craps():
    print("Welcome to the Craps game!")
    
    # First roll
    first_roll = get_roll_input()
    print(f"First roll: {first_roll}")
    
    # Check the result of the first roll
    if first_roll in [7, 11]:
        print("You win!")
        return True
    elif first_roll in [2, 3, 12]:
        print("You lose (craps)!")
        return False
    else:
        # Set the point and continue the game
        point = first_roll
        print(f"Your point is: {point}")
        
        while True:
            current_roll = get_roll_input()
            print(f"Next roll: {current_roll}")
            
            if current_roll == point:
                print("You win by making your point!")
                return True
            elif current_roll == 7:
                print("You lose by rolling a 7!")
                return False

if __name__ == "__main__":
    play_craps()
