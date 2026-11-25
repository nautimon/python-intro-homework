def divide_numbers():
        try:
                print("Please enter 2 numbers:")
                number1 = float(input("Enter the numerator: "))
                number2 = float(input("Enter the denominator: "))
                result = number1 / number2
        except ZeroDivisionError:
                print("Can't divide by zero — please try a non-zero denominator.")
                return None
        else:
            print(f"{number1} / {number2} = {result}")
            return result

(divide_numbers())