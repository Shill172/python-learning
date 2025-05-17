import random

# Basic guess the number game to practice modular coding, loops, etc.

def welcome():
    print("Welcome to Guess the number!\n")     

def validate_input():
    while True:     # Loop until a valid number is chosen
        try:
            user_input = int(input("Enter a number between 1-100: "))
            if 0 <= user_input <= 100:
                print(f"Input: {user_input} accepted!")
                return user_input       # When inputted number is within range, return that number
            else:
                print(f"{user_input} isn't valid. Enter a number between 1-100.")
        except ValueError:      # Throw a value error when not an int
            print("You did not input an int!")


def generate_number():
    random_generated = (random.randint(1, 100))
    return random_generated     # Get random number

def game(user_num, rand_num):   # Main logic
    while True:
        if user_num > rand_num:
            print("Too high!")
            user_num = validate_input()
        elif rand_num > user_num:
            print("Too low!")
            user_num = validate_input()
        else:
            print(f"Correct! The random number was {rand_num}")
            break
    
if __name__ == "__main__":
    welcome()
    user_input = validate_input()
    rand_num = generate_number()
    game(user_input, rand_num)