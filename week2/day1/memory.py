def my_f1():
    return "Hello"

def my_f2():
    return "Word"

def my_f3():
    return "This is Rick!"

# list_of_functions = [my_f1, my_f2, my_f3]
# print(list_of_functions)

def bigger_function(func):
    zunes = "Zunes!"
    return zunes + func()

print(bigger_function(my_f1))