# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

tickets = []

while True:
    family_member_age = input("Enter the age of the family member:\ntype \"done\" when all ages have been submitted: ")

    if family_member_age == "done":
        break
    else:
        family_member_age = int(family_member_age)

    if family_member_age > 12:
        tickets.append(15)
    elif 3 < family_member_age <= 12:
        tickets.append(10)
    else:
        tickets.append(0)

print(tickets, sum(tickets))


# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted to people over the age of 15.
# Given a list of names, write a program that asks a teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

teenagers = [
    'Tomer',
    'Almog',
    'Yossi',
    'Noar',
    'Ayelet',
    'Muhamed',
    'Vladimir'
]

print(teenagers)

for teen in teenagers:
    teen_age = int(input(f"Hey {teen}! What's your age? "))

    if teen_age > 15:
        print("Enjoy the show")
    else:
        print("Bye Felicia")
        teenagers.remove(teen)

print(teenagers)
