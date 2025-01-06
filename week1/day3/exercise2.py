# Accept a number from the user and print its multiplication table

number = input("Pick a number: ")

number = int(number)
for i in range(0, 11):
    print(i * number)