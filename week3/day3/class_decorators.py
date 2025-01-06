class MyClass:
  @staticmethod
  def add(a, b): 
    return a + b

# print(MyClass.add(3, 6))

# neat = MyClass()
# print(neat.add(16,9))

# class YourClass(MyClass):
#   pass

# apples = YourClass()
# print(apples.add(9,8))

class MyClass:
  __counter = 0

  @classmethod
  def add(cls, a): 
    return cls.__counter + a
  
# tornado = MyClass()

class Person:
    used_names = set()

    def __init__(self, name, age):
        if name in self.used_names:
            name = input("That name is taken. Enter another name: ")

        self.name = name
        self.age = age
        self.used_names.add(name)

    @classmethod
    def fromYear(cls, name, birth_year):
        THIS_YEAR = 2024
        return cls(name, THIS_YEAR - birth_year)

    @property
    def professional_name(self):
        return "Mr " + self.name

billy = Person('Billy', 16)

print(billy.professional_name)



