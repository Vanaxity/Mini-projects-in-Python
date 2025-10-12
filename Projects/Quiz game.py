#quiz game

questions = ("What is the capital of France?", "What is the capital of Germany?", "What is the capital of Italy?", "What is the capital of Spain?")

options = (("A. Paris", "B. Berlin", "C. Rome", "D. Madrid"), ("A. Paris", "B. Berlin", "C. Rome", "D. Madrid"), ("A. Paris", "B. Berlin", "C. Rome", "D. Madrid"), ("A. Paris", "B. Berlin", "C. Rome", "D. Madrid"))

answers = ("A", "B", "C", "D")
guesses = []
score = 0 
question_num = 0
 
for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
    question_num += 1

print("--------------------------------")
print("Results")
print("--------------------------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int((score / len(questions)) * 100)
print(f"Your score is: {score}%")

