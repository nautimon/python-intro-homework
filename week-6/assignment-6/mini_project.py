numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

def bubble_sort(numbers):
    sorted_numbers = numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range((len(numbers)) -1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
                swapped = True
    return sorted_numbers

def show_menu():
    menu = ("""===Number Cruncher ===
    1. Find minimum
    2. Find maximum
    3. Search for a number
    4. Sort the list
    5. Quit""")
    print(menu)
    user_choice = (input("Choose an option (1-5): "))
    return user_choice

def main():
    while True:
        user_choice = show_menu()
        if user_choice == "1":
            print(find_min(numbers))
        elif user_choice == "2":
            print(find_max(numbers))
        elif user_choice == "3":
            target = int(input("Give a number: "))
            result = (search(numbers, target))
            if  result == -1:
                print("Not found")
            else:
                print(f"Found at index: {result}")
                
        elif user_choice == "4":
            print(bubble_sort(numbers))
        elif user_choice == "5":
            print("Tootles!")
            break
            
main()