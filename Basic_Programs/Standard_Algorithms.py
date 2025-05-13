# Practicing loops etc by coding standard algorithms 

# Input Validation 
while True:
    level = int(input("Enter a level between 1-99: "))  # user input
    if 0 <= level <= 99:
        break   #if condition is true, great. 
    else:
        print("Enter a valid level within the range 1-99: ")    # if not ask again
print("Level: ", level, "accepted!\n")


# Finding maximum
levels = [79, 32, 43, 55, 87, 58]
maxi = levels[0]     # assume first value is max
# i = index, lev = value at position in list
for i, level in enumerate(levels, start=1):   # start from position 1
    if maxi < level:     # compare current max with value at current position
        maxi = level
print("max is ", maxi)

# for max, can also use:
print(max(levels),"\n")


# Finding minimum
mini = levels[0]
for i, level in enumerate(levels, start=1):
    if mini > level:
        mini = level
print("minimum is: ", mini)

# same as max:
print(min(levels),"\n") 


#Searching in a list
characters = ["Monotaro", "Monodam", "Monokid", "Monophanie", "Monosuke"]
choice = str(input("Search for a Mono-cub!"))
for i in characters:
    if choice == i:
        print("Found!")
        break
else:
    print("Not found!")


#Count item in a list
numbers = [1, 3, 4, 5, 2, 6, 7, 3, 2, 1, 1, 5, 5, 6, 8, 2, 9, 9, 9, 9, 9, 9]
count = 0
Countchoice = int(input("Select a number between 1 and 9"))
for i in numbers:
    if Countchoice == i:
        count = count + 1
print("There are ", count, " ", Countchoice, "'s")


# Sum values


# Reverse list


# Sorting lists



    
 
