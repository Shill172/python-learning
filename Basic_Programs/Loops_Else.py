# Loops & Ifs

# For loop
forLoop = ["Yosuke", "Chie", "Yukari"]   # list
print("forLoop: ", forLoop)
for i in forLoop:   # Iterate through list
    print(i)    # Print each element in the list

print("")

# While loop
whileLoop = 0
print("while whileLoop < 3:")
while whileLoop < 3:
    print("whileLoop: ", whileLoop)
    whileLoop = whileLoop+1

print("")

# Else

#Break
print("if num == 3 break")
for num in range(5):    # Loop through each number in that range (0, 1, 2... 5)
    if num == 3:
        break           # End if condition is met
    print(num)

print("")

#Continue & if
print("if num == 3 continue")
for continueTest in range(5):
    if continueTest == 3:
        continue            # Skip if condition met
    print(continueTest)

print("")

## Elif, else
best = ("Makoto", "Marie", "Aigis")
for i in best:
    if i == "Aigis":
        print(i, "is best")
    elif i == "Marie":
        print(i, "is good")
    else:
        print(i, "is okay")

print("")

# Nested loop
print("Netsed loop i range 5, j range 3")
for i in range(5):
    print("i: ", i)
    for j in range(3):
        print("j: ", j)
    print("")

#Looping through dictionary
dictLoop = {"Name": "Strohl", "Level": 25, "Archetype": "Warrior"}
for x in dictLoop:
    print(x, ": ", dictLoop[x])     # x prints key, [x] prints value 

print("")

# Another way of printing key and value: 
for x, y in dictLoop.items():
    print(x, y)

print("")

# Counting differently 
                #start #stop  #increment
for i in range (10,     0,    -2):
    print(i)




