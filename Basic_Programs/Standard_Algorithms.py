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
choice = str(input("Search for a Mono-cub! "))
for i in characters:
    if choice == i:
        print("Found!")
        break
else:
    print("Not found!")


#Count item in a list
numbers = [1, 3, 4, 5, 2, 6, 7, 3, 2, 1, 1, 5, 5, 6, 8, 2, 9, 9, 9, 9, 9, 9]
count = 0
Countchoice = int(input("Select a number between 1 and 9: "))
for i in numbers:
    if Countchoice == i:
        count = count + 1
print("There are ", count, " ", Countchoice, "'s")

print()


# Sum values
sum_ = 0
for i in numbers:
    sum_ = i + sum_
print("The sum of numbers array is: ", sum_)

## Can also do this for sum
print(sum(numbers))


# Reverse list
reverse_this = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp1 = -1
                        # Iterate through half of list
for i, num in enumerate(reverse_this[:len(reverse_this)//2]):
        #Position at: Length of list - index - 1 because of zero index    
    temp1 = reverse_this[len(reverse_this) - i - 1]   #Store current num going to be replaced
    reverse_this[len(reverse_this) - i - 1] = reverse_this[i]
    reverse_this[i] = temp1
print(reverse_this)


# Sorting lists
## Bubble sort
temp_bubble = -1 
bubble_sort = [4, 5, 2, 1, 7, 3, 6]
for i in enumerate(bubble_sort):
    for j, value in enumerate(bubble_sort[:len(bubble_sort)-1]):
        if bubble_sort[j] > bubble_sort[j+1]:
            temp_bubble = bubble_sort[j+1]
            bubble_sort[j+1] = bubble_sort[j]
            bubble_sort[j] = temp_bubble
print(bubble_sort)

## Another method of bubble sort
bubble_sort2 = [4, 5, 2, 1, 7, 3, 6] 
n = len(bubble_sort2)

for i in range(n):
    for j in range(n - 1 - i):
        if bubble_sort2[j] > bubble_sort2[j+1]:
             bubble_sort2[j], bubble_sort2[j+1] = bubble_sort2[j+1], bubble_sort2[j]
print(bubble_sort2)

## Simpler way
sort3 = [4, 5, 2, 1, 7, 3, 6] 
sort3.sort()
print(sort3)
