# numbers = [1,2,3,4,5]

# square_number = lambda number: number**2

# squares = map(square_number, numbers)

# print(list(squares))

nums = [10,30,80,150,200]

# def greater_than_100(number):
#     return number > 100

greater_than_100 = lambda number: number > 100

over_100 = filter(greater_than_100, nums)
print(list(over_100))