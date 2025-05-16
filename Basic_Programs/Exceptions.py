# Practicing Exceptions

def zero_division():    # Cannot divide by zero
    try:
        print("Testing 5 / 0:")
        x = 5
        y = 0
        print(x / y)
    except ZeroDivisionError:
        print("It's impossible to divide by zero!!!\n")

def type_error():       # Used when an operatiohn is performed on an incorrect object type,
    try:
        print("Testing '5' + 10:")
        x = '5' + 10
        print(x)
    except TypeError:
        print("Cannot add a string to an int!!!\n")

def value_error():      # Used when a functions receives a value of wrong type
    try:
        print("Testing x = int('string in here')")
        x = int('string in here')
        print(x)
    except ValueError:
        print("You have an int a string and that cant be converted to a number!!!\n")

def index_error():      # Used when index accessed is out of range 
    try:
        print("Testing print(array[5]) in array of size 3:")
        array = [0, 1, 2] 
        print(array[5])
    except IndexError:
        print("You cant access a index you dont have!!!")

# Will add filenotfound error when I do file stuff





if __name__ == "__main__":
    zero_division()
    type_error()
    value_error()
    index_error()
