question = input("Enter a positive integer: ")

while not question.isdigit() or question == "0":
    print("That's not a positive integer. Try again")
    question = input("Enter a positive integer: ")

print(f"Got it: {question}")