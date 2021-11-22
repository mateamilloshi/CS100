#Matea Milloshi
#CS 100 2021F Section 105
#HW11, November 21,2021

class Dog:
    ''' Dog class definition'''
    species = "canis familiaris"
    
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self,trick):
        self.tricks.append(trick)
        print(self.name + " knows " + trick)

    def knows(self,cStr):
        if cStr in self.tricks:
            print("Yes, " + self.name + " knows " + cStr)
        else:
            print("No, " + self.name + " doesn't know " + cStr)
    
