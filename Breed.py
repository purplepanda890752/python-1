class Dog:
    species = "Canis familiaris"  # Class variable shared by all instances

    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

    def display_details(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")

# Creating instances for two different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Displaying details of the dogs
dog1.display_details()
dog2.display_details()
