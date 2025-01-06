from datetime import date

today = date.today()

class Car:
    def __init__(self, owner, color, make, model, year):
        self.owner = owner
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.owner} owns a {self.color} {self.make} {self.model} from {self.year}"
    
    def age(self):
        return today.year - self.year
    
    def drive(self):
        if self.age() < 5:
            return f"{self.owner} carefully drove to the store"
        else:
            return f"{self.owner} drove his rustbucket to the store"

    def park(self):
        if self.age() < 5:
            return f"That {self.model} was parked in the driveway"
        else:
            return f"that {self.model} was parked on the street."

my_car = Car('Aaron', 'Green', 'Suzuki', 'SX4', 2013)
elirans_car = Car('Eliran', 'White', 'Nissan', 'Juke', 2022)

my_car.owner = 'Eliran'
elirans_car.owner = 'Aaron'

print(my_car.park())
print(elirans_car.park())