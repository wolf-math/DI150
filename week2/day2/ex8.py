from time import sleep


# 🌟 Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct and incorrect answers. Create a list of wrong_answers

def main():
    score = 0
    incorrect_answers = []
    
    for item in data:
        result = question_asker(item["question"], item["answer"])

        if result[0] == "correct":
            score += 1
            print("You got it!")
            sleep(1)
            print(f"Your score is {score}")
            sleep(1)
        else:
            print("You got it wrong. Go rewatch.")
            sleep(1)
            print(f"Your score is {score}")
            sleep(1)
            incorrect_answers.append(result[1])
            print(f"You have {3 - len(incorrect_answers)} chances left.")
            sleep(1)
            print(f"The correct answer was {item["answer"]}, you answered {incorrect_answers[-1]["user_answer"]}")

        if len(incorrect_answers) >= 3:
            print("You Lose!")
            return
        
    if len(incorrect_answers) < 3:
        print("You Win!")



def question_asker(question, answer):
    user_answer = input(f"{question} ")

    if user_answer.lower() == answer.lower():
        return ("correct", {"question": question, "user_answer": user_answer})
    else:
        return ("incorrect", {"question": question, "user_answer": user_answer})


main()


# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.


