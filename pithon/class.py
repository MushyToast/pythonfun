import random
import time

class Dog:
    def __init__(self, name=None):
        self.name = name or self.generate_name()
        self.breed = self.generate_breed()
        self.age = 0
        self.barks = 0
        self.is_alive = True
    
    def generate_name(self):
        names = ["Fido", "Buddy", "Max", "Charlie", "Lucy", "Daisy", "Molly", "Sadie", "Rocky", "Riley", "Coco", "Lola", "Milo", "Toby", "Gizmo", "Oscar", "Zeus", "Apollo", "Thor", "Hercules"]
        return random.choice(names)
    
    def generate_breed(self):
        breeds = ["Labrador", "Poodle", "Bulldog", "Beagle", "Golden Retriever", "German Shepherd", "Chihuahua", "Yorkie", "Boxer", "Siberian Husky"]
        return random.choice(breeds)
    
    def check_age(self):
        if self.age > 10:
            self.is_alive = False
            print(f"{self.name} has lived a long and happy life, but it is time for them to rest.")
    
    def bark(self):
        self.check_age()
        if not self.is_alive:
            return
        self.barks += 1
        if self.barks % 10 == 0:
            self.age += 1
            self.check_age()
        print(f"Woof, {self.name}!")

dog1 = Dog()

for x in range(1000):
    dog1.bark()
    time.sleep(0.05)
