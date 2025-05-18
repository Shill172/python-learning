import time

# Using built in methods

def string_methods():
    string_text = "  The voice of the wind and droplets of light flow over you as you doze     "
    print(f"Original string: \n{string_text}")

    # Split on it's own splits the string by " ", making each word an item in a list
    print(string_text.split())

    # Strip cuts of the end where there is nothing
    print(string_text.strip())

    # Find finds what char the word is at in the string
    print(string_text.find("doze"))

    # Replcaes x with y. Case sensitive.
    print(string_text.replace("the", "thy"))

    # Slicing prints what posisiton boundaries you set
    print(string_text[15:50])


def list_methods():
    list_text = ["Persona 3 Reload", "Persona 4 Golden", "Persona 5 Royal"]
    list_text_toextend = ["Danganronpa", "Danganronpa 2", "Danganronpa V3"]
    print(f"original 2 lists: \n{list_text}\n{list_text_toextend}")

    # Append adds what you want on to the end of the list. Only takes one argument
    list_text.append("Metaphor ReFantazio")
    print(list_text)

    # Extend takes one list and adds it to another
    list_text.extend(list_text_toextend)
    print(list_text)

    # Pop removed the index
    list_text.pop(3)
    print(list_text)

    # Sort sorts a-z 1-10
    list_text.sort()
    print(list_text)

    # Slicing gives the start and inbetween indexes but not the end
    print(list_text[2:4]) 

def dictionary_methods():
    dict_text = {"Name": "Heismay", "Archetype": "Thief", "Level": 28, "Aura": "MAX", "Race": "Eugif"}
    print(f"Original dict_text: \n{dict_text}")

    # Get returns value of key
    print(dict_text.get("Name"))

    # Keys returns all keys 
    print(dict_text.keys())

    # Values returns all values
    print(dict_text.values())

    # Items returns all key-value pairs as tuples
    print(dict_text.items())

    # Update overwrites and adds
    dict_text.update({"Level": 29, "Kidnapper": True, "Follower Level": 2})
    print(dict_text)

    # Pop Removes key and returns item
    print("Popping Follower Level:\n",dict_text.pop("Follower Level"))

    # Pop Item removes the last key value pair
    print(f"Popping item: {dict_text.popitem()}\nNew list: {dict_text}")

    # key in d 
    if "Archetype" in dict_text:
        print("The GOAT has unlocked archetype usage")

    if "Thief" in dict_text.values():
        print("Heismay is using Thief archetype currently")

    # Clear empties whole dictionary
    print(f"Cleaing dictionary:{dict_text.clear()}")
    print(dict_text)



def sets_methods():
    print("Coming soon")

def program():
    while True:
        try:
            user_input = int(input("Welcome to built in methods! Select what data type you want to see: \n"
            "1. String\n"
            "2. Lists\n"
            "3. Dicionaries\n"
            "4. Sets\n"
            "5. Exit program\n"))
            if user_input == 1:
                string_methods()
            elif user_input == 2:
                list_methods()
            elif user_input == 3:
                dictionary_methods()
            elif user_input == 4:
                sets_methods()
            elif user_input == 5:
                print("Exiting program", end ="")   # end="" prevents newline
                for _ in range(3):
                    time.sleep(0.5)     # wait 0.5 seconds
                    print(".", end="", flush=True)  # flush=True means show immediately in terminal instead of buffer 
                time.sleep(0.8)
                print("\nLoading Complete!")
                break
            else:
                print("Please select a valid instruction!")
        except ValueError:
            print("Please select a valid instruction!")


if __name__ == "__main__":
    program()