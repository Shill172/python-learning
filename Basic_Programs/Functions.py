# Functions

def say_hello():
    print("Hello!")

def say_name(name, surname):
    print(f"First name: {name}\nSurname: {surname}")

def add(x, y):
    z = x + y
    return z

if __name__ == "__main__":
    say_hello()
    say_hello()

    say_name("Joker", "Persona")
    say_name("Persona", "Joker")

    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(add(num1, num2))



