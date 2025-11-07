score = 0  # this tracks the score

Capital_of_netherlands = input("What is the capital of the France? ")
if Capital_of_netherlands.lower() == "paris":
    print("Correct!")  # this is the reply if the answer is correct
    score += 1  # this updates the score
else:
    print("Incorrect. The capital of the France is Paris.")  # this is the reply if the answer is incorrect

Capital_of_sweden = input("What is the capital of Sweden? ")
if Capital_of_sweden.lower() == "stockholm":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The capital of Sweden is Stockholm.")

Capital_of_norway = input("What is the capital of Norway? ")
if Capital_of_norway.lower() == "oslo":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The capital of Norway is Oslo.")

Capital_of_denmark = input("What is the capital of Denmark? ")
if Capital_of_denmark.lower() == "copenhagen":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The capital of Denmark is Copenhagen.")

print(f"Your total score is {score} out of 4.")