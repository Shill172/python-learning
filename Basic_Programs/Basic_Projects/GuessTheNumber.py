import random

# Basic guess the number game to practice modular coding, loops, etc.

def welcome():
    print("Welcome to Guess the number!\n")

def validate_input():
    user_input = int(input("Enter a number between 1-100: "))  # user input
    while True:
        if 0 <= user_input <= 100:
            break   #if condition is true, great. 
        else:
            user_input = int(input((f"{user_input} ins't valid. Enter a valid level within the range 1-100: ")))    # if not ask again
    print(f"Input: {user_input} accepted!")
    return user_input

def generate_number():
    random_generated = (random.randint(1, 100))
    return random_generated

def game(user_num, rand_num):
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