from behaviors import IDigging

class DiggerContainer(IDigging):

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        try:
            if animal.does_dig == True:
                self.animals.append(animal)
                print(f"A(n) {animal} has been added to the digger's container")
            else:
                print(f"A(n) {animal} cannot be put in this container because it does not dig.")
        except AttributeError:
            return 0

    def __str__(self):
        if len(self.animals) == 0:
            return "The digger's container doesn't have any animals in it yet."
        else: 
            animalList = []
            for animal in self.animals:
                animalString = str(animal)
                animalList.append(animalString)
                joinAnimalList = ", ".join(animalList)
            return(f"The digger's container has the following animals in it: {joinAnimalList}")
