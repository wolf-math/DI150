# fruits = ['apple', 'banana', 'kiwi', 'pear', 'watermelon', 'tomato', 'avocado', 'chicken']

# for fruit in fruits:
#   print(fruit)

# cities = ["Tel Aviv", "San Francisco", "Paris", "Barcelona"]

# for city in cities:
#     print(f"I once went to {city}")

# for number in range(4, 19):
#   print(number)

# home_on_the_range = list(range(0,13))

# print(home_on_the_range)

# current_number = 1 
# while current_number <= 5:    
#     print(current_number)   
#     current_number += 1

# print("Finished")

# password = ''
# while password != 'hello-world-123':
#   password = input('What is the top secret password? ')

# print('You guessed the right password!')

# active = True

# while active: 
#     city = input(" (enter 'quit' when you are finished): ")
#     if city == 'quit':
#         break
#     elif city == 'leave me alone':
#         break
#     elif city == 'stop':
#         break
#     else:
#         print("I'd love to go to", city)
    
#     print("more stuff")

# print("Goodbye !")

# secret_number = 4

# while True:
#   user_number = input('Guess the secret number: ')
#   if int(user_number) == secret_number:
#     print('Congrats! You win!')
#     break
#   else:
#     print('Wrong guess...')

# current_number = 0
# while current_number <= 10:
#     current_number += 1
#     if 3 < current_number < 7: # If the number is between 3 and 7 
#         continue                # Go back to the beginning of the loop
#     print(current_number)

# current = 0
# while current <= 10:
#     print(current)
#     if 3 < current < 7:
#         continue
#     current += 1


basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.insert(0, "Apples")

print(basket)

count = 0
for i in basket:
    if i == "Apples":
        count += 1

print(f"There are {count} Apples in the basket.")

basket.clear()
print(basket)