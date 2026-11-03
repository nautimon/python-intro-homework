numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
menu = ("""=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit""")


while True:
    print(menu)
    user_choice = int(input("Choose an option (1-5): "))
    if user_choice == 1:
        smallest = numbers[0]
        for num in numbers:
            if num < smallest:
                smallest = num
        print(smallest)

    if user_choice == 2:
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        print(largest)

    if user_choice == 3:
        user_number = int(input("Enter a number: "))
        found = False
        for i in range(len(numbers)):
            if numbers[i] == user_number:
                found = True

                print(f"Found {user_number} at index: {i}")
        if not found:
            print(f"Number was not found.")

    if user_choice == 4:
        def bubble_sort(numbers):
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(numbers) - 1):
                    if numbers[i] > numbers[i + 1]:
                        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                        swapped = True
            return numbers
        bubble_sort(numbers)
        print(numbers)

    if user_choice == 5:
        print("Tootles!")
        break