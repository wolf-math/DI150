# Place a comment next to each variable. The comments will:


# Explain what each variable does
# Find out the type of each
# Format each variable into a print statement

#For example,  
#my_name = "Frank"  this line creates a name variable type: string 
#print("My name is {}".format(my_name))

cars = 100 # sets the variable cars to equal 100
space_in_a_car = 4.0 # sets the number of seats in a car
drivers = 30 # how many drivers there will be
passengers = 90 # how many passengers there will be
cars_not_driven = cars - drivers # the number of cars not driven is euqal to the number of cars minus the number of drivers
cars_driven = drivers # the number of cars that are driven is equal to the number of drivers. Therefore each driver drives exactly 1 car.
carpool_capacity = cars_driven * space_in_a_car # the number of total passengers possible for all the cars.
average_passengers_per_car = passengers / cars_driven # you get the idea...


print(f"There are {cars} cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")