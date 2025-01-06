class Neighbor:
    def __init__(self, isEvil, side, noisy, nosy):
        self.isEvil = isEvil
        self.side = side
        self.noisy = noisy
        self.nosy = nosy

    def __str__(self):
        return f"I have a neighbor on the {self.side} side, who is {self.isEvil}ly isEvil."
    
    def evil(self):
        if self.isEvil == True:
            return "This neighbor is the spawn of the devil"
        else:
            return "They're sorta cool"
        
    def isNoisy(self):
        if self.noisy == True:
            return "SHUT UP!!!!"
        else:
            return "What neighbor?"
        
ryansneigbor = Neighbor(True, 'Right', True, True)

print(ryansneigbor)
print(ryansneigbor.evil())


class RubberDuck:
    def __init__(self, color, size, squeek, waterproof, material):
        self.color = color
        self.size = size
        self.squeek = squeek
        self.waterproof = waterproof
        self.material = material

    def __str__(self):
        return f"A {self.size} inch {self.color} rubby ducky made of {self.material}"
    
    def isWaterproof(self):
        if self.waterproof == True:
            return f"This rubby ducky is waterproof"
        else:
            return f"This rubby ducky is not waterproof"
        
    def doesSqueek(self):
        if self.squeek == True:
            return "SQUEEK"
        else:
            return "I don't squeek"
            
    

class Flag:
    pass

class Alcohol:
    pass



# duck = RubberDuck("yellow", 13, True, False, "lead")

# print(duck.doesSqueek())
# print(duck)