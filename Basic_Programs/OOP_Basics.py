# Object oriented programming

class Pet:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    

    def print_info(self):
        print(f"{self.__name} is {self.__age} years old!") 

    def speak(self):
        print(f"{self.__name} says hello!")

    def feed(self):
        print(f"{self.__name} eats!")
         
class Owner:
    def __init__(self, name):
        self.__name = name
        self.__pet = None

    def get_name(self):
        return self.__name
    
    def set_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("PLEASE DON'T TRY OWN ANOTHER OWNER!")
        self.__pet = pet

    
    def get_info(self):
        print(f"{self.__name} is the owners name!")
    
    def walk(self):
        if self.__pet:
            print(f"{self.__name} is walking {self.__pet.get_name()}!")
        else:
            print(f"{self.__name} has no pet to walk!")



def main():
    a1 = Pet("Koromaru", 4)
    a1.print_info()
    a1.speak()
    a1.feed() 
    o1 = Owner("NAME")
    o1.set_pet(a1)
    o1.get_info()
    o1.walk()

    o2 = Owner("Bruh")
    o3 = Owner("Pls dont work")

#    o2.set_pet(o3)     # Raises type error
#    o2.walk()


if __name__ == "__main__":
    main()
