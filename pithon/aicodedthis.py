import random
import numpy 

class testObject:
    def new(a, b, self):
        self.a = a
        self.b = b
        self.id = str(random.randint(0, 10000) ) + str(random.randint(0, 10000) ) 
        return self

class test:
    def __init__(self):
        self.a = random.randint(0, 100)
        self.b = random.randint(0, 100)

        return testObject.new(self.a, self.b)
    

print (test())