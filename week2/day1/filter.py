# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filtered_object = filter(starts_with_A, fruit)
# print(list(filtered_object))

nums = [10,30,80,150,200]

def greater_than_100(number):
    return number > 100

over_100 = filter(greater_than_100, nums)
print(list(over_100))