class Mickaelizer:
    def __init__(self, name):
        print(f"Your name isn't {name} anymore, now it's Mickael")
        self.name = 'Mickael'

    def __str__(self):
        return f"{self.name} is the greatest name on the planet!!!!"
    
    def __repr__(self):
        return f"{self.name} Official"
    
    def __call__(self):
        return f"Mickael Mickael Mickael Mickael Mickael"
    
aaron = Mickaelizer('Aaron')
print(aaron)
print(aaron())
print(repr(aaron))