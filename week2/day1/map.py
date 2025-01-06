# def do_something(s):
#     return s + "s"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(do_something, fruit)

# print(list(map_object))

numbers = [1,2,3,4,5]

def square_number(number):
    return number**2

squares = map(square_number, numbers)

print(list(squares))