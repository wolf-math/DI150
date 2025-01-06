# class Dog():
#     dogs_king = "Bernie IV"

#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

#     def bark(self):
#         print(f"{self.name} barks ! WAF")

#     def walk(self, number_of_meters):
#         print(f"{self.name} walked {number_of_meters} meters")

#     def rename(self, new_name):
#         self.name = new_name

# my_dog = Dog("Rex")
# my_dog.rename("Paul")

# a_new_dog = Dog("Peanut")

# print(my_dog.name)

# print("The king of the dogs is:", Dog.dogs_king)
# print(f"The king of the {my_dog.name} is:", my_dog.dogs_king)
# print(f"The king of the {a_new_dog.name} is:", a_new_dog.dogs_king)


class Dog():
    number_of_dogs = 0
    dogs_king = "Bernie IV"

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog
        # Increment the number of dogs
        Dog.number_of_dogs += 1

    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")
my_dog2 = Dog("Bernie V")
my_dog3 = Dog("Bernie VI")
my_dog4 = Dog("Bernie VII")
my_dog5 = Dog("Bernie VIII")
my_dog6 = Dog("Bernie IX")
print(f"Curently, there are {Dog.number_of_dogs} dogs")

print(my_dog.number_of_dogs)
