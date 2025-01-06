# Exercise 5: Longest word without a specific character
# Instructions:
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.


sentence = input("Write a sentence without an 'A': ")
score = 0

while 'a' not in sentence:
    if len(sentence) > score:
        score = len(sentence)
        print(f"Congradulations, your score is {score}!!!")
    
        sentence = input("can you think of a longer one?\n")
    else:
        print("That is a lower score. You lose!")
        break

