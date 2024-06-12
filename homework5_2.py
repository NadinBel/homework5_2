class House:
    def __init__(self, numberOfFloors = 0):
        self.numberOfFloors = numberOfFloors
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

print(House().numberOfFloors)
House().setNewNumberOfFloors(6)
