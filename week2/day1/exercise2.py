people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

greater_than_4 = lambda name : len(name) <= 4

names_under_4 = filter(greater_than_4, people)

greet_names = lambda name : print(f"Hello {name}!")

greet = map(greet_names, names_under_4)

print(list(greet))
