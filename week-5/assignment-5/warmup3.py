names = ["Sarah", "Michael", "Bonnie", "Edward", "Anne", "Samuel"]
username = input("Enter a name to search for: ")
found = False

for i in range(len(names)):
    if names[i] == username:

        found = True
        print(f"Found {username} at index: {i}")
        break

if not found:
    print(f"{username} was not found in the list.")