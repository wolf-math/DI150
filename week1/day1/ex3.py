# Ask the user for a number between 1 and 100

# If the number is a multiple of three, print Fizz

# If the number is a multiple of five, print Buzz.

# If the number is a multiple is a multiples of both three and five, print FizzBuzz instead.

user_number = int(input("give me a number between 1 and 100: "))

if user_number % 15 == 0:
    print("fizzbuzz")
elif user_number % 3 == 0:
    print("fizz")
elif user_number % 5 == 0:
    print("buzz")
else:
    print(user_number)
