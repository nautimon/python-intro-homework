def user_number():
    while True:
        try:
                question = float(input("Enter a number: "))
                print(f"You entered: {question}")
                break
        except ValueError:
            print("That's not a valid number. Try again.")
user_number()